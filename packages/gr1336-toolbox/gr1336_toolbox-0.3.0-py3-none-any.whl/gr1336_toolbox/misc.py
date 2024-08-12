import importlib.util
from pathlib import Path
from .files import get_files
from typing import Any, TypeAlias, Literal, Callable
from .fast_types import is_array, is_dict, valid_path


def percentage_difference(num1: int, num2: int):
    """
    Calculate the percentage difference between two numbers.

    Parameters:
    - num1 (float): The first number.
    - num2 (float): The second number.

    Returns:
    float: The percentage difference.
    """
    assert (
        num1 != 0
    ), "Cannot calculate percentage difference when the first number is zero."

    percentage_difference = ((num2 - num1) / num1) * 100
    return abs(percentage_difference)


def flatten_list(entry):
    """
    Example:
    ```py
    from grtoolbox.types import flatten_list

    sample = ["test", [[[1]], [2]], 3, [{"last":4}]]
    results = flatten_list(sample)
    # results = ["test", 1, 2, 3, {"last": 4}]
    ```"""
    if is_array(entry):
        return [item for sublist in entry for item in flatten_list(sublist)]
    return [entry] if entry is not None else []


def filter_list(entry: list | tuple, types: TypeAlias) -> list:
    if not is_array(entry, allow_empty=False):
        return []
    return [x for x in entry if isinstance(x, types)]


def dict_to_list(
    entry: dict[str, Any],
    return_item: Literal["key", "content"] = "content",
) -> list:
    res = []
    assert is_dict(
        entry
    ), "the entry provided is not a valid dictionary. Received: {}".format(entry)
    if return_item == "content":
        return list(entry.values())
    return list(entry.keys())


def try_call(comp: Callable, verbose_exception: bool = False, **kwargs):
    """Can be used to call a function prune to errors, it returns its response if successfuly executed, otherwise it prints out an traceback if verbose_exception.

    Args:
        comp (Callable): _description_
        verbose_exception (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    try:
        return comp(**kwargs)
    except Exception as e:
        if verbose_exception:
            print(e)
        return None


def import_functions(
    path: str | Path,
    target_function: str,
):
    """
    Imports and returns all functions from .py files in the specified directory matching a certain function name.

    Args:
        path (str or Path): The path of the directories to search for the Python files.
        target_function (str): The exact string representing the function name to be searched within each file.

    Returns:
        list: A list containing all the functions with the given name found in the specified directory and subdirectories.

    Example:
        >>> import_functions('/path/to/directory', 'some_function')
        [<function some_function at 0x7f036b4c6958>, <function some_function at 0x7f036b4c69a0>]
    """
    results = []
    python_files = [x for x in Path(path).rglob("*.py") if x.is_file()]
    for file in python_files:
        spec = importlib.util.spec_from_file_location(file.name, file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, target_function):
            results.append(getattr(module, target_function))
    return results


def sort_array(array: list | tuple):
    """
    Sorts a list of tuples based on the first element of each tuple.

    Args:
        imports (list of tuple): A list where each element is a tuple,
                                 with the first element being a string or integer.

    Returns:
        list of tuple: The sorted list of import tuples.

    Example:
        >>> sort_imports([(3, 'bar'), (1, 'foo'), (2, 'baz')])
        [(1, 'foo'), (2, 'baz'), (3, 'bar')]
    """
    if is_array(array, allow_empty=False):
        return sorted(array, key=lambda x: x[0])
    return array


__all__ = [
    "import_functions",
    "sort_array",
    "try_call",
    "dict_to_list",
    "filter_list",
    "flatten_list",
    "percentage_difference",
]
