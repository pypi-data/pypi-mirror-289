from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Generator, MutableMapping, Optional, Sequence, cast, overload

import psycopg2
import psycopg2.extras as extras
from psycopg2._psycopg import connection as Connection
from psycopg2.extras import RealDictRow
from psycopg2.sql import Composable
from pydantic import BaseModel
from rcheck import r

from pnorm import (
    ConnectionAlreadyEstablishedException,
    MultipleRecordsReturnedException,
    NoRecordsReturnedException,
)
from pnorm.credentials import CredentialsDict, CredentialsProtocol, PostgresCredentials
from pnorm.cursors import SingleCommitCursor, TransactionCursor
from pnorm.exceptions import connection_not_created
from pnorm.mapping_utilities import (
    combine_into_return,
    combine_many_into_return,
    get_params,
)
from pnorm.pnorm_types import MappingT, ParamType, T


class PostgresClient:
    def __init__(
        self,
        credentials: CredentialsProtocol | CredentialsDict | PostgresCredentials,
        auto_create_connection: bool = True,
    ) -> None:
        # Want to keep as the PostgresCredentials class for SecretStr
        if isinstance(credentials, PostgresCredentials):
            self.credentials = credentials
        elif isinstance(credentials, dict):
            self.credentials = PostgresCredentials(**credentials)
        else:
            self.credentials = PostgresCredentials(**credentials.as_dict())

        self.connection: Connection | None = None
        self.auto_create_connection = r.check_bool(
            "auto_create_connection",
            auto_create_connection,
        )
        self.cursor: SingleCommitCursor | TransactionCursor = SingleCommitCursor(self)

    def set_schema(self, *, schema: str) -> None:
        schema = r.check_str("schema", schema)
        # self.execute("set search_path to %(search_path)s", {"search_path": schema})
        self.execute(f"set search_path to {schema}")

    @overload
    def get(
        self,
        return_model: type[MappingT],
        query: str | Composable,
        params: Optional[ParamType] = None,
        default: Optional[T] = None,
        combine_into_return_model: bool = False,
    ) -> MappingT: ...

    @overload
    def get(
        self,
        return_model: type[T],
        query: str | Composable,
        params: Optional[ParamType] = None,
        default: Optional[T] = None,
        combine_into_return_model: bool = False,
    ) -> T: ...

    def get(
        self,
        return_model: type[T] | type[MappingT],
        query: str | Composable,
        params: Optional[ParamType] = None,
        default: Optional[T] = None,
        combine_into_return_model: bool = False,
    ) -> T | MappingT:
        """Always returns exactly one record or raises an exception

        This method should be used by default when expecting exactly one row to
        be returned from the SQL query, such as when selecting an object by its
        unique id.

        Parameters
        ----------
        return_model : type[T of BaseModel]
            Pydantic model to marshall the SQL query results into
        query : str
            SQL query to execute
        params : Optional[Mapping[str, Any] | BaseModel] = None
            Named parameters for the SQL query
        default: T of BaseModel | None = None
            The default value to return if no rows are returned
        combine_into_return_model : bool = False
            Whether to combine the params mapping or pydantic model with the
            result of the query into the return_model

        Raises
        ------
        NoRecordsReturnedException
            When the query did not result in returning a record and no default
            was given
        MultipleRecordsReturnedException
            When the query returns at least two records

        Returns
        -------
        get : T of BaseModel
            Results of the SQL query marshalled into the return_model Pydantic model

        Examples
        --------
        >>>
        >>>
        >>>
        """
        query_params = get_params("Query Params", params)

        with self._handle_auto_connection():
            with self.cursor(self.connection) as cursor:
                cursor.execute(query, query_params)
                query_result = cast(list[RealDictRow], cursor.fetchmany(2))

        if len(query_result) >= 2:
            msg = f"Received two or more records for query: {self._query_as_string(query)}"
            raise MultipleRecordsReturnedException(msg)

        single: dict[str, Any] | BaseModel
        if len(query_result) == 0:
            if default is None:
                msg = f"Did not receive any records for query: {self._query_as_string(query)}"
                raise NoRecordsReturnedException(msg)

            single = default
        else:
            single = query_result[0]

        return combine_into_return(
            return_model,
            single,
            params if combine_into_return_model else None,
        )

    @overload
    def find(
        self,
        return_model: type[MappingT],
        query: str | Composable,
        params: Optional[ParamType] = None,
        *,
        default: MappingT,
        combine_into_return_model: bool = False,
    ) -> MappingT: ...

    @overload
    def find(
        self,
        return_model: type[T],
        query: str | Composable,
        params: Optional[ParamType] = None,
        *,
        default: T,
        combine_into_return_model: bool = False,
    ) -> T: ...

    @overload
    def find(
        self,
        return_model: type[MappingT],
        query: str | Composable,
        params: Optional[ParamType] = None,
        *,
        default: Optional[MappingT] = None,
        combine_into_return_model: bool = False,
    ) -> MappingT | None: ...

    @overload
    def find(
        self,
        return_model: type[T],
        query: str | Composable,
        params: Optional[ParamType] = None,
        *,
        default: Optional[T] = None,
        combine_into_return_model: bool = False,
    ) -> T | None: ...

    def find(
        self,
        return_model: type[T] | type[MappingT],
        query: str | Composable,
        params: Optional[ParamType] = None,
        *,
        default: Optional[T | MappingT] = None,
        combine_into_return_model: bool = False,
    ) -> T | MappingT | None:
        """Return the first result if it exists

        [desc]

        Parameters
        ----------
        return_model : type[T of BaseModel]
            Pydantic model to marshall the SQL query results into
        query : str
            SQL query to execute
        params : Optional[Mapping[str, Any] | BaseModel] = None
            Named parameters for the SQL query
        default: T of BaseModel | None = None
            The default value to return if no rows are returned
        combine_into_return_model : bool = False
            Whether to combine the params mapping or pydantic model with the
            result of the query into the return_model

        Returns
        -------
        find : T of BaseModel | None
            Results of the SQL query marshalled into the return_model Pydantic model
            or None if no rows returned

        Examples
        --------
        >>>
        >>>
        >>>
        """
        query_params = get_params("Query Params", params)
        query_result: RealDictRow | BaseModel | MappingT | None

        with self._handle_auto_connection():
            with self.cursor(self.connection) as cursor:
                cursor.execute(query, query_params)
                query_result = cast(RealDictRow | None, cursor.fetchone())

        if query_result is None or len(query_result) == 0:
            if default is None:
                return None

            query_result = default

        return combine_into_return(
            return_model,
            query_result,
            params if combine_into_return_model else None,
        )

    @overload
    def select(
        self,
        return_model: type[T],
        query: str | Composable,
        params: Optional[ParamType] = None,
    ) -> tuple[T, ...]: ...

    @overload
    def select(
        self,
        return_model: type[MappingT],
        query: str | Composable,
        params: Optional[ParamType] = None,
    ) -> tuple[MappingT, ...]: ...

    def select(
        self,
        return_model: type[T] | type[MappingT],
        query: str | Composable,
        params: Optional[ParamType] = None,
    ) -> tuple[T, ...] | tuple[MappingT, ...]:
        """Return all rows

        Parameters
        ----------
        return_model : type[T of BaseModel]
            Pydantic model to marshall the SQL query results into
        query : str
            SQL query to execute
        params : Optional[Mapping[str, Any] | BaseModel] = None
            Named parameters for the SQL query

        Returns
        -------
        select : tuple[T of BaseModel, ...]
            Results of the SQL query marshalled into the return_model Pydantic model

        Examples
        --------
        >>>
        >>>
        >>>
        """
        query_params = get_params("Query Params", params)

        with self._handle_auto_connection():
            with self.cursor(self.connection) as cursor:
                cursor.execute(query, query_params)
                query_result = cast(list[RealDictRow], cursor.fetchall())

        if len(query_result) == 0:
            return tuple()

        return combine_many_into_return(return_model, query_result)

    # todo: select using fetchmany for pagination

    def execute(
        self,
        query: str | Composable,
        params: Optional[ParamType] = None,
    ) -> None:
        """Execute a SQL query

        [desc]

        Parameters
        ----------
        query : str
            SQL query to execute
        params : Optional[Mapping[str, Any] | BaseModel] = None
            Named parameters for the SQL query

        Examples
        --------
        >>>
        >>>
        >>>
        """
        query_params = get_params("Query Params", params)

        with self._handle_auto_connection():
            with self.cursor(self.connection) as cursor:
                cursor.execute(query, query_params)

    @overload
    def execute_values(
        self,
        query: str | Composable,
        values: Optional[
            Sequence[BaseModel] | Sequence[MutableMapping[str, Any]]
        ] = None,
        *,
        template: Optional[Sequence[str]] = None,
        return_model: type[MappingT],
    ) -> tuple[MappingT, ...]: ...

    @overload
    def execute_values(
        self,
        query: str | Composable,
        values: Optional[
            Sequence[BaseModel] | Sequence[MutableMapping[str, Any]]
        ] = None,
        *,
        template: Optional[Sequence[str]] = None,
        return_model: type[T],
    ) -> tuple[T, ...]: ...

    @overload
    def execute_values(
        self,
        query: str | Composable,
        values: Optional[
            Sequence[BaseModel] | Sequence[MutableMapping[str, Any]]
        ] = None,
        *,
        template: Optional[Sequence[str]] = None,
        return_model: None = None,
    ) -> None: ...

    def execute_values(
        self,
        query: str | Composable,
        values: Optional[Sequence[BaseModel] | Sequence[MappingT]] = None,
        *,
        template: Optional[Sequence[str]] = None,
        return_model: Optional[type[T] | type[MappingT]] = None,
    ) -> tuple[T, ...] | tuple[MappingT, ...] | None:
        """Execute a sql query with values

        Parameters
        ----------
        query : str
            SQL query to execute
        values :

        template :


        Examples
        --------
        >>>
        >>>
        >>>
        """
        data: list[Any] | dict[str, Any] = []

        if values is None:
            data = get_params("Values", values)
        elif isinstance(values, list) and isinstance(values[0], tuple):
            data = values
        else:
            data = [tuple(get_params("Query params", v).values()) for v in values]

        with self._handle_auto_connection():
            with self.cursor(self.connection) as cursor:
                extras.execute_values(cursor, query, data, template)

                if return_model is None:
                    return

                query_result = cast(list[RealDictRow], cursor.fetchall())

        if len(query_result) == 0:
            return tuple()

        return combine_many_into_return(return_model, query_result)

    def _create_connection(self) -> None:
        if self.connection is not None:
            raise ConnectionAlreadyEstablishedException()

        # self.connection = psycopg2.connect(**self.credentials.as_dict())

        self.connection = psycopg2.connect(**self.credentials.as_dict())
        # self.connection = psycopg.connect(**self.credentials.as_dict(), row_factory=psycopg.rows.dict_row)

    def _end_connection(self) -> None:
        if self.connection is None:
            connection_not_created()

        self.cursor.close()
        self.connection.close()
        self.connection = None

    def _rollback(self) -> None:
        if self.connection is None:
            connection_not_created()

        self.connection.rollback()

    def _create_transaction(self) -> None:
        self.cursor = TransactionCursor(self)

    def _end_transaction(self) -> None:
        self.cursor.commit()
        self.cursor = SingleCommitCursor(self)

    @contextmanager
    def _handle_auto_connection(self) -> Generator[None, None, None]:
        close_connection_after_use = False

        if self.auto_create_connection:
            if self.connection is None:
                self._create_connection()
                close_connection_after_use = True
        elif self.connection is None:
            connection_not_created()

        try:
            yield
        finally:
            if close_connection_after_use:
                self._end_connection()

    def _query_as_string(self, query: str | Composable) -> str:
        if isinstance(query, str):
            return query

        with self._handle_auto_connection():
            with self.cursor(self.connection) as cursor:
                return query.as_string(cursor)

    @contextmanager
    def start_transaction(self) -> Generator[PostgresClient, None, None]:
        self._create_transaction()

        try:
            yield self
        except:
            self._rollback()
            raise
        finally:
            self._end_transaction()

    @contextmanager
    def start_session(
        self,
        *,
        schema: Optional[str] = None,
    ) -> Generator[PostgresClient, None, None]:
        original_auto_create_connection = self.auto_create_connection
        self.auto_create_connection = False
        close_connection_after_use = False

        if self.connection is None:
            self._create_connection()
            close_connection_after_use = True

        if schema is not None:
            self.set_schema(schema=schema)

        try:
            yield self
        except:
            self._rollback()
            raise
        finally:
            if self.connection is not None and close_connection_after_use:
                self._end_connection()

            self.auto_create_connection = original_auto_create_connection
