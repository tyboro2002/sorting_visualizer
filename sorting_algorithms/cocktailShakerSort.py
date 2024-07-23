from itemContainer import ItemContainer
from sorter import Sorter


class CocktailShakerSort(Sorter):
    """
    sort the data using cocktailShaker sort

    1. Initialize:
        a. Set start to 0 and end to the length of the list minus 1.
    2. Forward Pass:
        a. Compare each pair of adjacent elements from start to end.
        b. Swap elements if the first is greater than the second.
        c. After reaching the end, decrement end by 1.
    3. Backward Pass:
        a. Compare each pair of adjacent elements from end to start.
        b. Swap elements if the first is greater than the second.
        c. After reaching the start, increment start by 1.
    4. Repeat: Continue the forward and backward passes until start is greater than or equal to end.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)
        self.is_sorted = False
        self.start = 0
        self.end = len(self.items) - 1

    def sort_step(self, ax2=None, animation=False):
        if self.is_sorted:
            return False

        swapped = False

        for i in range(self.start, self.end):
            if self.items[i] > self.items[i + 1]:
                self.items[i], self.items[i + 1] = self.items[i + 1], self.items[i]
                swapped = True
                self.add_image(ax2, highlight=(i, i+1), animation=animation)

        if not swapped:
            self.is_sorted = True
            return False

        swapped = False
        self.end -= 1

        for i in range(self.end, self.start, -1):
            if self.items[i] < self.items[i - 1]:
                self.items[i], self.items[i - 1] = self.items[i - 1], self.items[i]
                swapped = True
                self.add_image(ax2, highlight=(i, i-1), animation=animation)

        self.start += 1

        if not swapped:
            self.is_sorted = True

        return not self.is_sorted

    def sort(self):
        while not self.is_sorted:
            self.sort_step()

    def animate_step(self, ax2=None, animation=False):
        while not self.is_sorted:
            self.sort_step(ax2=ax2, animation=animation)
