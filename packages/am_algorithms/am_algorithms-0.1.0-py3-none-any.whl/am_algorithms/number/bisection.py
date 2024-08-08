from abc import ABC, abstractmethod
from typing import Callable


class Bisection(ABC):
    @abstractmethod
    def bisection_method(self, func: Callable[[float], float], a: float, b: float, epsilon: float) -> float:
        pass


class BisectionIter(Bisection):
    def bisection_method(self, func: Callable[[float], float], a: float, b: float, epsilon: float) -> float:
        """
        Finds a root of the function 'func' within the interval [a, b] using the iterative bisection method.

        This method repeatedly divides the interval in half and selects the subinterval where the function changes sign
        until the interval is smaller than the specified tolerance 'epsilon'. It returns the midpoint of the final interval.

        :param func: The function for which to find the root. It should be callable with a single float argument.
        :param a: The lower bound of the interval.
        :param b: The upper bound of the interval.
        :param epsilon: The tolerance for the root approximation; the method stops when the interval width is less than epsilon.
        :return: An approximation of the root of the function within the given interval.
        :raises ValueError: If 'a' is not less than 'b', or if 'epsilon' is not positive.
        """
        if a >= b:
            raise ValueError("Lower limit 'a' must be less than upper limit 'b'")
        if epsilon <= 0:
            raise ValueError("Tolerance 'epsilon' must be positive")

        if abs(func(a)) < epsilon:
            return a
        if abs(func(b)) < epsilon:
            return b

        while b - a > epsilon:
            midpoint = (a + b) / 2
            f_midpoint = func(midpoint)

            if abs(f_midpoint) < epsilon:
                return midpoint

            a, b = (a, midpoint) if func(a) * f_midpoint < 0 else (midpoint, b)

        return (a + b) / 2


class BisectionRec(Bisection):
    def bisection_method(self, func: Callable[[float], float], a: float, b: float, epsilon: float) -> float:
        """
        Finds a root of the function 'func' within the interval [a, b] using the recursive bisection method.

        This method divides the interval in half and recursively selects the subinterval where the function changes sign
        until the interval width is smaller than the specified tolerance 'epsilon'. It returns the midpoint of the final interval.

        :param func: The function for which to find the root. It should be callable with a single float argument.
        :param a: The lower bound of the interval.
        :param b: The upper bound of the interval.
        :param epsilon: The tolerance for the root approximation; the method stops when the interval width is less than epsilon.
        :return: An approximation of the root of the function within the given interval.
        :raises ValueError: If 'a' is not less than 'b', or if 'epsilon' is not positive.
        """
        if a >= b:
            raise ValueError("Lower limit 'a' must be less than upper limit 'b'")
        if epsilon <= 0:
            raise ValueError("Tolerance 'epsilon' must be positive")

        if abs(func(a)) < epsilon:
            return a
        if abs(func(b)) < epsilon:
            return b

        midpoint = (a + b) / 2

        if b - a <= epsilon:
            return midpoint

        return (self.bisection_method(func, a, midpoint, epsilon) if func(a) * func(midpoint) < 0
                else self.bisection_method(func, midpoint, b, epsilon))