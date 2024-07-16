from itemContainer import ItemContainer
from sorter import Sorter


class BubbleSort(Sorter):
    """
    sort the data using bubble sort

    1. Start at the beginning of the array.
    2. Compare each pair of adjacent elements:
        a. If the elements are in the wrong order (i.e., the first is greater than the second), swap them.
    3. Move to the next pair of elements.
    4. Repeat steps 2 and 3 for the entire array:
        a. After each complete pass through the array, the largest element is moved to its correct position.
        b. The process is repeated for the rest of the array, excluding the last sorted elements.
    5. Continue until no swaps are needed: This indicates that the array is sorted.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)
        self.states = []
        self.current_index = len(self.items) - 1
        self.is_sorted = False

    def sort_step(self, ax2=None, animation=False):

        if self.is_sorted:
            return False

        swapped = False
        for i in range(self.current_index):
            if animation:
                self.add_image(ax2, highlight=(i, i+1))
            if self.items[i] > self.items[i + 1]:
                self.items[i], self.items[i + 1] = self.items[i + 1], self.items[i]
                swapped = True
                self.states.append((self.items, i, i + 1))  # Store items and indices of swapped bars
                if animation:
                    self.add_image(ax2, highlight=(i, i+1))
        if not swapped:
            self.is_sorted = True
        else:
            self.current_index -= 1
        return swapped

    def sort(self):
        while not self.is_sorted:
            self.sort_step()

    def animate_step(self, ax2=None, animation=False):
        while not self.is_sorted:
            self.sort_step(ax2=ax2, animation=animation)

