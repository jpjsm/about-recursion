"""This function generates all combinations of 'n' balanced pairs of
parenthesis.

Usage: balanced_parenthesis(n)
Returns a list of string with all parenthesis combinmations.

For example, for the indicated 'n' the answer would be:

n   | results
1   | ()
2   | ()(), (())
3   | ((())), (()()), (())(),
    | ()(()), ()()()
4   | ()()()(), ()()(()), ()(())(),
    | ()(()()), ()((())), (())()(),
    | (())(()), (()())(), ((()))(),
    | (()()()), (()(())), ((())()),
    | ((()())), (((())))

"""

from typing import List


def balanced_parenthesis(n: int) -> List[str]:
    if n < 0:
        raise ValueError("'n' must be a positive number or zero.")

    if n == 0:
        return [""]

    if n == 1:
        return ["()"]

    solutions: List[str] = []
    # The recursive solution
    # (left) + right

    for l in range(n):
        r = n - 1 - l
        left_sols = balanced_parenthesis(l)
        right_sols = balanced_parenthesis(r)
        for left in left_sols:
            for right in right_sols:
                solutions.append(f"({left}){right}")
    return solutions


if __name__ == "__main__":
    for i in range(4):
        sol = balanced_parenthesis(i)
        print(i, "|", sol)
