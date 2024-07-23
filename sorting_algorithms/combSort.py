from itemContainer import ItemContainer
from sorter import Sorter
from matplotlib import pyplot as plt, animation
import math

class CombSort(Sorter):
    """
    Sort the data using comb sort

    1. Initialize the gap size to the length of the list.
    2. Shrink the gap by a shrink factor in each iteration.
    3. Compare and swap elements with the gap distance.
    4. Continue until the gap is 1 and no swaps are needed.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)

    def comb_sort(self, ax2=None, animation=False):
        gap = len(self.items)
        shrink_factor = 1.3
        sorted = False

        while not sorted:
            gap = int(gap / shrink_factor)
            if gap <= 1:
                gap = 1
                sorted = True

            i = 0
            while i + gap < len(self.items):
                self.add_image(ax2, highlight=(i, i + gap), animation=animation)
                if self.items[i] > self.items[i + gap]:
                    self.items[i], self.items[i + gap] = self.items[i + gap], self.items[i]
                    sorted = False
                    self.add_image(ax2, highlight=(i, i + gap), animation=animation)
                i += 1

            self.add_image(ax2, highlight=None, animation=animation)

    def sort(self):
        self.comb_sort()

    def animate_step(self, ax2=None, animation=False):
        self.comb_sort(ax2=ax2, animation=animation)
