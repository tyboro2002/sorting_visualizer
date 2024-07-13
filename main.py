from itemContainer import ItemContainer
from sorting_algorithms.bubleSort import BubbleSort

animation_filename = "test_animation.mp4"

if __name__ == "__main__":
    # items = [5, 3, 8, 6, 7, 2, 4, 1]
    item_container = ItemContainer(length=10)
    # print(item_container.get_items())
    item_container.random_shuffle()

    # Create BubbleSort instance
    bubble_sort = BubbleSort(item_container)

    # Visualize the sorting process
    ani = bubble_sort.animate()
    ani.save(animation_filename, writer='ffmpeg')
