from itemContainer import ItemContainer
from sorter import Sorter


class MergeSort(Sorter):
    """
    sort the data using merge sort

    1. Split the Array:
        a. Find the middle point of the array to divide it into two halves.
        b. Recursively split each half until the subarrays contain only one element.
    2. Merge the Subarrays:
        a. Merge the two sorted halves into a single sorted array.
        b. During the merge, repeatedly compare the smallest elements of each half and append the smaller element to the
           result array.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)
        self.states = []

    def merge(self, left, mid, right, ax2=None, animation=False):
        n1 = mid - left + 1
        n2 = right - mid

        L = self.items[left:mid + 1]
        R = self.items[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                self.items[k] = L[i]
                i += 1
            else:
                self.items[k] = R[j]
                j += 1
            if animation:
                self.add_image(ax2, highlight=(k,), range_highlight=(left, right))
            k += 1

        while i < n1:
            self.items[k] = L[i]
            i += 1
            if animation:
                self.add_image(ax2, highlight=(k,), range_highlight=(left, right))
            k += 1

        while j < n2:
            self.items[k] = R[j]
            j += 1
            if animation:
                self.add_image(ax2, highlight=(k,), range_highlight=(left, right))
            k += 1

    def merge_sort(self, left, right, ax2=None, animation=False):
        if left < right:
            mid = left + (right - left) // 2
            self.add_image(ax2, range_highlight=(left, mid))
            self.merge_sort(left, mid, ax2, animation)
            self.add_image(ax2, range_highlight=(mid + 1, right))
            self.merge_sort(mid + 1, right, ax2, animation)
            self.merge(left, mid, right, ax2, animation)

    def sort(self):
        self.merge_sort(0, len(self.items) - 1)

    def animate_step(self, ax2=None, animation=False):
        self.merge_sort(0, len(self.items) - 1, ax2=ax2, animation=animation)
