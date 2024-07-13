from itemContainer import ItemContainer


class Sorter:
    """
    A super class to bundle the sorter classes.
    """
    def __init__(self, itemContainer: ItemContainer, shuffle_method) -> None:
        itemContainer = shuffle_method(itemContainer)
        self.itemContainer = itemContainer
        self.items = itemContainer.get_items()

    def sort(self):
        raise NotImplementedError("You should implement this method in subclasses.")

    def animate(self):
        raise NotImplementedError("You should implement this method in subclasses.")

    def run(
            self,
            sorted_filename: str,
            animate: bool = True,
            animation_filename: str = "sorting_animation.mp4"
    ) -> None:
        """
        Do a full maze generation run (possibly save the animation of the generation).
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
