numlist = [5, 10, 4, 2, 36, 2, 3, 18, 15, 22]

def bubbleSort(array):

    for i in range(len(array)):
        swapped = False
        for j in range(len(array)-i-1):

            element = array[j]
            neighbour = array[j+1]

            if element > neighbour:
                array[j+1] = element
                array[j] = neighbour
                swapped = True

        if not swapped:
            break

    return array

# bubbleSort(numlist)

def merge(left, right):
    """Recursively sorts a list using the merge sort algorithm."""
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


def mergeSort(array):

    if len(array) <=1:
        return array

    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    return merge(left, right)

# mergeSort(numlist)

numlist = [5, 10, 4, 2, 36, 2, 3, 18, 15, 22]


def selectionSort(array):
    for s in range(len(array)):
        min_idx = s

        for i in range(s + 1, len(array)):

            # For sorting in descending order
            # for minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # Arranging min at the correct position
        (array[s], array[min_idx]) = (array[min_idx], array[s])


# selectionSort(numlist)

def insertionSort(array):

    # Outer loop to traverse on len(array)
    for i in range(1, len(array)):

        a = array[i]

        # Move elements of array[0 to i-1],
        # which are greater to one position
        # ahead of their current position
        j = i - 1

        while j >= 0 and a < array[j]:
            # temp = array[j]
            # temp2 = array[j+1]
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = a

    return array

insertionSort(numlist)


def timsort(array, MIN_RUN):
    """Timsort algorithm implementation using insertion sort and merge sort."""
    n = len(array)

    # Sort individual subarrays of size MIN_RUN or smaller using insertion sort
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        array = insertionSort(array)

    # Merge sorted runs
    size = MIN_RUN
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min(n - 1, left + 2 * size - 1)
            if mid < right:
                left_part = array[left:mid + 1]
                right_part = array[mid + 1:right + 1]
                array[left:right + 1] = merge(left_part, right_part)
        size *= 2

    return array

numlist = [34, 7, 23, 32, 5, 62, 32, 2, 15, 5, 10, 4, 2, 36, 2, 3, 18, 15, 22]
timsort(numlist, 32)


numlist = [34, 7, 23, 11, 5, 62, 32, 18, 15, 22]
# Quicksort algorithm
def quicksort(array, low, high):
    if low < high:
        pv = partition(array, low, high)

        # Left of Pivot
        array = quicksort(array, low, pv - 1)

        # Right of Pivot
        array = quicksort(array, pv + 1, high)

    return array

# Divide and Conquer algorithm
def partition(array, low, high):
    # Rightmost element
    pivot = array[high]

    # Second pointer
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1 # j moves to the right while i stays the same if array[j] > pivot
            array[i], array[j] = array[j], array[i]
    # swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1 # this is where the partition is done

quicksort(numlist, 0, len(numlist)-1)



numlist = [34, 7, 23, 11, 5, 62, 32, 18, 15, 22]
def partition(array, start, end):

    pivot_index = start
    pivot = array[pivot_index]

    # start = pivot_index + 1
    # end = len(array) - 1

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if start < end:
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = pivot, array[end]

    return end

def quickSort(array, start, end):
    if start < end:
        pv = partition(array, start, end)

        # Left of Pivot
        array = quickSort(array, start, pv - 1)

        # Right of Pivot
        array = quickSort(array, pv + 1, end)

    return array

quickSort(numlist, 0, len(numlist)-1)


# Python program for implementation of heap Sort

# To heapify a subtree rooted with node i
# which is an index in arr[].
def heapify(arr, n, i):
    # Initialize largest as root
    largest = i

    # i is parent node
    # left child = 2 * parent + 1
    l = 2 * i + 1 #
    r = l + 1 # right child = 1 + left child

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)


# Main function to do heap sort
def heapSort(arr):
    n = len(arr)

    # Build heap (rearrange array), moving bigger numbers to parent node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):
        # Move root to end, i.e. largest item on the top to the bottom last leaf
        arr[0], arr[i] = arr[i], arr[0]
        # if i == n - 4:
        #     return arr[-3:]
        # Call max heapify on the reduced heap rearranging from the right side
        # heapify on the unsorted array, right is sorted
        heapify(arr, i, 0)

array = [34, 7, 23, 11, 5, 62, 32, 18, 15, 22]

heapSort(array)

# Example usage



