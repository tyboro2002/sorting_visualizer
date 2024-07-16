from itemContainer import ItemContainer
from sorter import Sorter


class InsertionSort(Sorter):
    """
    sort the data using insertion sort

    1. Initialize: Consider the first element as sorted.
    2. Iterate: Start from the second element (index 1) to the last element.
    3. Pick: Take the current element (let's call it the key).
    4. Compare and Shift:
        a. Compare the key with elements in the sorted portion.
        b. Shift elements of the sorted portion that are greater than the key to one position to the right.
    5. Insert: Place the key in its correct position.
    6. Repeat: Continue the process for all elements.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)
        self.states = []
        self.is_sorted = False
        self.i = 1

    def sort_step(self, ax2=None, animation=False):
        if self.is_sorted:
            return False

        if self.i < len(self.items):
            key = self.items[self.i]
            j = self.i - 1

            while j >= 0 and self.items[j] > key:
                self.items[j + 1], self.items[j] = self.items[j], self.items[j + 1]
                j -= 1
                if animation:
                    self.add_image(ax2, highlight=(j + 1, self.i))

            self.states.append((self.items, j + 1, self.i))

            if animation:
                self.add_image(ax2, highlight=(j + 1, self.i))

            self.i += 1
        else:
            self.is_sorted = True

        return not self.is_sorted

    def sort(self):
        while not self.is_sorted:
            self.sort_step()

    def animate_step(self, ax2=None, animation=False):
        while not self.is_sorted:
            self.sort_step(ax2=ax2, animation=animation)
