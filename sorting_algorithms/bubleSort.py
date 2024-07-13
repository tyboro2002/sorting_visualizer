from matplotlib import pyplot as plt, animation

from itemContainer import ItemContainer


class BubbleSort:
    def __init__(self, itemContainer: ItemContainer):
        self.items = itemContainer.get_items()
        self.states = []
        self.current_index = len(self.items) - 1
        self.is_sorted = False
        self.frames = []

    def sort_step(self, ax2=None, animation=False):

        if self.is_sorted:
            return False

        swapped = False
        for i in range(self.current_index):
            if animation:
                ax2.set_xticks([]), ax2.set_yticks([])
                im2 = ax2.bar(range(len(self.items)), self.items, align="edge", color='skyblue')
                im2[i].set_color('orange')  # Highlight swapped bar 1
                im2[i + 1].set_color('orange')  # Highlight swapped bar 2
                self.frames.append(im2)
            if self.items[i] > self.items[i + 1]:
                self.items[i], self.items[i + 1] = self.items[i + 1], self.items[i]
                swapped = True
                self.states.append((self.items, i, i + 1))  # Store items and indices of swapped bars
                # print(self.states[-1])
                if animation:
                    ax2.set_xticks([]), ax2.set_yticks([])
                    im2 = ax2.bar(range(len(self.items)), self.items, align="edge", color='skyblue')
                    im2[i].set_color('orange')  # Highlight swapped bar 1
                    im2[i+1].set_color('orange')  # Highlight swapped bar 2
                    self.frames.append(im2)
        if not swapped:
            self.is_sorted = True
        else:
            self.current_index -= 1
        return swapped

    def sort(self):
        while not self.is_sorted:
            self.sort_step()

    def animate(self):
        fig, ax = plt.subplots(figsize=(max(len(self.items) / 5, 10), max(len(self.items) / 5, 10)))
        ax.set_xticks([]), ax.set_yticks([])

        # Initial bar plot
        bar_rects = ax.bar(range(len(self.items)), self.items, align="edge", color='skyblue')

        # Generate frames for animation
        self.frames = [bar_rects]
        while not self.is_sorted:
            self.sort_step(ax2=ax, animation=True)
            im = ax.bar(range(len(self.items)), self.items, align="edge")
            im[self.states[-1][1]].set_color('orange')  # Highlight swapped bar 1
            im[self.states[-1][2]].set_color('orange')  # Highlight swapped bar 2
            self.frames.append(im)

        # print(self.frames)
        # print(len(self.frames))
        # Create the animation
        return animation.ArtistAnimation(fig, self.frames, repeat=False, interval=200)

