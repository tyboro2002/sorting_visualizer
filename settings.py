from itemContainer import ItemContainer

animate = True
animations_dir = "animations/"
sorted_dir = "sorted_dir/"
sort_filetype = ".png"
animations_filetype = ".mp4"
add_maze_size_to_name = False
size = 10

# what sorting simulations do we run
running = False
buble_sort = running
insertion_sort = running
radix_sort = running
gnome_sort = running
cocktail_shaker_sort = running
shell_sort = running
selection_sort = running
heap_sort_min = running
heap_sort_max = running
quick_sort = running
merge_sort = running
gravity_sort = running
comb_sort = True

# what shuffling algorithms are used
shufflers = [
    ItemContainer.random_shuffle,
    ItemContainer.reverse,
    ItemContainer.v_shaped,
    ItemContainer.almost_sorted,
    ItemContainer.a_shaped
]
