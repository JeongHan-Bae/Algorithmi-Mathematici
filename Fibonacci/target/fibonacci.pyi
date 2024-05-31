# fibonacci.pyi

from typing import List, Tuple


def fibonacci(n: int, *args) -> int:
    """
    Calculate the nth Fibonacci number.

    Parameters:
    n (int): The position in the Fibonacci sequence (must be non-negative).
    *args: Can either be a tuple (init1, init2) or two individual integers for initial values.

    Returns:
    int: The nth Fibonacci number.
    """
    ...


def fibonacci_list(length: int, n: int = 0, init_vals: Tuple[int, int] = (0, 1)) -> List[int]:
    """
    Generate a list of Fibonacci numbers.

    Parameters:
    length (int): The number of Fibonacci numbers to generate (must be greater than or equal to 1).
    n (int): The starting index for the Fibonacci sequence (must be non-negative, default is 0).
    init_vals (Tuple[int, int]): Initial values for the sequence (default is (0, 1)).

    Returns:
    List[int]: A list of Fibonacci numbers.
    """
    ...
