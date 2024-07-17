from itemContainer import ItemContainer
from settings import sorted_dir, add_maze_size_to_name, animate, animations_dir, sort_filetype, animations_filetype, \
    size, buble_sort, radix_sort, insertion_sort, shufflers, gnome_sort, cocktail_shaker_sort, shell_sort, \
    selection_sort, heap_sort_max, heap_sort_min, quick_sort, merge_sort, gravity_sort, comb_sort
from sorting_algorithms.bubleSort import BubbleSort
from sorting_algorithms.cocktailShakerSort import CocktailShakerSort
from sorting_algorithms.combSort import CombSort
from sorting_algorithms.gnomeSort import GnomeSort
from sorting_algorithms.gravitySort import GravitySort
from sorting_algorithms.heapSort import HeapSort
from sorting_algorithms.insertionSort import InsertionSort
from sorting_algorithms.mergeSort import MergeSort
from sorting_algorithms.quickSort import QuickSort
from sorting_algorithms.radixSorter import RadixSort
from sorting_algorithms.selectionSort import SelectionSort
from sorting_algorithms.shellSort import ShellSort

# Variations of algorithms
# TODO (double) Selection Sort
# TODO Binary Insertion Sort
# TODO Weak Heap Sort
# TODO Ternary Heap Sort
# TODO Binary Quick Short
# TODO American Flag Sort
# TODO Spread Sort
# TODO Sample Sort
# TODO Proxmap Sort

# Normal Algorithms
# TODO Pancake Sort
# TODO Cycle Sort
# TODO Exchange Sort (looking forward or looking backward)
# TODO Odd Even Sort
# TODO Circle Sort
# TODO Baiai Sort (TODO search explanation for this algorithm)
# TODO Patience Sort
# TODO Strand Sort
# TODO Bitonic Sort
# TODO Odd Even Network Sort
# TODO Pairwise Network Sort
# TODO Quick LL sort
# TODO Quick Dual Pivot Sort
# TODO Proportion Extend Sort (with 1/16 sorted to find median)
# TODO Intro Sort
# TODO Pattern Defeating Quick Sort
# TODO Tim Sort
# TODO Iterative Merge Sort
# TODO Smooth Sort
# TODO Poplar Sort
# TODO Cartesian Tree Sort
# TODO Sqrt Sort
# TODO Block Sort
# TODO Wiki Sort
# TODO Grail Sort

# Merge sort variations
# TODO In Place Merge Sort
# TODO Weave Sort
# TODO Rotate Merge Sort
# TODO Quad Sort

# Fast Algorithms
# TODO Merge Sort (in the workings)
# TODO Counting Sort
# TODO Bucket Sort
# TODO Tournament Sort
# TODO Tree Sort

# Joke Algorithms
# TODO Bogo Sort
# TODO Bogo Bogo Sort
# TODO Stooge Sort
# TODO Slow Sort
# TODO (Quantum Bogo Sort)
# TODO Stalin Sort
# TODO Sleep Sort
# TODO Miracle Sort
# TODO Power Sort

# String Sort Algorithms
# TODO Burst Sort

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
                animation_filename=animations_dir + 'CocktailShakerSort/CocktailShakerSort_' + shuffler.__name__ +
                "_animation" +
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

        if selection_sort:
            print("starting selection sort for " + shuffler.__name__)
            SelectionSort(
                item_container,
                shuffler
            ).run(
                sorted_filename=sorted_dir + "SelectionSort/SelectionSort_" + shuffler.__name__ +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
                animate=animate,
                animation_filename=animations_dir + 'SelectionSort/SelectionSort_' + shuffler.__name__ + "_animation" +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
            )
            print("done selection sort for " + shuffler.__name__)

        if heap_sort_min:
            print("starting heap sort min for " + shuffler.__name__)
            HeapSort(
                item_container,
                shuffler,
                min_heap=True
            ).run(
                sorted_filename=sorted_dir + "HeapSort_min/HeapSort_min_" + shuffler.__name__ +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
                animate=animate,
                animation_filename=animations_dir + 'HeapSort_min/HeapSort_min_' + shuffler.__name__ + "_animation" +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
            )
            print("done heap sort min for " + shuffler.__name__)

        if heap_sort_max:
            print("starting heap sort max for " + shuffler.__name__)
            HeapSort(
                item_container,
                shuffler,
                min_heap=False
            ).run(
                sorted_filename=sorted_dir + "HeapSort_max/HeapSort_max_" + shuffler.__name__ +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
                animate=animate,
                animation_filename=animations_dir + 'HeapSort_max/HeapSort_max_' + shuffler.__name__ + "_animation" +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
            )
            print("done heap sort max for " + shuffler.__name__)

        if quick_sort:
            print("starting quick sort for " + shuffler.__name__)
            QuickSort(
                item_container,
                shuffler
            ).run(
                sorted_filename=sorted_dir + "QuickSort/QuickSort_" + shuffler.__name__ +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
                animate=animate,
                animation_filename=animations_dir + 'QuickSort/QuickSort_' + shuffler.__name__ + "_animation" +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
            )
            print("done quick sort for " + shuffler.__name__)

        if merge_sort:
            print("starting merge sort for " + shuffler.__name__)
            MergeSort(
                item_container,
                shuffler
            ).run(
                sorted_filename=sorted_dir + "MergeSort/MergeSort_" + shuffler.__name__ +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
                animate=animate,
                animation_filename=animations_dir + 'MergeSort/MergeSort_' + shuffler.__name__ + "_animation" +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
            )
            print("done merge sort for " + shuffler.__name__)

        if gravity_sort:
            print("starting gravity sort for " + shuffler.__name__)
            GravitySort(
                item_container,
                shuffler
            ).run(
                sorted_filename=sorted_dir + "GravitySort/GravitySort_" + shuffler.__name__ +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
                animate=animate,
                animation_filename=animations_dir + 'GravitySort/GravitySort_' + shuffler.__name__ + "_animation" +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
            )
            print("done gravity sort for " + shuffler.__name__)

        if comb_sort:
            print("starting comb sort for " + shuffler.__name__)
            CombSort(
                item_container,
                shuffler
            ).run(
                sorted_filename=sorted_dir + "CombSort/CombSort_" + shuffler.__name__ +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + sort_filetype,
                animate=animate,
                animation_filename=animations_dir + 'CombSort/CombSort_' + shuffler.__name__ + "_animation" +
                (f"_{len(item_container)}" if add_maze_size_to_name else "") + animations_filetype
            )
            print("done comb sort for " + shuffler.__name__)
