from itemContainer import ItemContainer
from sorter import Sorter


class ShellSort(Sorter):
    """
    sort the data using shell sort

    1. Initialize the Gap Sequence:
        a. Start with a large gap, typically ⌊n/2⌋, where n is the number of elements in the list.
        b. Reduce the gap size in each iteration by a factor (commonly 2).
    2. Gap Sorting:
        a. For each gap h, perform a gapped insertion sort:
            i. Start from the hth element and compare it with the element h positions before it.
            ii. Swap elements if they are in the wrong order.
            iii. Continue comparing and swapping elements h positions apart.
    3. Reduce the Gap:
        a. Reduce the gap size and repeat the gapped insertion sort.
    4. Final Pass:
        a. When the gap is reduced to 1, perform a final insertion sort pass.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)

    def sort_step(self, ax2=None, animation=False):
        n = len(self.items)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = self.items[i]
                j = i
                while j >= gap and self.items[j - gap] > temp:
                    self.items[j], self.items[j - gap] = self.items[j - gap], self.items[j]
                    j -= gap
                    self.add_image(ax2, highlight=(j, j-gap), animation=animation)
                self.items[j] = temp
                self.add_image(ax2, highlight=(j, j-gap), animation=animation)
            gap //= 2

    def sort(self):
        self.sort_step()
