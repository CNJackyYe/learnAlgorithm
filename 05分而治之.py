def sum(x, list):
    if list == []:
        return x
    x += list[0]
    return sum(x, list[1:])

print(sum(0, [3, 4, 5, 6, 1, 10]))

#推荐答案

# def sum(list):
#     if list == []:
#         return 0
#     return list[0] + sum(list[1:])


# sum([3, 4, 5, 6, 1, 10])


# list2 = [1, 2, 3, 4, 5, 6]
# print(list2[2:3])

