"""You get as input a single string (of characters, text) containing an
expression that has the following format:

- It is enclosed in parentheses;
- These contain an operator, either '+' or '*';
- Which is followed by two (no more and no less) operands,
  each of which is either an integer or another expression in the same format.
- Evaluate the expression:
  - The value of an expression is the sum of the values of the two operands if
  its operator is a '+' character;
  - on the other hand, when the operator is a '*' character, the value is the
  product of the two operands.
  - The value of an integer is the integer itself.

Note:
Each pair of parentheses contain exactly one operator and two operands;
parentheses determine order of precedence.

For example: "( * 2 ( + 3 4 ) )" evaluates to 14 [ via 3+4=7, 2*7=14 ].

"""

from typing import Tuple


DEFINED_OPERATORS = set(["*", "+"])
DEFINED_WHITESPACES = set([" ", "\t", "\r", "\n"])
DEFINED_NUMBERS = set(str(i) for i in range(10))


def find_rightmostclosingparenthesis(text: str) -> int:
    """Finds the position of rightmost closing parentesis, or returns -1 if
    there's an unbalanced number of [open, close] parentheses.


    Args:
        text (str): The expression text to search for the rightmost closing
        parenthesis

    Returns:
        int: the position in 'text' of the rightmost closing parentheses, or
        -1 if there is an unbalanced number of clossing parenthesis.

    Exception:
        ValueError: if first char of string is not an opening parentheses
    """
    if text[0] != "(":
        raise ValueError("'text' must begin with '('.")

    open_count = 1
    i = 1
    text_len = len(text)
    while i < text_len:
        if text[i] == "(":
            open_count += 1
        elif text[i] == ")":
            open_count -= 1
            if open_count == 0:
                break

        i += 1

    return i if open_count == 0 else -1


def find_firstopeningparentheses(text: str) -> int:
    """Finds the first opening parentheses in text

    Args:
        text (str): _description_

    Returns:
        int: _description_
    """
    text_len = len(text)
    for i in range(text_len):
        if text[i] == "(":
            return i
    return -1


def get_operand(exp: str) -> Tuple[bool, int, str]:
    ## Skip whitespaces
    i = 0
    while exp[i] in DEFINED_WHITESPACES:
        i += 1

    ## Check for number
    is_number = exp[i] in DEFINED_NUMBERS
    if is_number:
        value = int(exp[i])
        i += 1
        while exp[i] in DEFINED_NUMBERS:
            value *= 10
            value += int(exp[i])
            i += 1

        return (True, value, exp[i:].strip())
    elif exp[i] == "(":
        right_mostclosingparentheses = find_rightmostclosingparenthesis(exp[i:])
        new_exp = exp[i : right_mostclosingparentheses + 1 + i]
        return (False, 0, new_exp)
    raise ValueError("Not a valid Operand syntax")


def prefix_expression_evaluator(exp: str) -> int:
    """Evaluate the prefix expression
    You get as input a single string (of characters, text) containing an expression
    that has the following format:

    - It is enclosed in parentheses;
    - These contain an operator, either '+' or '*';
    - Which is followed by two (no more and no less) operands,
    each of which is either an integer or another expression in the same format.
    - Evaluate the expression:
    - The value of an expression is the sum of the values of the two operands if
    its operator is a '+' character;
    - on the other hand, when the operator is a '*' character, the value is the
    product of the two operands.
    - The value of an integer is the integer itself.

    Note:
    Each pair of parentheses contain exactly one operator and two operands;
    parentheses determine order of precedence.

    For example: "( \* 2 ( + 3 4 ) )" evaluates to 14 [ via 3+4=7, 2*7=14 ].
    Args:
        exp (str): The expression to evaluate

    Returns:
        int: The result of the expression evaluated
    """
    exp = exp.strip()
    if find_rightmostclosingparenthesis(exp) == -1:
        raise ValueError("Expression has an unbalanced number of parentheses")

    exp_len = len(exp)
    # find operator
    i = 1
    while (
        i < exp_len
        and exp[i] not in DEFINED_OPERATORS
        and exp[i] in DEFINED_WHITESPACES
    ):
        i += 1

    if exp[i] not in DEFINED_OPERATORS:
        raise ValueError("operator not found as first element of expression")

    operator = exp[i]
    i += 1
    # get value of left operand
    is_value, left, right_operand = get_operand(exp[i:])
    if not is_value:
        left_expression = right_operand
        right_operand = exp[i + len(left_expression) + 1 :]
        left = prefix_expression_evaluator(left_expression)

    # get value of right operand
    is_value, right, right_operand = get_operand(right_operand)
    if not is_value:
        right = prefix_expression_evaluator(right_operand)

    # Evaluate expression and return value

    if operator == "+":
        return left + right
    elif operator == "*":
        return left * right

    raise ValueError("Undefined operator")


if __name__ == "__main__":
    expressions = [
        # "( + 1 2 )",
        # "(+ 1 2)",
        # "( * 2 3 )",
        # "(* 2 3)",
        "(+ (+ 1 2) 3)",
        "(+ 1 (+ 2 3))",
    ]

    for exp in expressions:
        print(exp, "=", prefix_expression_evaluator(exp))
