# Let's provide examples for each of the mentioned list operations in Python.

# Starting with an initial list
initial_list = [1, 2, 3, 4, 5]

# 1 - Append/add operation - O(1)
append_example = initial_list.copy()
append_example.append(6)

# 2 - Delete operations - O(1)
delete_by_index_example = initial_list.copy()
deleted_element = delete_by_index_example.pop()  # Removes the last element

# 3- Deleting by value - O(n)
delete_by_value_example = initial_list.copy()
delete_by_value_example.remove(3)  # Removes the first occurrence of 3

# 4 - Lookup/Access - O(1)
access_example = initial_list[2]  # Accesses the element at index 2

# 5 - Traverse - O(n)
traverse_example = [
    element for element in initial_list
]  # Simple traversal copying elements

# 6 - Merge - O(n + m)
second_list = [6, 7, 8]
merge_example = initial_list + second_list  # Merges initial_list and second_list

# 7 - insert at position operation - O(n)
insert_by_index_example = initial_list.copy()
insert_by_index_example.insert(2, 10)

# 8 - subarray - O(n)
sub_array_example = initial_list.copy()
sub_array_example = sub_array_example[:3]

# 9 - copy - O(n)
sub_array_example = initial_list.copy()
