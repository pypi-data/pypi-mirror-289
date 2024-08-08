from abc import ABC, abstractmethod


class Gcd(ABC):
    @abstractmethod
    def value(self, a: float, b: float) -> float:
        pass


class GcdSubIter(Gcd):
    def value(self, a: float, b: float) -> float:
        """
        Computes the greatest common divisor (GCD) of two numbers using the iterative subtraction method.

        This method repeatedly subtracts the smaller number from the larger number until one of the numbers becomes zero.
        The non-zero number at this point is the GCD.

        :param a: First number.
        :param b: Second number.
        :return: The GCD of `a` and `b`.
        """
        a, b = abs(a), abs(b)

        while a and b:
            if a > b:
                a -= b
            else:
                b -= a

        return a or b


class GcdSubRec(Gcd):
    def value(self, a: float, b: float) -> float:
        """
        Computes the greatest common divisor (GCD) of two numbers using the recursive subtraction method.

        This method recursively subtracts the smaller number from the larger number until one of the numbers becomes zero
        or both numbers become equal. The common value is the GCD.

        :param a: First number.
        :param b: Second number.
        :return: The GCD of `a` and `b`.
        :raises ValueError: If both `a` and `b` are zero.
        """
        a, b = abs(a), abs(b)
        return (
            b if a == 0 else
            a if (b == 0 or a == b) else
            self.value(a - b, b) if a > b else
            self.value(a, b - a)
        )


class GcdModIter(Gcd):
    def value(self, a: float, b: float) -> float:
        """
        Computes the greatest common divisor (GCD) of two numbers using the iterative modulo method.

        This method repeatedly replaces the larger number by the remainder of the division of the larger number by the smaller number,
        until the remainder is zero. The non-zero number at this point is the GCD.

        :param a: First number.
        :param b: Second number.
        :return: The GCD of `a` and `b`.
        """
        a, b = abs(a), abs(b)

        while b != 0:
            a, b = b, a % b

        return a


class GcdModRec(Gcd):
    def value(self, a: float, b: float) -> float:
        """
        Computes the greatest common divisor (GCD) of two numbers using the recursive modulo method.

        This method recursively replaces the larger number by the remainder of the division of the larger number by the smaller number,
        until the remainder is zero. The remaining non-zero number is the GCD.

        :param a: First number.
        :param b: Second number.
        :return: The GCD of `a` and `b`.
        """
        a, b = abs(a), abs(b)
        return a if b == 0 else self.value(b, a % b)