# list: The list in which we are searching for an element. # * item: The element we're searching for
def BinarySearch(list, item):

    low = 0  # low: starts at 0 (the first index of the list)
    high = len(list) - 1  # * high: starts at len(list)-1 (the last index of the list)s

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


myList = [1, 3, 7, 9]

print(BinarySearch(myList, 3))  # => 1
print(BinarySearch(myList, -1))  # ! None
