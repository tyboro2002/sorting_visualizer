from itemContainer import ItemContainer
from sorter import Sorter


class GravitySort(Sorter):
    """
    Sort the data using gravity (bead) sort.

    1. Setup Beads: Create a grid where each row represents the height of beads falling for each integer.
    2. Drop Beads: Simulate gravity by "dropping" the beads to the bottom of each column.
    3. Collect Results: Collect the results from the bead positions after gravity has sorted them.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)

    def gravity_sort(self, ax2=None, animation=False):
        if not all(isinstance(x, int) and x >= 0 for x in self.items):
            raise ValueError("Gravity Sort can only be applied to non-negative integers.")

        # Count the beads
        max_height = max(self.items)
        counts = [0] * (max_height + 1)

        for num in self.items:
            counts[num] += 1

        self.add_image(ax2, highlight=[], range_highlight=(0, len(self.items) - 1), animation=animation)

        # Simulate gravity from right to left, placing largest items first
        index = len(self.items) - 1
        for height in range(max_height, -1, -1):  # Start from the largest height
            while counts[height] > 0:
                temp_items = self.items[:]
                temp_items[index] = height
                self.add_image(ax2, highlight=[index], range_highlight=(0, len(self.items) - 1), animation=animation)
                self.items[index] = height
                counts[height] -= 1
                index -= 1

                self.add_image(
                    ax2, highlight=[index + 1], range_highlight=(0, len(self.items) - 1), animation=animation
                )

    def sort(self):
        self.gravity_sort()

    def animate_step(self, ax2=None, animation=False):
        self.gravity_sort(ax2=ax2, animation=animation)
