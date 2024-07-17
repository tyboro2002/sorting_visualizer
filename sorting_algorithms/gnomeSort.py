from itemContainer import ItemContainer
from sorter import Sorter


class GnomeSort(Sorter):
    """
    sort the data using gnome sort

    1. Initialize: Set the initial position to 0 (the start of the array).
    2. Move Forward: If the current position is 0 or the element at the current position is greater than or equal to the
       element at the previous position, move one step forward.
    3. Swap and Move Back: If the current position is greater than 0 and the element at the current position is less
       than the element at the previous position, swap the two elements and move one step back.
    4. Repeat: Repeat steps 2 and 3 until the end of the array is reached.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)

    def sort_step(self, ax2=None, animation=False):
        index = 0
        while index < len(self.items):
            if index == 0:
                index += 1
            if self.items[index] >= self.items[index - 1]:
                if animation:
                    self.add_image(ax2, highlight=(index, index - 1))
                index += 1
            else:
                self.items[index], self.items[index - 1] = self.items[index - 1], self.items[index]
                if animation:
                    self.add_image(ax2, highlight=(index, index - 1))
                index -= 1

    def sort(self):
        self.sort_step()
