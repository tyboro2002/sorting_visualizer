from matplotlib import pyplot as plt, animation

from itemContainer import ItemContainer
from sorter import Sorter


class GnomeSort(Sorter):
    """
    sort the data using gnome sort

    1. Initialize: Set the initial position to 0 (the start of the array).
    2. Move Forward: If the current position is 0 or the element at the current position is greater than or equal to the element at the previous position, move one step forward.
    3. Swap and Move Back: If the current position is greater than 0 and the element at the current position is less than the element at the previous position, swap the two elements and move one step back.
    4. Repeat: Repeat steps 2 and 3 until the end of the array is reached.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)
        self.frames = []

    def sort_step(self, ax2=None, animation=False):
        index = 0
        while index < len(self.items):
            if index == 0:
                index += 1
            if self.items[index] >= self.items[index - 1]:
                index += 1
            else:
                self.items[index], self.items[index - 1] = self.items[index - 1], self.items[index]
                if animation:
                    self.add_image(ax2, highlight=(index, index-1))
                index -= 1

    def sort(self):
        self.sort_step()

    def add_image(self, ax, highlight=None):
        ax.set_xticks([]), ax.set_yticks([])
        ax.axis('off')  # Remove axes
        im2 = ax.bar(range(len(self.items)), self.items, align="edge", color='skyblue')
        if highlight:
            for e in highlight:
                im2[e].set_color('orange')  # Highlight swapped bars
        self.frames.append(im2)

    def animate(self):
        fig, ax = plt.subplots(figsize=(max(len(self.items) / 5, 10), max(len(self.items) / 5, 10)))
        ax.set_xticks([]), ax.set_yticks([])
        ax.axis('off')  # Remove axes

        # Initial bar plot
        bar_rects = ax.bar(range(len(self.items)), self.items, align="edge", color='skyblue')

        # Generate frames for animation
        self.frames = [bar_rects]
        self.sort_step(ax2=ax, animation=True)

        # Create the animation
        ani = animation.ArtistAnimation(fig, self.frames, repeat=False, interval=200)
        return ani
