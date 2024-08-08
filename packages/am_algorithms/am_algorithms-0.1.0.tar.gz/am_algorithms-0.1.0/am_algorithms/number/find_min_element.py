from abc import ABC, abstractmethod
from typing import Any


class FindMinElement(ABC):
    @abstractmethod
    def value(self, nums: list[int]) -> Any:
        pass


class FindMinElementBySwapping(FindMinElement):
    def value(self, nums: list[int]) -> Any:
        """
        Finds the minimum element in a list of integers by iterating through the list.

        This method initializes the minimum value as the first element of the list and then iterates through
        the rest of the list, updating the minimum value whenever a smaller element is encountered.

        :param nums: List of integers.
        :return: The minimum value found in the list.
        :raises IndexError: If the input list is empty.
        """
        min_val = nums[0]

        for num in nums[1:]:
            if num < min_val:
                min_val = num

        return min_val


class FindMinWithMax(FindMinElement):
    def value(self, nums: list[int]) -> Any:
        """
        Finds both the minimum and maximum elements in a list of integers using a modified comparison approach.

        This method compares elements in pairs to find both the minimum and maximum values. If the list has an odd number
        of elements, it handles the last element separately. The approach ensures that each element is compared at most once.

        :param nums: List of integers.
        :return: A tuple containing the minimum and maximum values found in the list.
        :raises IndexError: If the input list is empty.
        """

        n = len(nums)
        if n == 1:
            min_val = max_val = nums[0]
        else:
            min_val = min(nums[0], nums[1])
            max_val = max(nums[0], nums[1])

            i = 2
            while i <= n - 2:
                max_val, min_val = (max(max_val, nums[i]), min(min_val, nums[i + 1])) if nums[i] > nums[i + 1] \
                    else (max(max_val, nums[i + 1]), min(min_val, nums[i]))
                i += 2

            if n % 2 == 1:
                max_val = max(max_val, nums[-1])
                min_val = min(min_val, nums[-1])

        return min_val, max_val
