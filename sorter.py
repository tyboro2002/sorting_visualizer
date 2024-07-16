from matplotlib import animation, pyplot as plt

from itemContainer import ItemContainer


class Sorter:
    """
    A super class to bundle the sorter classes.
    """

    def __init__(self, itemContainer: ItemContainer, shuffle_method) -> None:
        if shuffle_method:
            itemContainer = shuffle_method(itemContainer)
        self.itemContainer = itemContainer
        self.items = itemContainer.get_items()
        self.frames = []

    def sort(self):
        raise NotImplementedError("You should implement this method in subclasses.")

    def sort_step(self, ax2=None, animation=False):
        raise NotImplementedError("Subclasses should implement this method.")

    def animate_step(self, ax2=None, animation=False):
        self.sort_step(ax2=ax2, animation=animation)

    def animate(self):
        fig, ax = plt.subplots(figsize=(max(len(self.items) / 5, 10), max(len(self.items) / 5, 10)))
        ax.set_xticks([]), ax.set_yticks([])
        ax.axis('off')  # Remove axes

        # Initial bar plot
        bar_rects = ax.bar(range(len(self.items)), self.items, align="edge", color='skyblue')

        # Generate frames for animation
        self.frames = [bar_rects]
        self.animate_step(ax2=ax, animation=True)

        # Create the animation
        ani = animation.ArtistAnimation(fig, self.frames, repeat=False, interval=200)

        # Close the figure to avoid keeping it open
        plt.close(fig)
        return ani

    def add_image(self, ax, highlight=None, range_highlight=None):
        ax.set_xticks([]), ax.set_yticks([])
        ax.axis('off')  # Remove axes
        im2 = ax.bar(range(len(self.items)), self.items, align="edge", color='skyblue')
        if range_highlight:
            for e in range(range_highlight[0], range_highlight[1] + 1):
                im2[e].set_color('lightgrey')  # Highlight range being sorted
        if highlight:
            for e in highlight:
                im2[e].set_color('orange')  # Highlight swapped bars
        self.frames.append(im2)

    def run(
            self,
            sorted_filename: str,
            animate: bool = True,
            animation_filename: str = "sorting_animation.mp4"
    ) -> None:
        """
        Do a full sorting run (possibly save the animation of the sorting).
        """
        if not animate:
            self.sort()
            self.itemContainer.save(sorted_filename)
        else:
            print("generating animation")
            ani = self.animate()
            print("saving animation")
            ani.save(animation_filename, writer='ffmpeg')
            self.itemContainer.save(sorted_filename)
