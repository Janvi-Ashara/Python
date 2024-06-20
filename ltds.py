# list

# a=['janvi','a','hello',1,4,True]
# print(a)

# lst = range(1,10,2)
# for i in lst:
#     print(i , end=' ')

# lst=list(range(1,11))
# print(lst)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# del lst[8]
# print(lst)
# # 6 is a value
# print(lst.index(6))

# lst1=[2,6,4,5,7]
# lst1.reverse()
# print(lst1)

# lst1.sort(reverse=True)
# print(lst1)

# ls=[10,20,30,50]
# ls1=ls
# print(ls)
# ls[3]=23
# print(ls)
# print(ls1)

# ls=[10,20,30,50]
# ls1=ls[ : ] 
# print(ls)
# print(ls1)

# ls=[]
# n=int(input("how many element you  want to enter?"))
# for i in range(n):
#     print("enter element  : ")
#     ls.append(int(input('element is :')))
#     print('the element',ls)
# find=int(input('Enter an element you want to count :'))
# cnt=0
# for i in ls:
#     if find==i:
#         cnt=cnt+1
# print(f"{find} is found {cnt} time")

# a=(1,'j','a','n','v','i')
# print(a)
# b=list(a)
# print(b)

# name=input("enter your namr :")
# city=input("enter your dream city : ")
# print(f'My name is {name} and my dream city is {city}')

# lst = [i*i for i in range(10)]
# print(lst)
# lst=[i*i for i in range(10) if i%2==0]
# print(lst)
# lst1=[i for i in range(10) if i*2==0] 
# print(lst1)   //not working

# output:
# 0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# [0, 4, 16, 36, 64]
# [0]

# ls=[10,20,30,50]
# ls.insert(1,89)
# ls.insert(2,90)
# print(ls)
# [10, 89, 20, 30, 50]
# m=[7,8,9]
# ls.extend(m)
# print(ls)
#[10, 20, 90, 30, 50, 7, 8, 9]

# a=(1,)
# print(type(a))
# type=tuple aavse


# a=[1,2,3,4,5,6]
# print(a)
# b=tuple(a)
# print(b)

# print(a[2:5])

# tpl=(1,'janvi')
# rno,name=tpl[0:2]
# print(rno,name)

#update the tuple
# num=(1,2,34,5)
# print(num)
# lst=list(num)
# print(lst)
# a=int(input('enter the position:'))
# lst[a]=int(input('enter the number :'))
# print(lst)
# num=tuple(lst)
# print(num)

# #delete in tuple
# num=(1,2,34,5,6,67)
# print(num)
# lst=list(num)
# print(lst)
# a=int(input('enter the position:'))
# print(lst)
# del (lst[a])
# print(lst)
# lst.remove(5)
# print(lst)
# num=tuple(lst)
# print(num)

# output:
# (1, 2, 34, 5, 6, 67)
# [1, 2, 34, 5, 6, 67]
# enter the position:2
# [1, 2, 34, 5, 6, 67]
# [1, 2, 5, 6, 67]
# [1, 2, 6, 67]
# (1, 2, 6, 67)


#set{}

# cities={}
# print(type(cities))

# a=set()
# print(type(a))

# city1={'japan','india','usa'}
# city2={'munich','nepal','peris','japan'}
# city3={'rjt','srt','vdr'}
# city4={'ahm','jmn'}
# city35={'rjt','srt'}
# print(city1.union(city2))
# city1.update(city2)
# print(city1,city2)
# city1.difference_update(city2)
# print(city1)
# print(city1.intersection(city2))
# city1.intersection_update(city2)
# print(city1)
# print(city1.symmetric_difference(city2))
# city1.symmetric_difference_update(city2)
# print(city1)
# print(city3.isdisjoint(city4))
# print(city3.issuperset(city35))
# city2.add("ltaly")
# print(city2)

# Output
# {'japan'}
# None
# {'nepal', 'peris', 'munich'}
# None
# True
# True

# info={'car',5,6,True}
# if "car" in info:
#     print("Yes")
# else:
#     print("no")



# function:
#DOC_STRING
# def square(n):
#     # print(none) Error generate karse...
#     ''' takt the number n ,return  value'''
#     print(n**2)
# square(5)
# print(square.__doc__)


# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("average is :" ,sum/len(numbers))
# average(30,8,98,6,7)

#for loop with else

# for x in range(5):
#     print("iteration no{} in for loop".format(x+1))
# else:
#     print("else block  in loop")
# print("out of loop")

#Recursion:

# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# # a=factorial(5)
# # print(a)
# print(factorial(6))

#fibonacci series
# f0=0
# f1=1
# a=int(input('enter number:'))
# for i in range(a):
#     i=f0+f1
#     print(f0)
#     f0=f1
#     f1=i

# def fibo(n):
#     f0=0
#     f1=1
#     if (n==0 or n==1):
#         return 0
#     else:
#         for fn in range(2,n+1):
#             fn=f0+f1
#             f0=f1
#             f1=fn
#         return f1

# a = int(input('Enter the number: '))
# print(fibo(a))
# print(fibo(9))

# def Fibonacci(n):
#     if n<= 0:
#         print("Incorrect input")
#     # First Fibonacci number is 0
#     elif n == 1:
#         return 0
#     # Second Fibonacci number is 1
#     elif n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
 
# # Driver Program
 
# print(Fibonacci(10))

def fibo_series(n):
    f0 = 0
    f1 = 1
    if n == 0 or n==1:
        return 1
    else:
        print(f0, f1, end=' ')
        for i in range(2, n):
            fn = f0 + f1
            print(fn, end=' ')
            f0 = f1
            f1 = fn

a = int(input('Enter the number of terms: '))
fibo_series(a)
