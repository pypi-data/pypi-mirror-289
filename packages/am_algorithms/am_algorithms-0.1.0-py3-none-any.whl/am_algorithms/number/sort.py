from sortedcontainers import SortedList
from am_algorithms.sort_generic import Sort


class BucketSort(Sort[float]):
    """
    Sorts a list of numbers using the bucket sort algorithm.
    Bucket sort distributes elements into buckets, sorts each bucket individually, and then concatenates the buckets.

    :param nums: The list of numbers to be sorted.
    :return: The sorted list of numbers.
    """
    def sort(self, nums: list[float]) -> list[float]:
        if not nums:
            return nums

        min_value, max_value = min(nums), max(nums)

        num_buckets = int(max_value - min_value + 1)
        buckets = [SortedList() for _ in range(num_buckets)]

        for num in nums:
            buckets[int(num - min_value)].add(num)

        sorted_nums = []
        for bucket in buckets:
            sorted_nums.extend(bucket)

        return sorted_nums
