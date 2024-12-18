# Write a Python program to store roll numbers of student in array who attended training program in random order. Write function for searching whether particular student attended training program or not, using following:
# a) Linear search 
# b) Sentinel search.
# c) Binary Search

def linear_search(array, key):
    #Searches for the key in the array using linear search. 
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1

def sentinel_search(array, key):
    #Searches for the key in the array using sentinel search.
    n = len(array)
    last = array[-1]
    array[-1] = key
    i = 0
    while array[i] != key:
        i += 1
    array[-1] = last
    if i < n - 1 or array[-1] == key:
        return i
    return -1

def binary_search(array, key):
    #Searches for the key in the sorted array using binary search.
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    # Input array of roll numbers
    n = int(input("Enter the number of students who attended the training: "))
    array = []
    for i in range(n):
        print("Enter roll number of student", i + 1, ":", end=" ")
        roll_no = int(input())
        array.append(roll_no)

    key = int(input("\nEnter roll number to search:"))

    # Perform linear search
    index = linear_search(array, key)
    if index != -1:
        print("\nLinear Search: Roll number", key, "found at position", index + 1)
    else:
        print("\nLinear Search: Roll number", key, "not found.")

    # Perform sentinel search
    index = sentinel_search(array, key)
    if index != -1:
        print("\nSentinel Search: Roll number", key, "found at position", index + 1)
    else:
        print("\nSentinel Search: Roll number", key, "not found.")

    # Perform binary search
    sortedArray=array.sort()
    print("\nArray sorted for Binary Search:", array)
    index = binary_search(array, key)
    if index != -1:
        print("Binary Search: Roll number", key, "found at position", index + 1)
    else:
        print("Binary Search: Roll number", key, "not found.")

main()