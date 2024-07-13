from matplotlib import pyplot as plt, animation
from itemContainer import ItemContainer
from sorter import Sorter

class RadixSort(Sorter):
    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)
        self.frames = []

    def insertion_sort_digit(self, exp, ax2=None, animation=False):
        n = len(self.items)
        for i in range(1, n):
            key = self.items[i]
            j = i - 1
            while j >= 0 and (self.items[j] // exp) % 10 > (key // exp) % 10:
                self.items[j + 1] = self.items[j]
                j -= 1
            self.items[j + 1] = key

            if animation:
                self.add_image(ax2, highlight=(i, j + 1))

    def sort_step(self, ax2=None, animation=False):
        max_item = max(self.items)
        exp = 1
        while max_item // exp > 0:
            self.insertion_sort_digit(exp, ax2, animation)
            exp *= 10

    def sort(self):
        self.sort_step()

    def add_image(self, ax, highlight=None):
        ax.set_xticks([]), ax.set_yticks([])
        ax.axis('off')  # Remove axes
        im2 = ax.bar(range(len(self.items)), self.items, align="edge", color='skyblue')
        if highlight:
            for e in highlight:
                im2[e].set_color('orange')  # Highlight the current key and position
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
