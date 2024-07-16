from matplotlib import pyplot as plt, animation

from itemContainer import ItemContainer
from sorter import Sorter


class HeapSort(Sorter):
    """
    sort the data using heap sort

    1. Build a Heap:
        a. Start from the last non-leaf node and heapify each node up to the root node.
        b. Heapifying a node means ensuring that the subtree rooted at that node satisfies the heap property.
    2. Heap Sort Process:
        a. Swap the root element with the last element of the heap.
        b. Reduce the heap size by one.
        c. Heapify the new root element to maintain the heap property.
        d. Repeat the process until the heap size is reduced to 1.
    """
    def __init__(self, itemContainer: ItemContainer, shuffle_method, min_heap=True):
        super().__init__(itemContainer, shuffle_method)
        self.frames = []
        self.min_heap = min_heap

    def heapify(self, n, i, ax2=None, animation=False):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if self.min_heap:
            if left < n and self.items[i] > self.items[left]:
                largest = left

            if right < n and self.items[largest] > self.items[right]:
                largest = right
        else:
            if left < n and self.items[i] < self.items[left]:
                largest = left

            if right < n and self.items[largest] < self.items[right]:
                largest = right

        if largest != i:
            self.items[i], self.items[largest] = self.items[largest], self.items[i]
            if animation:
                self.add_image(ax2, highlight=(i, largest))
            self.heapify(n, largest, ax2, animation)

    def sort_step(self, ax2=None, animation=False):
        n = len(self.items)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i, ax2, animation)

        for i in range(n - 1, 0, -1):
            self.items[i], self.items[0] = self.items[0], self.items[i]
            if animation:
                self.add_image(ax2, highlight=(i, 0))
            self.heapify(i, 0, ax2, animation)

    def sort(self):
        self.sort_step()
        if self.min_heap:
            self.items = self.items[::-1]

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
        if self.min_heap:
            self.items = self.items[::-1]
        self.add_image(ax)

        # Create the animation
        ani = animation.ArtistAnimation(fig, self.frames, repeat=False, interval=200)
        return ani
