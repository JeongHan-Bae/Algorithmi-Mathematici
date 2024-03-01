#include <cstring>
#include <iostream>
#include <tuple>

// ANSI escape codes for text color
#define ANSI_COLOR_RED "\x1b[31m"
#define ANSI_COLOR_YELLOW "\x1b[33m"
#define ANSI_COLOR_GREEN "\x1b[32m"
#define ANSI_COLOR_BLUE "\x1b[36m"
#define ANSI_COLOR_CYAN "\033[1;36m"
#define ANSI_COLOR_RESET "\x1b[0m"
#define ANSI_COLOR_LIGHT_YELLOW "\033[1;33m"

std::tuple<int, int> find_in_pascal(int n) {
    if (n == 1) {
        return std::make_tuple(0, 0);
        // Special case: 1 at the top of the triangle
    }

    int row = 2;            // Start at row 2
    int col = 1;            // Start at column 1
    long long int comb = 2; // Initial combination value

    while (true) {
        if (comb < n) {
            if (row / 2 == col) {
                /* At the middle, already the greatest value of this row, move
                 * to the next row
                 */
                row = row + 1;
                comb = comb * row / (row - col);
            } else {
                long long int greater_comb = comb * (row - col) / (col + 1);
                if (greater_comb > n) {
                    /* The value to the right is greater than n, move to the
                     * next row
                     */
                    row = row + 1;
                    comb = comb * row / (row - col);
                } else {
                    col = col + 1;
                    comb = greater_comb;
                }
            }
        } else if (comb > n) {
            // Too large, move left
            col = col - 1;
            comb = comb * (col + 1) / (row - col);
        } else {
            return std::make_tuple(row, col);
            // Found the first occurrence of n
        }

        if (row * (row - 1) / 2 > n) {
            return std::make_tuple(n, 1);
            // No possibility to find n in column greater than 1
        }
    }
}

/**
 * @Usage
 * Example: pascal.exe {positive integer number}
 *
 * @brief Launch the program with a positive integer number as the argument.
 */
int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << ANSI_COLOR_RED "Usage: " << argv[0]
                  << " <number>" ANSI_COLOR_RESET << "\n";
        return 1;
    }

    const char* input = argv[1];
    auto len = std::strlen(input);

    if (len > 10 || (len == 10 && input[0] > '2')) {
        std::cerr << ANSI_COLOR_RED
                     "Error: Input number is too large." ANSI_COLOR_RESET "\n";
        return 1;
    }

    if (len == 10 && std::strcmp(input, "2147483647") > 0) {
        std::cerr << ANSI_COLOR_RED
                     "Error: Input number is too large." ANSI_COLOR_RESET "\n";
        return 1;
    }

    char* end;
    long long num = std::strtoll(input, &end, 10);

    if (*end != '\0' || num < 1LL) {
        std::cerr << ANSI_COLOR_RED
                     "Error: Invalid input."
                     " Please enter a valid positive integer." ANSI_COLOR_RESET "\n";
        return 1;
    }

    if (num > 1073700000) {
        std::cout << ANSI_COLOR_YELLOW
                     "Attention:"
                     " The number is quite large and may take some time to "
                     "calculate." ANSI_COLOR_RESET "\n";
    }

    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    auto [x, y] = find_in_pascal(static_cast<int>(num));
    std::printf("The integer %s%d%s is found at %s(%d,%d)%s %s[0-index]%s"
                " of%s the Pascal triangle%s\n",
                ANSI_COLOR_CYAN, static_cast<int>(num), ANSI_COLOR_RESET,
                ANSI_COLOR_LIGHT_YELLOW, x - 1, y - 1, ANSI_COLOR_RESET,
                ANSI_COLOR_BLUE, ANSI_COLOR_RESET, ANSI_COLOR_GREEN,
                ANSI_COLOR_RESET);

    return 0;
}