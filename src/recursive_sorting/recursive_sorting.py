import math

# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    # Not sure what this is for
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # TO-DO
    newArr = []
    total_counter = 0
    arrA_index = 0
    arrB_index = 0

    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            newArr.append(arrA[arrA_index])
            # merged_arr[total_counter] = arrA[arrA_index]
            arrA_index += 1
            # total_counter += 1
        else:
            newArr.append(arrB[arrB_index])
            # merged_arr[total_counter] = arrB[arrB_index]
            arrB_index += 1
            # total_counter += 1

    newArr += arrA[arrA_index:]
    newArr += arrB[arrB_index:]

    return newArr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    if len(arr) >= 2:
        middle = math.floor(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])

        return merge(left, right)
    else:
        return arr


print(merge_sort([0, 4, 3, 6, 7, 9, 1, 2]))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
