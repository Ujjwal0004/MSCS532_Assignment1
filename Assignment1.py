def insertion_sort(A):
    
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
       
        while j >= 0 and A[j] < key:
            A[j + 1] = A[j]
            j = j - 1

        A[j + 1] = key
    return A

numbers = [5,2,9,1,5,1]
print("Original array:", numbers)
insertion_sort(numbers)
print("Sorted array in decreasing order are :", numbers)
