import random
import time
# def numbers(n):
#     z=0
#     f=[]
#     number =[random.randint(0,n) for i in range(10)]
#     print(number)
#     for i in range(len(number)-1):
#         if (number[i]+number[i+1])%2 !=0:
#             z+=1
#             f.append((number[i],number[i+1]))
#     return z,f
#
# print(numbers(n=int(input())))


def linearSearch(lys, element):
    for i in range(len(lys)):
        if lys[i] == element:
            return i
        return -1



print(linearSearch(lys=[random.randint(0, 12)for i in range(20)], element=int(input()) ))