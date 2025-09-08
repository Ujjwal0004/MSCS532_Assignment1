def insertion_sort(A):
    
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
       # Moving smaller numbers/elements to the right
        while j >= 0 and A[j] < key:
            A[j + 1] = A[j]
            j = j - 1

        A[j + 1] = key
    return A

# Asking user input to sort the numbers in decreasing order     
user_input = input("Enter numbers separated by spaces: ")
A = list(map(int, user_input.strip().split()))
print("Original array:", A)
insertion_sort(A)
print("Sorted numbers in decreasing order:", A)
