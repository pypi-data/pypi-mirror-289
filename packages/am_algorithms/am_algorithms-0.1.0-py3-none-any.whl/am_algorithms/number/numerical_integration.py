from abc import ABC, abstractmethod
from typing import Callable


class NumericalIntegration(ABC):
    @abstractmethod
    def integrate(self, func: Callable[[float], float], a: float, b: float, n: float) -> float:
        pass


class IntegrationTrapezoidalMethod(NumericalIntegration):
    """
    Computes the definite integral of a function using the trapezoidal rule.

    The trapezoidal rule approximates the integral of a function by dividing the interval [a, b] into n subintervals,
    calculating the area of trapezoids formed by the function values at the endpoints of these subintervals, and summing them.

    :param func: The function to integrate. Should take a single float argument and return a float.
    :param a: The lower limit of integration.
    :param b: The upper limit of integration.
    :param n: The number of subintervals to divide the integration range into.
    :return: The approximate value of the integral.
    :raises ValueError: If `a` is not less than `b` or if `n` is less than or equal to zero.
    """
    def integrate(self, func: Callable[[float], float], a: float, b: float, n: float) -> float:
        if a >= b:
            raise ValueError("Lower limit 'a' must be less than upper limit 'b'")
        if n <= 0:
            raise ValueError("Number of subintervals 'n' must be positive")

        h = (b - a) / float(n)
        integral_sum = 0.0
        base_a = func(a)

        for i in range(1, n):
            base_b = func(a + h * i)
            integral_sum += (base_a + base_b)
            base_a = base_b

        return integral_sum * 0.5 * h


class IntegrationRectangleMethod(NumericalIntegration):
    """
    Computes the definite integral of a function using the rectangle (midpoint) rule.

    The rectangle rule approximates the integral of a function by dividing the interval [a, b] into n subintervals,
    calculating the area of rectangles with heights given by the function values at the midpoints of these subintervals,
    and summing them.

    :param func: The function to integrate. Should take a single float argument and return a float.
    :param a: The lower limit of integration.
    :param b: The upper limit of integration.
    :param n: The number of subintervals to divide the integration range into.
    :return: The approximate value of the integral.
    :raises ValueError: If `a` is not less than `b` or if `n` is less than or equal to zero.
    """
    def integrate(self, func: Callable[[float], float], a: float, b: float, n: float) -> float:
        if a >= b:
            raise ValueError("Lower limit 'a' must be less than upper limit 'b'")
        if n <= 0:
            raise ValueError("Number of subintervals 'n' must be positive")

        h = (b - a) / float(n)
        integral_sum = 0.0
        midpoint = a + (h / 2.0)

        for _ in range(n):
            integral_sum += func(midpoint)
            midpoint += h

        return integral_sum * h