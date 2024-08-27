#Set Functions and Methods

# Set Creation
my_set = {1, 2, 3}
another_set = set([3, 4, 5])

# Set Methods
my_set.add(4)
my_set.update([5, 6])
my_set.remove(3)  # Raises KeyError if element is not found
my_set.discard(2)  # Does not raise an error if element is not found
removed_element = my_set.pop()  # Removes an arbitrary element
my_set.clear()  # Removes all elements

# Set Operations
union_set = my_set.union(another_set)
intersection_set = my_set.intersection(another_set)
difference_set = my_set.difference(another_set)
symmetric_difference_set = my_set.symmetric_difference(another_set)

# Set Comparisons
is_subset = my_set.issubset(another_set)
is_superset = my_set.issuperset(another_set)
is_disjoint = my_set.isdisjoint(another_set)

# Built-in Functions for Sets
set_length = len(my_set)
element_exists = 4 in my_set

# Print results
print(f"Updated Set: {my_set}")
print(f"Removed Element: {removed_element}")
print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference: {difference_set}")
print(f"Symmetric Difference: {symmetric_difference_set}")
print(f"Is Subset: {is_subset}")
print(f"Is Superset: {is_superset}")
print(f"Is Disjoint: {is_disjoint}")
print(f"Set Length: {set_length}")
print(f"Element Exists (4): {element_exists}")
#2. List Functions and Methods

# List Creation
my_list = [1, 2, 3]
another_list = [4, 5, 6]

# List Methods
my_list.append(4)
my_list.extend([5, 6])
my_list.insert(2, 7)
my_list.remove(2)  # Removes the first occurrence of 2
popped_element = my_list.pop()  # Removes and returns the last element
my_list.pop(0)  # Removes and returns the element at index 0
index_of_3 = my_list.index(3)  # Returns the index of the first occurrence of 3
count_of_4 = my_list.count(4)  # Returns the number of occurrences of 4
my_list.sort()  # Sorts the list in place
my_list.reverse()  # Reverses the list in place
my_list_copy = my_list.copy()  # Returns a shallow copy of the list
my_list.clear()  # Removes all elements

# Built-in Functions for Lists
list_length = len(another_list)
element_exists = 4 in another_list

# Print results
print(f"Updated List: {my_list}")
print(f"Popped Element: {popped_element}")
print(f"Index of 3: {index_of_3}")
print(f"Count of 4: {count_of_4}")
print(f"List Copy: {my_list_copy}")
print(f"List Length: {list_length}")
print(f"Element Exists (4): {element_exists}")
#3. Tuple Functions and Methods

# Tuple Creation
my_tuple = (1, 2, 3, 4, 5)
another_tuple = tuple([6, 7, 8])

# Tuple Methods
index_of_3 = my_tuple.index(3)  # Returns the index of the first occurrence of 3
count_of_4 = my_tuple.count(4)  # Returns the number of occurrences of 4

# Tuple Operations
concatenated_tuple = my_tuple + another_tuple  # Concatenation
repeated_tuple = my_tuple * 2  # Repeating a tuple
element_at_index_2 = my_tuple[2]  # Accessing elements by index
sliced_tuple = my_tuple[1:4]  # Slicing a tuple

# Built-in Functions for Tuples
tuple_length = len(my_tuple)
element_exists = 4 in my_tuple

# Print results
print(f"Original Tuple: {my_tuple}")
print(f"Index of 3: {index_of_3}")
print(f"Count of 4: {count_of_4}")
print(f"Concatenated Tuple: {concatenated_tuple}")
print(f"Repeated Tuple: {repeated_tuple}")
print(f"Element at Index 2: {element_at_index_2}")
print(f"Sliced Tuple: {sliced_tuple}")
print(f"Tuple Length: {tuple_length}")
print(f"Element Exists (4): {element_exists}")