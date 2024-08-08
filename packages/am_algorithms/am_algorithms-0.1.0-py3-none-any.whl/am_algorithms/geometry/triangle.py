from dataclasses import dataclass
from enum import Enum
from am_algorithms.geometry.point import Point


class TriangleType(Enum):
    EQUILATERAL = 1
    ISOSCELES = 2
    RIGHT_ANGLED = 3
    ACUTE = 4
    OBTUSE = 5


@dataclass
class Triangle:
    x: Point
    y: Point
    z: Point

    def get_sides_of_triangle(self) -> tuple[float, float, float]:
        """
        Calculates the lengths of the sides of the triangle based on its vertices.

        :return: A tuple containing the lengths of the sides of the triangle.
        """
        return (
            self.x.distance_to(self.y),
            self.y.distance_to(self.z),
            self.z.distance_to(self.x)
        )

    def area_heron(self) -> float:
        """
        Calculates the area of the triangle using Heron's formula.

        :return: The area of the triangle if it is valid, or -1 if the points do not form a valid triangle.
        """
        a, b, c = self.get_sides_of_triangle()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5 if self.is_triangle(a, b, c) else -1

    def get_triangle_type(self) -> TriangleType:
        """
        Determines the type of the triangle based on its side lengths.

        The method classifies the triangle into one of the following categories:
        - **Equilateral**: All sides are equal.
        - **Isosceles**: At least two sides are equal.
        - **Right-angled**: The triangle satisfies the Pythagorean theorem (a^2 + b^2 = c^2).
        - **Acute**: All angles are less than 90 degrees (a^2 + b^2 > c^2).
        - **Obtuse**: One angle is greater than 90 degrees (a^2 + b^2 < c^2).
        - **Scalene**: All sides are different.

        :return: An integer value representing the type of the triangle, corresponding to the `TriangleType` enum.
                 Returns -1 if the points do not form a valid triangle.
        """
        a, b, c = sorted(self.get_sides_of_triangle())
        epsilon = 1e-6
        a_sq_b_sq_sum, c_square = a ** 2 + b ** 2, c ** 2
        are_ab_equal = abs(a - b) < epsilon
        are_bc_equal = abs(b - c) < epsilon
        are_ac_equal = abs(a - c) < epsilon

        if not self.is_triangle(a, b, c):
            return None

        types = {
            TriangleType.EQUILATERAL: are_ab_equal and are_bc_equal,
            TriangleType.ISOSCELES: are_ab_equal or are_bc_equal or are_ac_equal,
            TriangleType.RIGHT_ANGLED: abs(a_sq_b_sq_sum - c_square) < epsilon,
            TriangleType.ACUTE: a_sq_b_sq_sum > c_square,
            TriangleType.OBTUSE: a_sq_b_sq_sum < c_square
        }

        return next((key for key, condition in types.items() if condition), None)

    @staticmethod
    def is_triangle(a: float, b: float, c: float) -> bool:
        """
        Determines if the given side lengths can form a valid triangle.

        :param a: Length of the first side.
        :param b: Length of the second side.
        :param c: Length of the third side.
        :return: True if the side lengths form a valid triangle, False otherwise.
        """
        return a > 0 and b > 0 and 0 < c < a + b and a + c > b and b + c > a
