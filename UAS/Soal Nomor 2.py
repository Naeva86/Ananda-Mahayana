def insertion_sort(arr, descending=False):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        if descending:
            while j >=0 and key > arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        else:
            while j >= 0 and key < arr [j]:
                arr[j + 1] = arr[j]
        arr[j+1] = key
        
arr = [7, 9, 3, 1, 2, 5]
insertion_sort(arr, descending=True)
print ("Sorted array (Descending Order): ")
for i in range(len(arr)):
    print ("%d" %arr[i])