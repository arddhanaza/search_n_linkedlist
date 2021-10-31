# Quick Sort
data = [6, 3, 4, 5, 7, 0, 2, 8, 9, 1]


def partition(start, end, data):
    pivot_index = start
    pivot = data[pivot_index]

    while start < end:
        while start < len(data) and data[start] <= pivot:
            start += 1

        while data[end] > pivot:
            end -= 1

        if (start< end):
            temp = data[start]
            data[start] = data[end]
            data[end] = temp

    temp = data[end]
    data[end] = data[pivot_index]
    data[pivot_index] = temp

    return end

def quickSort(start, end, data):
    if (start < end):

        partition_index = partition(start, end, data)

        quickSort(start, partition_index -1, data)
        quickSort(partition_index +1, end, data)


def cetak(data):
    print("Data Asal -->")
    print(data)
    quickSort(0, len(data)-1, data)
    print("Data Setelah Diurutkan -->")
    print(data)


cetak(data)
