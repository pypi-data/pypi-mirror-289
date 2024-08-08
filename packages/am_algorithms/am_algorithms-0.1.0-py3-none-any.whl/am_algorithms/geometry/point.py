from dataclasses import dataclass
from typing import Self
from enum import Enum


class Position(Enum):
    POINT_IS_ON_THE_LINE = 0
    POINT_IS_ON_THE_LEFT_SIDE_OF_THE_LINE = 1
    POINT_IS_ON_THE_RIGHT_SIDE_OF_THE_LINE = 2


@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: Self) -> float:
        """
        Calculates the Euclidean distance between this point and another point.

        :param other: The other point to which the distance is calculated.
        :return: The Euclidean distance between the two points.
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def position_relative_to_line(self, p1: Self, p2: Self) -> int:
        """
        Determines the relative position of the point with respect to the line defined by two other points.

        The method uses the cross product to determine if the point is on the line, or to the left or right of the line.
        A cross product of zero indicates that the point is on the line, a positive cross product indicates that
        the point is on the left side of the line, and a negative cross product indicates that the point is on
        the right side of the line.

        :param p1: The first point defining the line.
        :param p2: The second point defining the line.
        :return: An integer representing the position of the point:
                 - Position.POINT_IS_ON_THE_LINE.value if the point lies on the line.
                 - Position.POINT_IS_ON_THE_LEFT_SIDE_OF_THE_LINE.value if the point is on the left side.
                 - Position.POINT_IS_ON_THE_RIGHT_SIDE_OF_THE_LINE.value if the point is on the right side.
        """
        vx1 = p2.x - p1.x
        vy1 = p2.y - p1.y
        vx2 = self.x - p1.x
        vy2 = self.y - p1.y

        cross_product = vx1 * vy2 - vy1 * vx2

        return (
            Position.POINT_IS_ON_THE_LINE.value) if cross_product == 0 else (
            Position.POINT_IS_ON_THE_LEFT_SIDE_OF_THE_LINE.value if cross_product > 0 else
            Position.POINT_IS_ON_THE_RIGHT_SIDE_OF_THE_LINE.value
        )

    def point_on_segment(self, segment_start: Self, segment_end: Self) -> bool:
        """
        Checks whether the point lies on the line segment defined by two other points.

        The method first checks if the point is within the bounding box defined by the segment's endpoints.
        It then checks if the cross product is close to zero to determine if the point is on the line segment.

        :param segment_start: The starting point of the line segment.
        :param segment_end: The ending point of the line segment.
        :return: True if the point is exactly on the segment between segment_start and segment_end.
                 False otherwise.
        """
        x_within_bounds = min(segment_start.x, segment_end.x) <= self.x <= max(segment_start.x, segment_end.x)
        y_within_bounds = min(segment_start.y, segment_end.y) <= self.y <= max(segment_start.y, segment_end.y)

        if not x_within_bounds or not y_within_bounds:
            return False

        cross_product = (self.y - segment_start.y) * (segment_end.x - segment_start.x) - (self.x - segment_start.x) * (
                    segment_end.y - segment_start.y)
        return abs(cross_product) < 1e-9

    def cross_product(self, p1: Self, p2: Self) -> int:
        """
        Calculates the cross product of vectors formed by the point and two other points to determine the orientation of the turn.

        The cross product helps in determining the relative orientation of the turn made by moving from the first point
        to the second point with respect to the line segment defined by the point.

        :param p1: The first point used to form the vector.
        :param p2: The second point used to form the vector.
        :return:
            1 if the cross product is positive (indicating a counter-clockwise turn),
            2 if the cross product is negative (indicating a clockwise turn),
            0 if the cross product is zero (indicating collinearity).
        """
        val = (float(p1.y - self.y) * (p2.x - p1.x)) - (float(p1.x - self.x) * (p2.y - p1.y))
        return (
            1 if val > 0 else
            2 if val < 0 else
            0
        )

    def is_on_segment(self, p1: Self, p2: Self) -> bool:
        """
        Determines if the point lies within the bounds of the line segment defined by two other points.

        The method checks if the point's coordinates fall within the minimum and maximum x and y values of the segment's endpoints.

        :param p1: One endpoint of the line segment.
        :param p2: The other endpoint of the line segment.
        :return: True if the point lies on the segment between p1 and p2.
                 False otherwise.
        """
        return min(p1.x, p2.x) <= self.x <= max(p1.x, p2.x) and min(p1.y, p2.y) <= self.y <= max(p1.y, p2.y)


def do_segments_intersect(p1: Point, q1: Point, p2: Point, q2: Point) -> bool:
    """
    Determines whether two line segments, defined by four points, intersect each other.

    The function calculates the cross products of vectors to determine the orientation of the endpoints of the segments.
    It then checks if the segments intersect based on these orientations or if any of the endpoints of one segment lie on
    the other segment.

    :param p1: One endpoint of the first line segment.
    :param q1: The other endpoint of the first line segment.
    :param p2: One endpoint of the second line segment.
    :param q2: The other endpoint of the second line segment.
    :return: True if the segments intersect each other, either by crossing or touching.
             False if the segments do not intersect.
    """
    v1 = p1.cross_product(q1, p2)
    v2 = p1.cross_product(q1, q2)
    v3 = p2.cross_product(q2, p1)
    v4 = p2.cross_product(q2, q1)

    return (
            ((v1 != v2) and (v3 != v4)) or
            (v1 == 0 and p2.is_on_segment(p1, q1)) or
            (v2 == 0 and q2.is_on_segment(p1, q1)) or
            ((v3 == 0 and p1.is_on_segment(p2, q2)) or
            (v4 == 0 and q1.is_on_segment(p2, q2)))
    )
