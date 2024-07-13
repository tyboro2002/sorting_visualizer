import random

from matplotlib import pyplot as plt


class ItemContainer:
    def __init__(self, items=None, length=None):
        if items is not None:
            self.items = items
            self.length = len(items)
        if length is not None:
            self.items = [i for i in range(1, length + 1)]
            self.length = length

    def get_items(self):
        return self.items

    def set_items(self, items):
        self.items = items

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def random_shuffle(self):
        random.shuffle(self.items)
        return self

    def reverse(self):
        self.items = self.items[::-1]
        return self

    def __len__(self):
        return self.length

    def save(self, path):
        fig, ax = plt.subplots(figsize=(max(len(self.items) / 5, 10), max(len(self.items) / 5, 10)))
        ax.set_xticks([]), ax.set_yticks([])
        ax.bar(range(len(self.items)), self.items, align="edge")
        plt.savefig(path, bbox_inches='tight')
        plt.close()
