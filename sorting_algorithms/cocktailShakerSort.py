from matplotlib import pyplot as plt, animation

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
        self.frames = []
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
                if animation:
                    self.add_image(ax2, highlight=(i, i+1))

        if not swapped:
            self.is_sorted = True
            return False

        swapped = False
        self.end -= 1

        for i in range(self.end, self.start, -1):
            if self.items[i] < self.items[i - 1]:
                self.items[i], self.items[i - 1] = self.items[i - 1], self.items[i]
                swapped = True
                if animation:
                    self.add_image(ax2, highlight=(i, i-1))

        self.start += 1

        if not swapped:
            self.is_sorted = True

        return not self.is_sorted

    def sort(self):
        while not self.is_sorted:
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
        while not self.is_sorted:
            self.sort_step(ax2=ax, animation=True)

        # Create the animation
        ani = animation.ArtistAnimation(fig, self.frames, repeat=False, interval=200)
        plt.show()
        return ani
