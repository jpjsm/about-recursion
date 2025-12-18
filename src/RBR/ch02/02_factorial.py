def factorial_iterative(n: int) -> int:
    if not isinstance(n, int) or n < 1:
        raise ValueError("'n' must be a positive number, greater than zero.")

    factorial = 1
    for i in range(n, 0, -1):
        factorial *= i

    return factorial


def factorial_recursive(n: int) -> int:
    if not isinstance(n, int) or n < 1:
        raise ValueError("'n' must be a positive number, greater than zero.")

    if n == 1:
        return 1

    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    n: int = 995
    print(f"Iterative Factorial({n:,}): {factorial_iterative(n)}")
    print(f"Recursive Factorial({n:,}): {factorial_recursive(n)}")
