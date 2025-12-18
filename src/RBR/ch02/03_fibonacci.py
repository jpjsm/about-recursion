import time


def time_func(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    delta_secs = time.perf_counter() - start
    return delta_secs, result


def fibonacci_iterative(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("'n' must be a positive number, greater or equal zero.")

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


def fibonacci_recursive(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("'n' must be a positive number, greater or equal zero.")

    if n == 0 or n == 1:
        return n

    return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)


def fibonacci_emulate_recursion(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("'n' must be a positive number, greater or equal zero.")

    callStack = (
        []
    )  # The explicit call stack (to hold 'frame objects': n, state, left, right)
    initialFrame = (n, 0, None, None)
    callStack.append(initialFrame)
    result = None

    while callStack:
        n, state, left, _ = callStack.pop()
        if n <= 1:
            result = n
            continue

        if state == 0:
            # First time seeing this frame: push it back to stack with state=1
            # Then push left frame
            rightFrame = (n, 1, None, None)
            leftFrame = (n - 1, 0, None, None)
            callStack.append(rightFrame)
            callStack.append(leftFrame)
        elif state == 1:
            # left frame done, store result and push right Frame
            rightFrame = (n, 2, result, None)
            leftFrame = (n - 2, 0, None, None)
            callStack.append(rightFrame)
            callStack.append(leftFrame)
        elif state == 2:
            # left frame done, store result and push right Frame
            result = left + result

    return result


if __name__ == "__main__":
    n: int = 2
    delta_i, fib_iterative = time_func(fibonacci_iterative, n)
    print(
        f"        Iterative Fibonacci({n:,}): {fib_iterative:,} in {delta_i*1000} millisecs."
    )
    # delta_r, fib_recursive = time_func(fibonacci_recursive, n)
    # print(
    #     f"        Recursive Fibonacci({n:,}): {fib_recursive:,} in {delta_r*1000} millisecs."
    # )
    delta_e, fib_emulate = time_func(fibonacci_emulate_recursion, n)
    print(
        f"Emulate Recursive Fibonacci({n:,}): {fib_emulate:,} in {delta_e*1000} millisecs."
    )
