import importlib.util
from pathlib import Path
from typing import Any, TypeAlias, Literal, Callable
from .fast_types import is_array, is_dict, valid_path
from .files import get_files


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
    validate_path: bool = True,
):
    """Imports from all python files target function in the given path"""
    if validate_path:
        assert valid_path(path), f"Path '{path}' does not exist!"
    results = []
    files = get_files(path, "py")
    for file in files:
        spec = importlib.util.spec_from_file_location(file.name, file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, target_function):
            results.append(getattr(module, target_function))
    return results


__all__ = [
    "import_functions",
    "try_call",
    "dict_to_list",
    "filter_list",
    "flatten_list",
    "percentage_difference",
]
