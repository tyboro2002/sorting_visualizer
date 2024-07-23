from itemContainer import ItemContainer
from sorter import Sorter


class QuickSort(Sorter):
    """
    sort the data using quick sort

    1. Select a Pivot:
        a. Choose a pivot element from the array.
    2. Partitioning:
        a. Rearrange the elements in the array such that elements less than the pivot are on the left, elements greater
           than the pivot are on the right, and the pivot is in its final position.
    3. Recursively Apply Quick Sort:
        a. Recursively apply the quick sort to the sub-array of elements with smaller values and the sub-array of
           elements with greater values.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)
        self.states = []

    def median_of_three(self, low, mid, high):
        a = self.items[low]
        b = self.items[mid]
        c = self.items[high]
        if (a - b) * (c - a) >= 0:
            return low
        elif (b - a) * (c - b) >= 0:
            return mid
        else:
            return high

    def partition(self, low, high, ax2=None, animation=False):
        mid = (low + high) // 2
        median_index = self.median_of_three(low, mid, high)
        # Add image to highlight the median selection
        self.add_image(ax2, highlight=(low, mid, high), range_highlight=(low, high), animation=animation)
        self.items[median_index], self.items[high] = self.items[high], self.items[median_index]
        # Add image to highlight the median selection
        self.add_image(ax2, highlight=(low, mid, high), range_highlight=(low, high), animation=animation)
        pivot = self.items[high]
        i = low - 1

        for j in range(low, high):
            if self.items[j] < pivot:
                i += 1
                self.items[i], self.items[j] = self.items[j], self.items[i]
                self.add_image(ax2, highlight=(i, j), range_highlight=(low, high), animation=animation)

        self.items[i + 1], self.items[high] = self.items[high], self.items[i + 1]
        self.add_image(ax2, highlight=(i + 1, high), range_highlight=(low, high), animation=animation)
        return i + 1

    def quick_sort(self, low, high, ax2=None, animation=False):
        if low < high:
            pi = self.partition(low, high, ax2, animation)
            self.quick_sort(low, pi - 1, ax2, animation)
            self.quick_sort(pi + 1, high, ax2, animation)

    def sort(self):
        self.quick_sort(0, len(self.items) - 1)

    def animate_step(self, ax2=None, animation=False):
        self.quick_sort(0, len(self.items) - 1, ax2=ax2, animation=animation)
