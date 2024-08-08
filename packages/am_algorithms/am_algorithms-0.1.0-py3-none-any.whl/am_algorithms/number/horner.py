from abc import ABC, abstractmethod


class Horner(ABC):
    @abstractmethod
    def value(self, poly: list[float], n: float, x: float) -> float:
        pass


class HornerRec(Horner):
    def value(self, poly: list[float], n: float, x: float) -> float:
        """
        Computes the value of a polynomial at a given point using Horner's method (recursive approach).

        This method recursively evaluates the polynomial by breaking it down into simpler components,
        applying Horner's method to efficiently compute the polynomial value.

        :param poly: List of coefficients of the polynomial, where `poly[i]` is the coefficient of x^i.
        :param n: Degree of the polynomial. Must be non-negative and equal to len(poly) - 1.
        :param x: The point at which the polynomial value is to be computed.
        :return: The computed value of the polynomial at point `x`.
        :raises ValueError: If `n` is negative or if the length of `poly` does not match `n + 1`.
        """
        if n < 0:
            raise ValueError("Degree cannot be negative number")
        if len(poly) != n + 1:
            raise ValueError("Degree and values of polynomial do not match")

        # Helper function for type safety and clarity
        def _value(poly: list[float], n: float, x: float) -> float:
            return poly[0] if n == 0 else poly[n] + x * _value(poly, n - 1, x)

        return _value(poly, n, x)


class HornerIter(Horner):
    def value(self, poly: list[float], n: float, x: float) -> float:
        """
        Computes the value of a polynomial at a given point using Horner's method (iterative approach).

        This method iteratively evaluates the polynomial by applying Horner's method,
        which reduces the number of multiplications and additions needed to compute the polynomial value.

        :param poly: List of coefficients of the polynomial, where `poly[i]` is the coefficient of x^i.
        :param n: Degree of the polynomial. Must be non-negative and equal to len(poly) - 1.
        :param x: The point at which the polynomial value is to be computed.
        :return: The computed value of the polynomial at point `x`.
        :raises ValueError: If `n` is negative or if the length of `poly` does not match `n + 1`.
        """
        if n < 0:
            raise ValueError("Degree cannot be negative number")
        if len(poly) != n + 1:
            raise ValueError("Degree and values of polynomial do not match")

        result = poly[0]
        for i in range(1, n + 1):
            result = result * x + poly[i]

        return result