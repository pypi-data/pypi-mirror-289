"""This module is for the event handler's expression
scope interfaces implementations.
"""

from typing import Any
from typing import List
from typing import Optional
from typing import Tuple

from typing_extensions import final

from apysc._type.variable_name_mixin import VariableNameMixIn


class HandlerScope:
    """
    Class for a handler scope. The apysc uses this class at
    a with-statement.
    """

    _handler_name: str
    _instance: VariableNameMixIn

    @final
    def __init__(self, *, handler_name: str, instance: VariableNameMixIn) -> None:
        """
        Class for a handler scope. The apysc uses this class at
        a with-statement.

        Parameters
        ----------
        handler_name : str
            Target handler's name.
        instance : VariableNameMixIn
            Instance will be binded the target handler.
        """
        self._handler_name = handler_name
        self._instance = instance

    @final
    def __enter__(self) -> None:
        """
        Enter and set an event handler scope setting.
        """
        _increment_scope_count()
        _save_handler_calling_stack(
            handler_name=self._handler_name, instance=self._instance
        )

    @final
    def __exit__(self, *args: Any) -> None:
        """
        Exit and remove an event handler scope setting.

        Parameters
        ----------
        *args : list
            Positional arguments.
        """
        _delete_handler_calling_stack(handler_name=self._handler_name)
        _decrement_scope_count()


def _save_handler_calling_stack(
    *, handler_name: str, instance: VariableNameMixIn
) -> None:
    """
    Save the handler calling stack data to the SQLite.

    Parameters
    ----------
    handler_name : str
        Target handler's name.
    instance : VariableNameMixIn
        Instance will be binded the target handler.
    """
    from apysc._expression import expression_data_util

    scope_count: int = get_current_event_handler_scope_count()
    variable_name: str = instance.variable_name
    query: str = (
        "INSERT INTO "
        f"{expression_data_util.TableName.HANDLER_CALLING_STACK.value}"
        "(handler_name, scope_count, variable_name) "
        f"VALUES('{handler_name}', {scope_count}, '{variable_name}');"
    )
    expression_data_util.exec_query(sql=query)


def remove_suffix_num_from_handler_name(*, handler_name: str) -> str:
    """
    Remove the suffix number from a specified handler name.

    Parameters
    ----------
    handler_name : str
        Target handler's name.

    Returns
    -------
    handler_name : str
        Result handler's name.
    """
    splitted: List[str] = handler_name.split("_")
    splitted = splitted[:-1]
    handler_name = "_".join(splitted)
    return handler_name


def _delete_handler_calling_stack(*, handler_name: str) -> None:
    """
    Delete the handler calling stack data from the SQLite.

    Parameters
    ----------
    handler_name : str
        Target handler's name.
    """
    from apysc._expression import expression_data_util

    scope_count: int = get_current_event_handler_scope_count()
    query: str = (
        "DELETE FROM "
        f"{expression_data_util.TableName.HANDLER_CALLING_STACK.value} "
        f"WHERE handler_name = '{handler_name}' "
        f"AND scope_count = {scope_count};"
    )
    expression_data_util.exec_query(sql=query)


class TemporaryNotHandlerScope:
    """
    Class temporarily sets up a scope that is not
    a handler. The apysc uses this at a with-statement.
    """

    _original_scope_count: int

    @final
    def __init__(self) -> None:
        """
        Class temporarily sets up a scope that is not a handler.
        The apysc uses this at a with-statement.
        """
        self._original_scope_count = get_current_event_handler_scope_count()

    @final
    def __enter__(self) -> None:
        """
        Enter and set the scope count to zero.
        """
        _save_current_scope_count(count=0)

    @final
    def __exit__(self, *args: Any) -> None:
        """
        Exit and revert the scope count.

        Parameters
        ----------
        *args : list
            Positional arguments.
        """
        _save_current_scope_count(count=self._original_scope_count)


def _increment_scope_count() -> None:
    """
    Increment current scope count.
    """
    scope_count: int = get_current_event_handler_scope_count()
    scope_count += 1
    _save_current_scope_count(count=scope_count)


def _decrement_scope_count() -> None:
    """
    Decrement current scope count.
    """
    scope_count: int = get_current_event_handler_scope_count()
    scope_count -= 1
    scope_count = max(scope_count, 0)
    _save_current_scope_count(count=scope_count)


def _save_current_scope_count(*, count: int) -> None:
    """
    Save current scope count.

    Parameters
    ----------
    count : int
        Scope count to save.
    """
    from apysc._expression import expression_data_util

    query: str = (
        "DELETE FROM "
        f"{expression_data_util.TableName.EVENT_HANDLER_SCOPE_COUNT.value};"
    )
    expression_data_util.exec_query(sql=query, commit=False)
    query = (
        "INSERT INTO "
        f"{expression_data_util.TableName.EVENT_HANDLER_SCOPE_COUNT.value}"
        f"(count) VALUES({count});"
    )
    expression_data_util.exec_query(sql=query)


def get_current_event_handler_scope_count() -> int:
    """
    Get a current event handler's scope count.

    Returns
    -------
    scope_count : int
        Current event handler's scope count. If normal
        handler's call, then this interface returns 1,
        or call the other handler in handler's function,
        then this interface returns 2 or more count.
    """
    from apysc._expression import expression_data_util

    query: str = (
        "SELECT count FROM "
        f"{expression_data_util.TableName.EVENT_HANDLER_SCOPE_COUNT.value} "
        "LIMIT 1;"
    )
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple] = expression_data_util.cursor.fetchone()
    if result is None:
        return 0
    scope_count: int = int(result[0])
    return scope_count


def current_scope_is_in_event_handler() -> bool:
    """
    Get a boolean indicating whether a current scope is in an event handler
    or not.

    Returns
    -------
    result : bool
        This interface returns True if a current scope is in an event handler.
    """
    scope_count: int = get_current_event_handler_scope_count()
    if scope_count == 0:
        return False
    return True
