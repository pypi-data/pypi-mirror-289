import operator
from am_algorithms.sort_generic import BubbleSort


def is_palindrome(text: str) -> bool:
    """
    Checks if the given string is a palindrome.
    A palindrome is a string that reads the same forward and backward.
    :param text: The string to be checked.
    :return: True if the string is a palindrome, False otherwise.
    """
    return text == text[::-1]


def are_anagrams(t1: str, t2: str) -> bool:
    """
    Determines if two strings are anagrams of each other.
    Two strings are anagrams if they contain the same characters in the same frequency.

    :param t1: The first string.
    :param t2: The second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    if len(t1) != len(t2):
        return False

    counts = {}

    for c1, c2 in zip(t1, t2):
        counts[c1] = counts.get(c1, 0) + 1
        counts[c2] = counts.get(c2, 0) - 1

    return all(count == 0 for count in counts.values())


# TODO czy robic to na sprawdzanie ascii litera po literze ???
def lexicographic_sort(texts: list[str]) -> list[str]:
    """
    Sorts a list of strings in lexicographic (alphabetical) order using bubble sort.
    This method sorts the list in place and returns it.

    :param texts: The list of strings to be sorted.
    :return: The sorted list of strings.
    """

    return BubbleSort[str]().sort(texts)


def naive_string_search(pattern: str, text: str) -> int:
    """
    Searches for the first occurrence of the pattern in the text using a naive approach.
    Returns the position (0-based index) of the first character of the pattern in the text,
    or -1 if the pattern is not found.

    :param pattern: The pattern to search for.
    :param text: The text to search within.
    :return: The starting index of the pattern in the text, or -1 if not found.
    """

    n, m = len(text), len(pattern)
    if m == 0 or n == 0 or m > n:
        return -1

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            return i

    return -1


def evaluate_rpn_expression(expression: str) -> float:
    """
    Evaluates a Reverse Polish Notation (RPN) expression.
    RPN is a mathematical notation in which every operator follows all of its operands.

    :param expression: The RPN expression to evaluate, with tokens separated by spaces.
    :return: The result of the evaluated expression.
    :raises ValueError: If the expression contains invalid characters.
    :raises ZeroDivisionError: If there is a division by zero in the expression.
    """
    valid_tokens = set("0123456789+-*/")
    if any(char not in valid_tokens for char in expression.replace(" ", "")):
        raise ValueError("Invalid characters found in the expression")

    tokens = expression.split()
    stack = []

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in "+-*/":
            b = stack.pop()
            a = stack.pop()

            if token == '/' and b == 0:
                raise ZeroDivisionError("Division by zero error")
            stack.append(operators[token](a, b))

    return stack.pop() if stack else None


