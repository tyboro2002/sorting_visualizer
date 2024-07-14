from itemContainer import ItemContainer
from settings import sorted_dir, add_maze_size_to_name, animate, animations_dir, sort_filetype, animations_filetype, \
    size, buble_sort, radix_sort, insertion_sort, shufflers, gnome_sort, cocktail_shaker_sort, shell_sort
from sorting_algorithms.bubleSort import BubbleSort
from sorting_algorithms.cocktailShakerSort import CocktailShakerSort
from sorting_algorithms.gnomeSort import GnomeSort
from sorting_algorithms.insertionSort import InsertionSort
from sorting_algorithms.radixSorter import RadixSort
from sorting_algorithms.shellSort import ShellSort

# TODO Selection Sort
# TODO Merge Sort
# TODO Quick Sort
# TODO Heap Sort
# TODO Counting Sort

if __name__ == "__main__":
    item_container = ItemContainer(length=size)

    for shuffler in shufflers:
        if buble_sort:
            print("starting bubble sort for " + shuffler.__name__)
            BubbleSort(
                item_container,
                shuffler
            ).run(
                sorted_filename=sorted_dir + "BubleSort/BubleSort_" + shuffler.__name__ +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
                animate=animate,
                animation_filename=animations_dir + 'BubleSort/BubleSort_' + shuffler.__name__ + "_animation" +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
            )
            print("done bubble sort for " + shuffler.__name__)

        if insertion_sort:
            print("starting insertion sort for " + shuffler.__name__)
            InsertionSort(
                item_container,
                shuffler
            ).run(
                sorted_filename=sorted_dir + "InsertionSort/InsertionSort_" + shuffler.__name__ +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
                animate=animate,
                animation_filename=animations_dir + 'InsertionSort/InsertionSort_' + shuffler.__name__ + "_animation" +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
            )
            print("done insertion sort for " + shuffler.__name__)

        if radix_sort:
            print("starting radix sort for " + shuffler.__name__)
            RadixSort(
                item_container,
                shuffler
            ).run(
                sorted_filename=sorted_dir + "RadixSort/RadixSort_" + shuffler.__name__ +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
                animate=animate,
                animation_filename=animations_dir + 'RadixSort/RadixSort_' + shuffler.__name__ + "_animation" +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
            )
            print("done radix sort for " + shuffler.__name__)

        if gnome_sort:
            print("starting gnome sort for " + shuffler.__name__)
            GnomeSort(
                item_container,
                shuffler
            ).run(
                sorted_filename=sorted_dir + "GnomeSort/GnomeSort_" + shuffler.__name__ +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
                animate=animate,
                animation_filename=animations_dir + 'GnomeSort/GnomeSort_' + shuffler.__name__ + "_animation" +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
            )
            print("done gnome sort for " + shuffler.__name__)

        if cocktail_shaker_sort:
            print("starting cocktail shaker sort for " + shuffler.__name__)
            CocktailShakerSort(
                item_container,
                shuffler
            ).run(
                sorted_filename=sorted_dir + "CocktailShakerSort/CocktailShakerSort_" + shuffler.__name__ +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
                animate=animate,
                animation_filename=animations_dir + 'CocktailShakerSort/CocktailShakerSort_' + shuffler.__name__ + "_animation" +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
            )
            print("done cocktail shaker sort for " + shuffler.__name__)

        if shell_sort:
            print("starting shell sort for " + shuffler.__name__)
            ShellSort(
                item_container,
                shuffler
            ).run(
                sorted_filename=sorted_dir + "ShellSort/ShellSort_" + shuffler.__name__ +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
                animate=animate,
                animation_filename=animations_dir + 'ShellSort/ShellSort_' + shuffler.__name__ + "_animation" +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
            )
            print("done shell sort for " + shuffler.__name__)
