from itemContainer import ItemContainer
from sorter import Sorter


class PancakeSort(Sorter):
    """
    Sort the data using pancake sort.

    1. Find the largest unsorted element.
    2. Flip it to the front.
    3. Flip it to its correct position.
    4. Repeat until sorted.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)

    def flip(self, k):
        self.items[:k + 1] = self.items[:k + 1][::-1]

    def pancake_sort(self, ax2=None, animation=False):
        n = len(self.items)
        for curr_size in range(n, 1, -1):
            # Find the maximum element in the unsorted array
            max_index = self.items.index(max(self.items[:curr_size]))

            if max_index != curr_size - 1:
                # Move the maximum element to the beginning
                if animation:
                    self.add_image(ax2, highlight=(0, max_index), range_highlight=(0, curr_size - 1))
                self.flip(max_index)
                if animation:
                    self.add_image(ax2, highlight=(0, max_index), range_highlight=(0, curr_size - 1))

                # Move the maximum element to its correct position
                self.flip(curr_size - 1)
                if animation:
                    self.add_image(ax2, highlight=(0, curr_size - 1), range_highlight=(0, curr_size - 1))

    def sort(self):
        self.pancake_sort()

    def animate_step(self, ax2=None, animation=False):
        self.pancake_sort(ax2=ax2, animation=animation)
