# def sum(x, list):
#     if list == []:
#         return x
#     x += list[0]
#     sum(x, list[1:])


# sum(0, [3, 4, 5, 6, 1, 10])


def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


sum([3, 4, 5, 6, 1, 10])


list2 = [1, 2, 3, 4, 5, 6]
print(list2[2:3])


def gcd(a,b):
    if b == 0:
        return a
    else:
        gcd(b,a%b)

a = 20000
 
b = 2
 
print('%d 和 %d 的最大公约数为：' %(a,b),gcd(a,b))
