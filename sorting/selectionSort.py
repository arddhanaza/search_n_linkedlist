# Selection Sort
data = [6, 3, 4, 5, 7, 0, 2, 8, 9, 1]


def selectionSort(data):
    panjang_data = len(data)

    for i in range(panjang_data):
        index_min_data = i
        print('step', i)
        for j in range(i + 1, panjang_data):
            print('sub-step', j)
            if data[index_min_data] > data[j]:
                index_min_data = j
        temp = data[i]
        data[i] = data[index_min_data]
        data[index_min_data] = temp


def cetak(data):
    print("Data Asal -->")
    print(data)
    selectionSort(data)
    print("Data Setelah Diurutkan -->")
    print(data)


cetak(data)
