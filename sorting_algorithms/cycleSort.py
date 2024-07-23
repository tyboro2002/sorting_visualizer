from matplotlib import animation, pyplot as plt

from itemContainer import ItemContainer
from sorter import Sorter

item = 0

class CycleSort(Sorter):
    """
    Sort the data using cycle sort.

    1. For each cycle in the array:
        a. Find the correct position for the element.
        b. If the element is not already in the correct position, move it to the correct position.
        c. Rotate the rest of the cycle until the cycle is complete.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)

    def cycle_sort(self, ax2=None, animation=False):
        global item
        n = len(self.items)
        for cycle_start in range(0, n - 1):
            item = self.items[cycle_start]

            # Find the position where we put the item
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if self.items[i] < item:
                    pos += 1

            # If the item is already there, continue
            if pos == cycle_start:
                continue

            # Otherwise, put the item to the correct position
            while item == self.items[pos]:
                pos += 1
            if animation:
                self.add_image(ax2, highlight=(cycle_start, pos))
            self.items[pos], item = item, self.items[pos]
            # print(self.items)
            if animation:
                self.add_image(ax2, highlight=(cycle_start, pos))

            # Rotate the rest of the cycle
            while pos != cycle_start:
                pos = cycle_start
                for i in range(cycle_start + 1, n):
                    if self.items[i] < item:
                        pos += 1

                while item == self.items[pos]:
                    pos += 1
                if animation:
                    self.add_image(ax2, highlight=(cycle_start, pos))
                self.items[pos], item = item, self.items[pos]
                # print(self.items)
                if animation:
                    self.add_image(ax2, highlight=(cycle_start, pos))

    def add_image(self, ax, highlight=None, range_highlight=None):
        # print(highlight, range_highlight) # TODO make it look like the bars are swapped
        # if highlight[0] != highlight[1]:
        #     print("nice")
        #     temp = self.items.copy()
        #     self.items[highlight[0]] = item
        ax.set_xticks([]), ax.set_yticks([])
        ax.axis('off')  # Remove axes
        im2 = ax.bar(range(len(self.items)), self.items, align="edge", color='skyblue')
        if range_highlight:

            for e in range(range_highlight[0], range_highlight[1] + 1):
                im2[e].set_color('lightgrey')  # Highlight range being sorted
        if highlight:
            for e in highlight:
                im2[e].set_color('orange')  # Highlight swapped bars
        self.frames.append(im2)
        # if highlight[0] != highlight[1]:
        #     self.items = temp.copy()

    def sort(self):
        self.cycle_sort()

    def animate_step(self, ax2=None, animation=False):
        self.cycle_sort(ax2=ax2, animation=animation)
