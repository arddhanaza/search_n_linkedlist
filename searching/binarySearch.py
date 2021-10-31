# Binary Search

data = [6, 3, 4, 5, 7, 2, 8, 9, 1,0]


def binarySearch(data, data_yang_dicari):
    first = 0
    last = len(data) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if data[mid] == data_yang_dicari:
            index = mid
        else:
            if data_yang_dicari < data[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


def cetak(data, data_yang_dicari):
    data.sort()
    print(data)
    result = binarySearch(data, 2)
    if result >= 0:
        print("Ketemuu di index ke ", result)
    else:
        print("Ga ketemu")


cetak(data, 10)
