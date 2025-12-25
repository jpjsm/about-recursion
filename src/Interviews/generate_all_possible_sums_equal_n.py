"""This function generates of possible sums of possitive numbers greater than
zero that add up to 'n'

For example, given N = 4

The answers will be
- 4
- 3 + 1
- 2 + 2
- 2 + 1 + 1
- 1 + 1 + 1 + 1
"""

from typing import List, Set, Tuple


def tuple_to_sorted_string(t: Tuple[int, ...]) -> str:
    l = list(t)
    return "|".join(str(i) for i in sorted(l))


def sums_of_number(n: int) -> List[Tuple[int, ...]]:
    if n < 1:
        raise ValueError("'n' must be possitive greater than zero.")
    if n == 1:
        return [tuple([1])]

    numbers: List[Tuple[int, ...]] = [tuple([n])]
    duplicates_check: Set[str] = set(tuple_to_sorted_string(tuple([n])))
    # left * [right]
    for l in range(n - 1, 0, -1):
        for left in sums_of_number(l):
            for right in sums_of_number(n - l):
                sol = tuple(list(left) + list(right))
                sol_str = tuple_to_sorted_string(sol)
                if sol_str not in duplicates_check:
                    numbers.append(sol)
                    duplicates_check.add(sol_str)

    return list(numbers)


if __name__ == "__main__":
    for i in range(1, 5):
        sols = sums_of_number(i)
        print(i, "|", sols)
