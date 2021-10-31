# Bubble Sort
data = [6, 3, 4, 5, 7, 0, 2, 8, 9, 1]


def bubbleSort(data):
    panjang_data = len(data)

    for i in range(panjang_data):
        print('step', i)
        for j in range(0, panjang_data - i - 1):
            print('sub-step', j)
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp


def cetak(data):
    print("Data Asal -->")
    print(data)
    bubbleSort(data)
    print("Data Setelah Diurutkan -->")
    print(data)


cetak(data)
