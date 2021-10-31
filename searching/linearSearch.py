# Linear Search
data = [6, 3, 4, 5, 7, 0, 2, 8, 9, 1]

def linearSearch(data, data_yang_dicari):
    for i in range(len(data)):
        if data[i] == data_yang_dicari:
            print("Data berada pada Index ke ", i)
            exit()
    print("Data Not Found")

def cetak(data):
    print("Data Asal -->")
    print(data)
    data_yang_dicari = 0
    print("Data Yang Dicari -->")
    linearSearch(data, data_yang_dicari)

cetak(data)
