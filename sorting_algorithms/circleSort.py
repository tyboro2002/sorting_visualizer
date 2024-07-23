from itemContainer import ItemContainer
from sorter import Sorter


class CircleSort(Sorter):
    """
    Sort the data using circle sort.

    1. Divide the Array:
        a. The array is divided into two halves, which are not necessarily contiguous. The first half contains elements
        from the start to the middle of the array, and the second half contains elements from the end to the middle of
        the array.
    2. Compare and Swap:
        a. Compare elements in pairs from the two halves. For example, compare the first element of the first half with
        the last element of the second half, the second element of the first half with the second last element of the
        second half, and so on.
        b. If the first element is greater than the second element in any pair, they are swapped.
    3. Recursive Call:
        a. Recursively apply the same process to the two halves.
    4. Conquer Phase:
        a. After completing the comparisons and swaps for all elements, the array should be more sorted than before.
        b. Repeat the entire process until no more swaps are needed.
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