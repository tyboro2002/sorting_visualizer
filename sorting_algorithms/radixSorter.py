from itemContainer import ItemContainer
from sorter import Sorter


class RadixSort(Sorter):
    """
    sort the data using radix sort

    1. initialize:
        a. Choose the base (radix). For decimal numbers, the base is 10.
        b. Determine the maximum number of digits in the numbers to be sorted.
    2. Digit-wise Sorting:
        a. Start with the least significant digit (rightmost digit).
        b. For each digit position:
            i. Group the numbers into buckets based on the digit at the current position.
            ii. Reassemble the list by collecting numbers from the buckets in order.
        c. Move to the next digit position (to the left).
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)

    def insertion_sort_digit(self, exp, ax2=None, animation=False):
        n = len(self.items)
        for i in range(1, n):
            key = self.items[i]
            j = i - 1
            while j >= 0 and (self.items[j] // exp) % 10 > (key // exp) % 10:
                self.items[j + 1] = self.items[j]
                j -= 1
            self.items[j + 1] = key

            self.add_image(ax2, highlight=(i, j + 1), animation=animation)

    def sort_step(self, ax2=None, animation=False):
        max_item = max(self.items)
        exp = 1
        while max_item // exp > 0:
            self.insertion_sort_digit(exp, ax2, animation)
            exp *= 10

    def sort(self):
        self.sort_step()
