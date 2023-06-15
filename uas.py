from random import randint

def acak():
    arr = []
    for i in range(50):
        bilangan = randint(1, 30)
        arr.append(bilangan)
    return arr

def mergeSort_pemecahan(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    kiri = arr[:mid]
    kanan = arr[mid:]

    return kiri, kanan

def selectionSort(arr, size):
    for i in range(size):
        min_idx = i

        for j in range(i + 1, size):
            # To sort in descending order, change > to < in this line
            # Select the minimum element in each loop
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Put min at the correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def mergeSort(arr, descending=True):
    if len(arr) > 1:
        # Pembagian array menjadi dua bagian
        mid = len(arr) // 2
        kiri = arr[:mid]
        kanan = arr[mid:]

        # Rekursi untuk mengurutkan bagian kiri dan kanan
        mergeSort(kiri, descending)
        mergeSort(kanan, descending)

        i = j = k = 0

        # Menggabungkan kembali dua bagian yang telah diurutkan berdasarkan mode pengurutan
        if descending:  # Mode descending
            while i < len(kiri) and j < len(kanan):
                if kiri[i] >= kanan[j]:
                    arr[k] = kiri[i]
                    i += 1
                else:
                    arr[k] = kanan[j]
                    j += 1
                k += 1
        else:  # Mode ascending (default)
            while i < len(kiri) and j < len(kanan):
                if kiri[i] <= kanan[j]:
                    arr[k] = kiri[i]
                    i += 1
                else:
                    arr[k] = kanan[j]
                    j += 1
                k += 1

        # Menyalin sisa elemen yang tersisa (jika ada)
        while i < len(kiri):
            arr[k] = kiri[i]
            i += 1
            k += 1

        while j < len(kanan):
            arr[k] = kanan[j]
            j += 1
            k += 1
def search(arr1, n, arr2):
    linear = []
    for i in range(n):
        if arr1[i] == arr2:
            linear.append(i)
    return linear
if __name__ == "__main__":
    arr = acak()
    print("Data Awal:", arr)
    kiri, kanan = mergeSort_pemecahan(arr)
    print("data 1 : ", kiri)
    print("data 2 : ", kanan)
    
    size = len(kanan)
    selectionSort(kanan, size)
    mergeSort(kiri, descending=True)
    
    print("Hasil Selection sort ascending:", kanan)
    print("Hasil Merge sort descending:", kiri)
    unique = []
    for value in kiri:
        if value in kanan:
            unique.append(value)
    unique_array = list(set(unique))
    print("Array data setelah menghapus data ganda:", unique)