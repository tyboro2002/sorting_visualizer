from itemContainer import ItemContainer

animate = True
animations_dir = "animations/"
sorted_dir = "sorted_dir/"
sort_filetype = ".png"
animations_filetype = ".mp4"
add_maze_size_to_name = False
size = 10

# what sorting simulations do we run
buble_sort = False
insertion_sort = False
radix_sort = False
gnome_sort = True

# what shuffling algorithms are used
shufflers = [
    ItemContainer.random_shuffle,
    ItemContainer.reverse,
    ItemContainer.v_shaped,
    ItemContainer.almost_sorted,
    ItemContainer.a_shaped
]
