import sys
from typing import Tuple

# ANSI escape codes for text color
ANSI_COLOR_RED = "\x1b[31m"
ANSI_COLOR_YELLOW = "\x1b[33m"
ANSI_COLOR_GREEN = "\x1b[32m"
ANSI_COLOR_BLUE = "\x1b[36m"
ANSI_COLOR_CYAN = "\033[1;36m"
ANSI_COLOR_RESET = "\x1b[0m"
ANSI_COLOR_LIGHT_YELLOW = "\033[1;33m"


def find_in_pascal(n: int) -> Tuple[int, int]:
    """
    Find the position of a number in Pascal's triangle.
    Returns a tuple representing the (row, column) of the number.
    """
    if n == 1:
        return (0, 0)  # Special case: 1 at the top of the triangle

    row: int = 2  # Start at row 2
    col: int = 1  # Start at column 1
    comb: int = 2  # Initial combination value as long int

    while True:
        if comb < n:
            if row // 2 == col:
                # At the middle, already the greatest value of this row, move to the next row
                row += 1
                comb = comb * row // (row - col)
            else:
                greater_comb: int = comb * (row - col) // (col + 1)
                if greater_comb > n:
                    # The value to the right is greater than n, move to the next row
                    row += 1
                    comb = comb * row // (row - col)
                else:
                    col += 1
                    comb = greater_comb
        elif comb > n:
            # Too large, move left
            col -= 1
            comb = comb * (col + 1) // (row - col)
        else:
            return (row, col)  # Found the first occurrence of n

        if row * (row - 1) // 2 > n:
            return (n, 1)  # No possibility to find n in column greater than 1


if __name__ == "__main__":
    """
    To use the program, run the following command in the console:

    python pascal.py <positive integer number>

    Example:
    python pascal.py 3003
    """
    if len(sys.argv) != 2:
        print(
            ANSI_COLOR_RED + "Usage: python3",
            sys.argv[0],
            "<number>" + ANSI_COLOR_RESET,
        )
        sys.exit(1)

    input_str = sys.argv[1]
    if len(input_str) > 10 or (len(input_str) == 10 and input_str[0] > "2"):
        print(ANSI_COLOR_RED + "Error: Input number is too large." + ANSI_COLOR_RESET)
        sys.exit(1)

    if len(input_str) == 10 and input_str > "2147483647":
        print(ANSI_COLOR_RED + "Error: Input number is too large." + ANSI_COLOR_RESET)
        sys.exit(1)

    try:
        num = int(input_str)
        if num < 1:
            raise ValueError
    except ValueError:
        print(
            ANSI_COLOR_RED
            + "Error: Invalid input. Please enter a valid positive integer."
            + ANSI_COLOR_RESET
        )
        sys.exit(1)

    if num > 1073700000:
        print(
            ANSI_COLOR_YELLOW
            + "Attention: The number is quite large and may take some time to calculate."
            + ANSI_COLOR_RESET
        )

    x, y = find_in_pascal(num)
    print(
        "The integer",
        ANSI_COLOR_CYAN + str(num) + ANSI_COLOR_RESET,
        "is found at",
        ANSI_COLOR_LIGHT_YELLOW + f"({x-1},{y-1})" + ANSI_COLOR_RESET,
        "[0-index] of",
        ANSI_COLOR_GREEN + "the Pascal triangle" + ANSI_COLOR_RESET,
    )
