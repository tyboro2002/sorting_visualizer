from itemContainer import ItemContainer

animate = True
animations_dir = "animations/"
sorted_dir = "sorted_dir/"
sort_filetype = ".png"
animations_filetype = ".mp4"
add_sorting_size_to_name = False
size = 10
FPS = 5  # The fps we save the animations at (advised to use 5 for small ones)

# what sorting simulations do we run
running = False
running2 = False
buble_sort = running
insertion_sort = running
radix_sort = running2
gnome_sort = running
cocktail_shaker_sort = running
shell_sort = running2
selection_sort = running
heap_sort_min = running
heap_sort_max = running
quick_sort = running2
merge_sort = running2
gravity_sort = running
comb_sort = running2
weak_heap_sort_min = running
weak_heap_sort_max = running
binary_quick_sort = running2
pancake_sort = True

# what shuffling algorithms are used
shufflers = [
    ItemContainer.random_shuffle,
    ItemContainer.reverse,
    ItemContainer.v_shaped,
    ItemContainer.almost_sorted,
    ItemContainer.a_shaped
]
