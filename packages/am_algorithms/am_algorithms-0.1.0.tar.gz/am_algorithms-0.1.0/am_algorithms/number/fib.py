from abc import ABC, abstractmethod


class Fibonacci(ABC):
    @abstractmethod
    def value(self, n: float) -> float:
        pass


class NthFibonacciNumberRec(Fibonacci):
    def value(self, n: float) -> float:
        """
        Computes the nth Fibonacci number using a recursive algorithm.

        This method calculates the nth Fibonacci number by recursively summing the two preceding Fibonacci numbers.
        It uses the base cases where the Fibonacci number for 0 is 0 and for 1 is 1.

        :param n: The index of the Fibonacci number to compute.
        :return: The nth Fibonacci number.
        :raises RecursionError: Can cause a stack overflow for large values of n due to deep recursion.
        """
        return n if n <= 1 else self.value(n - 1) + self.value(n - 2)


class NthFibonacciNumberIter(Fibonacci):
    def value(self, n: float) -> float:
        """
        Computes the nth Fibonacci number using an iterative algorithm.

        This method calculates the nth Fibonacci number using a loop, which iteratively computes the next Fibonacci number
        by summing the two preceding numbers. It is more efficient and avoids recursion depth issues.

        :param n: The index of the Fibonacci number to compute.
        :return: The nth Fibonacci number.
        """

        if n <= 1:
            return n

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b

        return b


class NthFibonacciNumberFormula(Fibonacci):
    def value(self, n: float) -> float:
        """
        Computes the nth Fibonacci number using the analytical Binet's formula.

        This method calculates the Fibonacci number using the closed-form expression involving the golden ratio (phi) and
        its conjugate (psi). It provides a direct calculation without recursion or iteration.

        :param n: The index of the Fibonacci number to compute.
        :return: The nth Fibonacci number, rounded to the nearest integer.
        """

        if n <= 1:
            return n

        phi = (1 + (5 ** 0.5)) / 2
        psi = (1 - (5 ** 0.5)) / 2
        return round((phi ** n - psi ** n) / (5 ** 0.5))


def fibonacci_sequence(fibonacci_calc: Fibonacci, n: float) -> list[float]:
    """
    Generates a list of Fibonacci numbers up to the nth number.

    This function uses the provided Fibonacci calculation method to compute and return a list of Fibonacci numbers from
    0 up to n.

    :param fibonacci_calc: An instance of a class implementing the Fibonacci calculation method.
    :param n: The index up to which Fibonacci numbers are computed.
    :return: A list containing Fibonacci numbers from 0 to n.
    """
    return [fibonacci_calc.value(i) for i in range(n + 1)]
