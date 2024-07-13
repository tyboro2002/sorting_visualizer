from itemContainer import ItemContainer
from settings import sorted_dir, add_maze_size_to_name, animate, animations_dir, sort_filetype, animations_filetype
from sorting_algorithms.bubleSort import BubbleSort
from sorting_algorithms.insertionSort import InsertionSort
from sorting_algorithms.radixSorter import RadixSort

# TODO Selection Sort
# TODO Merge Sort
# TODO Quick Sort
# TODO Heap Sort
# TODO Counting Sort
# TODO Radix Sort (busy with this one)
# TODO Shell Sort
# TODO Cocktail Shaker Sort
# TODO Gnome Sort

if __name__ == "__main__":
    item_container = ItemContainer(length=999).random_shuffle()

    shufflers = [ItemContainer.random_shuffle, ItemContainer.reverse]
    for shuffler in shufflers:
        # print("starting bubble sort for " + shuffler.__name__)
        # BubbleSort(
        #     item_container,
        #     shuffler
        # ).run(
        #     sorted_filename=sorted_dir + "BubleSort_" + shuffler.__name__ +
        #     (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
        #     animate=animate,
        #     animation_filename=animations_dir + 'BubleSort_' + shuffler.__name__ + "_animation" +
        #     (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
        # )
        # print("done bubble sort for " + shuffler.__name__)
        #
        # print("starting insertion sort for " + shuffler.__name__)
        # InsertionSort(
        #     item_container,
        #     shuffler
        # ).run(
        #     sorted_filename=sorted_dir + "InsertionSort_" + shuffler.__name__ +
        #     (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
        #     animate=animate,
        #     animation_filename=animations_dir + 'InsertionSort_' + shuffler.__name__ + "_animation" +
        #     (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
        # )
        # print("done insertion sort for " + shuffler.__name__)

        print("starting radix sort for " + shuffler.__name__)
        RadixSort(
            item_container,
            shuffler
        ).run(
            sorted_filename=sorted_dir + "RadixSort_" + shuffler.__name__ +
            (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
            animate=animate,
            animation_filename=animations_dir + 'RadixSort_' + shuffler.__name__ + "_animation" +
            (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
        )
        print("done radix sort for " + shuffler.__name__)
