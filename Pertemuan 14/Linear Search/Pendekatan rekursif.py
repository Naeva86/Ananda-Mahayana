def search(arr, curr_index, key):
    if curr_index == len(arr):
        return -1
    if arr[curr_index] == key:
        return curr_index
    return search(arr, curr_index-1, key)

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 110
print(search(arr,0,x))