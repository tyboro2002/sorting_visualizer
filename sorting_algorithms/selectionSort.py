from matplotlib import pyplot as plt, animation

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
        self.frames = []
        self.is_sorted = False
        self.current_index = 0

    def sort_step(self, ax2=None, animation=False):
        if self.is_sorted:
            return False

        if self.current_index < len(self.items) - 1:
            min_index = self.current_index
            for j in range(self.current_index + 1, len(self.items)):
                if animation:
                    self.add_image(ax2, highlight=(j, min_index))
                if self.items[j] < self.items[min_index]:
                    min_index = j

            if min_index != self.current_index:
                self.items[self.current_index], self.items[min_index] = self.items[min_index], self.items[self.current_index]
                self.states.append((self.items[:], self.current_index, min_index))
                if animation:
                    self.add_image(ax2, highlight=(self.current_index, min_index))

            self.current_index += 1
        else:
            self.is_sorted = True

        return not self.is_sorted

    def add_image(self, ax, highlight=None):
        ax.set_xticks([]), ax.set_yticks([])
        ax.axis('off')  # Remove axes
        im2 = ax.bar(range(len(self.items)), self.items, align="edge", color='skyblue')
        if highlight:
            for e in highlight:
                im2[e].set_color('orange')  # Highlight swapped bars
        self.frames.append(im2)

    def sort(self):
        while not self.is_sorted:
            self.sort_step()

    def animate(self):
        fig, ax = plt.subplots(figsize=(max(len(self.items) / 5, 10), max(len(self.items) / 5, 10)))
        ax.set_xticks([]), ax.set_yticks([])
        ax.axis('off')  # Remove axes

        # Initial bar plot
        bar_rects = ax.bar(range(len(self.items)), self.items, align="edge", color='skyblue')

        # Generate frames for animation
        self.frames = [bar_rects]
        while not self.is_sorted:
            self.sort_step(ax2=ax, animation=True)

        # Create the animation
        ani = animation.ArtistAnimation(fig, self.frames, repeat=False, interval=200)
        return ani
