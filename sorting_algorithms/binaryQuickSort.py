from itemContainer import ItemContainer
from sorter import Sorter


class BinaryQuickSort(Sorter):
    """
    Sort the data using binary quick sort.

    1. Start with the most significant bit (MSB).
    2. Partition the data into two groups based on the current bit.
    3. Recursively sort each partition.
    4. Move to the next significant bit.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)

    def binary_quick_sort(self, low, high, bit, ax2=None, animation=False):
        if low >= high or bit < 0:
            return

        left = low
        right = high

        while left <= right:
            while left <= right and not (self.items[left] >> bit) & 1:
                self.add_image(ax2, highlight=(left, right), range_highlight=(low, high), animation=animation)
                left += 1
            while left <= right and (self.items[right] >> bit) & 1:
                self.add_image(ax2, highlight=(left, right), range_highlight=(low, high), animation=animation)
                right -= 1
            if left < right:
                self.add_image(ax2, highlight=(left, right), range_highlight=(low, high), animation=animation)
                self.items[left], self.items[right] = self.items[right], self.items[left]
                self.add_image(ax2, highlight=(left, right), range_highlight=(low, high), animation=animation)
                left += 1
                right -= 1

        self.add_image(ax2, highlight=None, range_highlight=(low, high), animation=animation)

        self.binary_quick_sort(low, right, bit - 1, ax2, animation)
        self.binary_quick_sort(left, high, bit - 1, ax2, animation)

    def sort(self):
        max_bit = max(self.items).bit_length() - 1
        self.binary_quick_sort(0, len(self.items) - 1, max_bit)

    def animate_step(self, ax2=None, animation=False):
        max_bit = max(self.items).bit_length() - 1
        self.binary_quick_sort(0, len(self.items) - 1, max_bit, ax2, animation)
