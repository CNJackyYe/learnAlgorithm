def binary_search(list_1, item):
    low = 0
    high = len(list_1)-1

    while low <= high:
        mid = round((low+high)/2)
        guess = list_1[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid+1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7]

print(binary_search(my_list, -9))
