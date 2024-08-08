from am_algorithms.sort_generic import InsertionSort


def is_prime(n: float) -> bool:
    """
    Checks if a number is a prime number.
    A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

    :param n: The number to be checked.
    :return: True if the number is prime, False otherwise.
    """

    # ---------------------------------------------------------------------------------------------------------
    """
    The following commented-out code is an alternative method for checking primality.
    It uses a mathematical approach that includes:
    - Directly returning True for 2 and 3
    - Eliminating multiples of 2 and 3 early
    - Checking potential factors up to the square root of n in steps of 6

    limit = int(n ** 0.5) + 1
    return (
        n >= 2 and
        (n == 2 or n == 3 or
         (n % 2 != 0 and n % 3 != 0 and
          all(n % i != 0 and n % (i + 2) != 0 for i in range(5, limit, 6)))
         )
    )
    """
    # ---------------------------------------------------------------------------------------------------------

    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def get_divisors(n: float) -> list[float]:
    """
    Returns a list of all divisors of a given number.
    Divisors are the numbers that divide the given number without leaving a remainder.

    :param n: The number to get divisors of.
    :return: A sorted list of all divisors of the number.
    """
    if n < 1:
        return []

    divs = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)

    return InsertionSort[float]().sort(divs)


def is_perfect_number(n: float) -> bool:
    """
    Checks if a number is a perfect number.
    A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).

    :param n: The number to be checked.
    :return: True if the number is perfect, False otherwise.
    """
    return sum(get_divisors(n)[:-1]) == n


def get_prime_factors(n: float) -> list[float]:
    """
    Returns a list of all prime factors of a given number.
    Prime factors are the prime numbers that multiply together to give the original number.

    :param n: The number to get prime factors of.
    :return: A list of prime factors of the number.
    """
    if n < 2:
        return []

    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n /= 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n /= i

    if n > 2:
        prime_factors.append(n)

    return prime_factors


def get_square_root(num: float, eps: float = 1e-6) -> float:
    """
    Computes the square root of a number using the method of averaging (also known as the Babylonian method or Newton's method).

    :param num: The number to find the square root of. Should be non-negative.
    :param eps: The precision of the result. Default is 1e-6.
    :return: The square root of the number.
    """
    if num <= 0:
        return 0.0

    a = 1.0
    b = num

    while abs(a - b) >= eps:
        a = (a + b) / 2.0
        b = num / a

    return (a + b) / 2.0


def convert_to_base(n: float, base: float) -> str:
    """
    Converts a given number to a specified base and returns it as a string.
    The base should be between 2 and 36, where bases greater than 10 use letters for digits above 9.

    :param n: The number to be converted.
    :param base: The base to convert to (between 2 and 36).
    :return: The number represented in the specified base as a string.
    """
    def helper(n: float, base: float) -> str:
        if n == 0:
            return ""
        else:
            quotient = n // base
            remainder = n % base
            digit_char = chr(55 + remainder) if remainder > 9 else str(remainder)
            return helper(quotient, base) + digit_char

    return "0" if n == 0 else helper(n, base)
