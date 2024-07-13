import random


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

    def __len__(self):
        return self.length
