# Insertion Sort
data = [6, 3, 4, 5, 7, 0, 2, 8, 9, 1]


def insertionSort(data):
    panjang_data = len(data)
    for i in range(1, panjang_data):
        temp = data[i]
        index_j = i-1
        while index_j >= 0 and temp < data[index_j]:
            data[index_j + 1] = data[index_j]
            index_j -= 1
        data[index_j + 1] = temp


def cetak(data):
    print("Data Asal -->")
    print(data)
    insertionSort(data)
    print("Data Setelah Diurutkan -->")
    print(data)


cetak(data)
