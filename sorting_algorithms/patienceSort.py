import heapq

from itemContainer import ItemContainer
from sorter import Sorter
from bisect import bisect_left


class PatienceSort(Sorter):
    """
    Sort the data using patience sort.

    1. Create piles where each pile has elements in non-decreasing order.
    2. Merge the piles to create a sorted array.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method):
        super().__init__(itemContainer, shuffle_method)

    def patience_sort(self, ax2=None, animation=False):
        # Step 1: Create piles
        piles = []
        for item in self.items:
            pos = bisect_left([pile[-1] for pile in piles], item)
            if pos != len(piles):
                piles[pos].append(item)
            else:
                piles.append([item])
            if animation:
                self.add_image(ax2, highlight=[pos])

        # Intermediate step: Show all piles formed
        if animation:
            self.items = [item for pile in piles for item in pile]
            for i, pile in enumerate(piles):
                self.add_image(ax2, highlight=list(
                    range(sum(len(p) for p in piles[:i]), sum(len(p) for p in piles[:i + 1]))))

        # Step 2: Collect piles to create a sorted array using a min-heap
        heap = []
        for pile in piles:
            heapq.heappush(heap, (pile.pop(), pile))

        sorted_items = []
        while heap:
            smallest, pile = heapq.heappop(heap)
            sorted_items.append(smallest)
            if pile:
                heapq.heappush(heap, (pile.pop(), pile))
            if animation:
                self.items = sorted_items + [item for p in piles for item in p[::-1]]
                self.add_image(ax2)

        self.items = sorted_items
        if animation:
            self.add_image(ax2)

    def sort(self):
        self.patience_sort()

    def animate_step(self, ax2=None, animation=False):
        self.patience_sort(ax2=ax2, animation=animation)
