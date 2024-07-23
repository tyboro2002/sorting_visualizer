from itemContainer import ItemContainer
from sorter import Sorter


class CircleSort(Sorter):
    """
    Sort the data using circle sort.

    1. Divide the list into pairs of elements.
    2. Compare each pair of elements and swap if necessary.
    3. Recursively apply the same process to each half of the list.
    4. Repeat until the list is sorted.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)

    def circle_sort_rec(self, lo, hi, ax2=None, animation=False):
        if lo == hi:
            return False
        swapped = False
        i, j = lo, hi
        while i < j:
            if animation:
                self.add_image(ax2, highlight=(i, j))
            if self.items[i] > self.items[j]:
                self.items[i], self.items[j] = self.items[j], self.items[i]
                swapped = True
                if animation:
                    self.add_image(ax2, highlight=(i, j))
            i += 1
            j -= 1
        if i == j and self.items[i] > self.items[j + 1]:
            if animation:
                self.add_image(ax2, highlight=(i, j + 1))
            self.items[i], self.items[j + 1] = self.items[j + 1], self.items[i]
            swapped = True
            if animation:
                self.add_image(ax2, highlight=(i, j + 1))
        mid = (hi - lo) // 2
        left_swap = self.circle_sort_rec(lo, lo + mid, ax2, animation)
        right_swap = self.circle_sort_rec(lo + mid + 1, hi, ax2, animation)
        return swapped or left_swap or right_swap

    def circle_sort(self, ax2=None, animation=False):
        while self.circle_sort_rec(0, len(self.items) - 1, ax2, animation):
            pass

    def sort(self):
        self.circle_sort()

    def animate_step(self, ax2=None, animation=False):
        self.circle_sort(ax2=ax2, animation=animation)