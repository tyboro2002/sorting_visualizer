from itemContainer import ItemContainer
from sorter import Sorter


class WeakHeapSort(Sorter):
    """
    Sort the data using weak heap sort.

    1. Build a Weak Heap:
        a. Start from the last non-leaf node and weak heapify each node up to the root node.
        b. Weak heapifying a node ensures the weak heap property is satisfied.
    2. Weak Heap Sort Process:
        a. Swap the root element with the last element of the heap.
        b. Reduce the heap size by one.
        c. Weak heapify the new root element to maintain the weak heap property.
        d. Repeat the process until the heap size is reduced to 1.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method, min_heap=True):
        super().__init__(itemContainer, shuffle_method)
        self.min_heap = min_heap
        self.frames = []

    def weak_heapify(self, n, i, ax2=None, animation=False):
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
            self.add_image(ax2, highlight=(i, largest), animation=animation)
            self.weak_heapify(n, largest, ax2, animation)

    def sort_step(self, ax2=None, animation=False):
        n = len(self.items)

        for i in range(n // 2 - 1, -1, -1):
            self.weak_heapify(n, i, ax2, animation)

        for i in range(n - 1, 0, -1):
            self.items[i], self.items[0] = self.items[0], self.items[i]
            self.add_image(ax2, highlight=(i, 0), animation=animation)
            self.weak_heapify(i, 0, ax2, animation)

    def sort(self):
        self.sort_step()
        if self.min_heap:
            self.items = self.items[::-1]

    def animate_step(self, ax2=None, animation=False):
        self.sort_step(ax2=ax2, animation=animation)
        if self.min_heap:
            self.items = self.items[::-1]
        self.add_image(ax2)
