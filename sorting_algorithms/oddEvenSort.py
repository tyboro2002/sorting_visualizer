from itemContainer import ItemContainer
from sorter import Sorter


class OddEvenSort(Sorter):
    """
    Sort the data using odd-even sort (brick sort).

    1. Compare all odd indexed pairs of adjacent elements in the array and swap them if they are in the wrong order.
    2. Compare all even indexed pairs of adjacent elements in the array and swap them if they are in the wrong order.
    3. Repeat steps 1 and 2 until the array is sorted.

    Or in other words:

    1. Odd Phase:
        a. Compare and swap elements at odd indices with their next elements. For example, compare elements at index 1 with index 2, index 3 with index 4, and so on.
    2. Even Phase:
        a. Compare and swap elements at even indices with their next elements. For example, compare elements at index 0 with index 1, index 2 with index 3, and so on.
    3. Repeat:
        a. Repeat the odd and even phases until no more swaps are needed, meaning the array is sorted.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)

    def odd_even_sort(self, ax2=None, animation=False):
        n = len(self.items)
        sorted = False

        while not sorted:
            sorted = True
            # Perform Bubble sort on odd indexed element
            for i in range(1, n - 1, 2):
                self.add_image(ax2, highlight=(i, i + 1), animation=animation)
                if self.items[i] > self.items[i + 1]:
                    self.items[i], self.items[i + 1] = self.items[i + 1], self.items[i]
                    sorted = False
                    self.add_image(ax2, highlight=(i, i + 1), animation=animation)

            # Perform Bubble sort on even indexed element
            for i in range(0, n - 1, 2):
                self.add_image(ax2, highlight=(i, i + 1), animation=animation)
                if self.items[i] > self.items[i + 1]:
                    self.items[i], self.items[i + 1] = self.items[i + 1], self.items[i]
                    sorted = False
                    self.add_image(ax2, highlight=(i, i + 1), animation=animation)

    def sort(self):
        self.odd_even_sort()

    def animate_step(self, ax2=None, animation=False):
        self.odd_even_sort(ax2=ax2, animation=animation)
