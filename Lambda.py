# def cube(x):
#     return x*x*x
# print(cube(3))

# # using lambda
# f1= lambda x : x*x
# print(f1(3))

# def app(fx,value):
#     return 6+ fx(value)
# print(app(f1,2))
# print(app(lambda x:x*x*x,2))

# Map ,filter ,reduce
# cube=lambda x:x*x*x
# print(cube(4))

# l=[2,4,5,3,7,34]
# print(l)
# ls=[]
# for i in l:
#     ls.append(cube(i))
# print(ls)

# def cube(x):
#     return x*x*x
# # print(cube(2))
# l=[1,2,4,5,3,7]
# new=list(map(cube,l))
# print(new)

# numbers=[1,5,6]
# new1=list(map(lambda x: x*x +2,numbers))
# print(new1)

# num=[int(i) for i in input("enter value :").split(",")] //by comma //.split(" ") //by space
# print(list(map(lambda i: i*i,num)))


# l=[3,2,4,5]
# def func(x):
#     return x%2==0
# new1=list(filter(func,l))
# print(new1)

# num=[int(i) for i in input("enter value:").split(",")]
# print(list(filter(lambda x:x%2==0,num)))

# o/p:
# nter value:2,3,4,6,8
# [2, 4, 6, 8]

from functools import *
# from functools import  reduce
l=[2,1,3,45,6]
# sum=reduce(lambda a,b : a+b,l)
# print(sum)

def mysum(x,y):
    return x+y
sum=reduce(mysum,l)
print(sum)