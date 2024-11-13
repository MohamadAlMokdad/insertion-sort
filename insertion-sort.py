# Insertion Sort function definition
def insertion_sort(arr):
    # Traverse from the second element to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key after the last element smaller than it
        arr[j + 1] = key

    return arr

# Sample array
arr = [12, 11, 13, 5, 6]

# Sorting the array
sorted_arr = insertion_sort(arr)

# Displaying the sorted array
print("Sorted array using Insertion Sort:", sorted_arr)
