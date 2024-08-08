from abc import ABC, abstractmethod
from sortedcontainers import SortedList


class Sort[T](ABC):
    @abstractmethod
    def sort(self, nums: list[T]) -> list[T]:
        pass


class BubbleSort[T](Sort):
    """
    Sorts a list of elements using the bubble sort algorithm.
    Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong
    order. The process is repeated until the list is sorted.

    :param items: The list of elements to be sorted.
    :return: The sorted list of elements.
    """
    def sort(self, items: list[T]) -> list[T]:
        n = len(items)
        for i in range(n):
            for j in range(1, n - i):
                if items[j - 1] > items[j]:
                    items[j - 1], items[j] = items[j], items[j - 1]

        return items


class SelectionSort[T](Sort):
    """
    Sorts a list of elements using the selection sort algorithm.
    Selection sort repeatedly finds the minimum element from the unsorted part and moves it to the beginning.

    :param items: The list of elements to be sorted.
    :return: The sorted list of elements.
    """
    def sort(self, items: list[T]) -> list[T]:
        n = len(items)
        for i in range(n - 1):
            mn_index = i
            for j in range(i + 1, n):
                if items[j] < items[mn_index]:
                    mn_index = j
            items[i], items[mn_index] = items[mn_index], items[i]

        return items


class InsertionSort[T](Sort):
    """
    Sorts a list of elements using the insertion sort algorithm.
    Insertion sort builds the sorted list one item at a time by repeatedly picking the next item and inserting it
    into the correct position.

    :param items: The list of elements to be sorted.
    :return: The sorted list of elements.
    """
    def sort(self, items: list[T]) -> list[T]:
        n = len(items)
        for i in range(1, n):
            key = items[i]
            j = i - 1
            while j >= 0 and items[j] > key:
                items[j + 1] = items[j]
                j -= 1
            items[j + 1] = key

        return items


class MergeSort[T](Sort):
    """
    Sorts a list of elements using the merge sort algorithm.
    Merge sort divides the list into halves, recursively sorts each half, and then merges the sorted halves.

    :param items: The list of elements to be sorted.
    :return: The sorted list of elements.
    """
    def sort(self, items: list[T]) -> list[T]:
        self._merge_sort(items, 0, len(items) - 1)
        return items

    # Method to perform merge sort.
    def _merge_sort(self, items: list[T], left: T, right: T):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(items, left, mid)
            self._merge_sort(items, mid + 1, right)
            self._merge(items, left, mid, right)

    # Method to merge two halves of the array.
    def _merge(self, items: list[T], left: float, mid: float, right: float):
        i = left
        j = mid + 1
        k = left
        tmp = items[:]

        while i <= mid and j <= right:
            if tmp[i] <= tmp[j]:
                items[k] = tmp[i]
                i += 1
            else:
                items[k] = tmp[j]
                j += 1
            k += 1

        while i <= mid:
            items[k] = tmp[i]
            i += 1
            k += 1

        while j <= right:
            items[k] = tmp[j]
            j += 1
            k += 1


class QuickSort[T](Sort):
    """
    Sorts a list of elements using the quick sort algorithm.
    Quick sort selects a pivot element and partitions the list into elements less than and greater than the pivot,
    then recursively sorts the partitions.

    :param items: The list of elements to be sorted.
    :return: The sorted list of elements.
    """
    def sort(self, items: list[T]) -> list[T]:
        self._quick_sort(items, 0, len(items) - 1)
        return items

    # Method to provide quick sort
    def _quick_sort(self, nums: list[T], left: float, right: float):
        if left < right:
            pivot_index = self._partition(nums, left, right)
            self._quick_sort(nums, left, pivot_index - 1)
            self._quick_sort(nums, pivot_index + 1, right)

    # Method to provide partition
    def _partition(self, items: list[T], left: float, right: float) -> float:
        pivot = items[right]
        i = left - 1

        for j in range(left, right):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]

        items[i + 1], items[right] = items[right], items[i + 1]
        return i + 1

