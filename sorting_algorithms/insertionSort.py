from matplotlib import pyplot as plt, animation

from itemContainer import ItemContainer
from sorter import Sorter


class InsertionSort(Sorter):
    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)
        self.states = []
        self.frames = []
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
