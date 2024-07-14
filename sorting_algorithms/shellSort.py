from matplotlib import pyplot as plt, animation

from itemContainer import ItemContainer
from sorter import Sorter


class ShellSort(Sorter):
    """
    sort the data using shell sort

    1. Initialize the Gap Sequence:
        a. Start with a large gap, typically ⌊n/2⌋, where n is the number of elements in the list.
        b. Reduce the gap size in each iteration by a factor (commonly 2).
    2. Gap Sorting:
        a. For each gap h, perform a gapped insertion sort:
            i. Start from the hth element and compare it with the element h positions before it.
            ii. Swap elements if they are in the wrong order.
            iii. Continue comparing and swapping elements h positions apart.
    3. Reduce the Gap:
        a. Reduce the gap size and repeat the gapped insertion sort.
    4. Final Pass:
        a. When the gap is reduced to 1, perform a final insertion sort pass.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)
        self.frames = []

    def sort_step(self, ax2=None, animation=False):
        n = len(self.items)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = self.items[i]
                j = i
                while j >= gap and self.items[j - gap] > temp:
                    self.items[j], self.items[j - gap] = self.items[j - gap], self.items[j]
                    j -= gap
                    if animation:
                        self.add_image(ax2, highlight=(j, j-gap))
                self.items[j] = temp
                if animation:
                    self.add_image(ax2, highlight=(j, j-gap))
            gap //= 2

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
        plt.show()
        return ani
