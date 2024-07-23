from itemContainer import ItemContainer
from sorter import Sorter


class SelectionSort(Sorter):
    """
    sort the data using selection sort

    1. Start with the Full List:
        a. The whole list is initially considered unsorted.
    2. Find the Minimum Element:
        a. Traverse the unsorted portion of the list to find the smallest element.
    3. Swap Elements:
        a. Swap the smallest element found with the first element of the unsorted portion.
    4. Update the Boundary:
        a. Move the boundary between the sorted and unsorted portions to the right by one element.
    5. Repeat:
        a. Repeat the above steps for the new unsorted portion of the list.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)
        self.states = []
        self.is_sorted = False
        self.current_index = 0

    def sort_step(self, ax2=None, animation=False):
        if self.is_sorted:
            return False

        if self.current_index < len(self.items) - 1:
            min_index = self.current_index
            for j in range(self.current_index + 1, len(self.items)):
                self.add_image(ax2, highlight=(j, min_index), animation=animation)
                if self.items[j] < self.items[min_index]:
                    min_index = j

            if min_index != self.current_index:
                self.items[self.current_index], self.items[min_index] = (
                    self.items[min_index], self.items[self.current_index])
                self.states.append((self.items[:], self.current_index, min_index))
                self.add_image(ax2, highlight=(self.current_index, min_index), animation=animation)

            self.current_index += 1
        else:
            self.is_sorted = True

        return not self.is_sorted

    def sort(self):
        while not self.is_sorted:
            self.sort_step()

    def animate_step(self, ax2=None, animation=False):
        while not self.is_sorted:
            self.sort_step(ax2=ax2, animation=animation)
