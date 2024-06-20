# a=5
# print(a)

# s5=r'Welcome to \t"Atmiya University", \nRajkot' 
# print(s5)

# str='Good Morning!'
# s1='Morning'
# s2='Evening'
# print(str)
# str=str.replace(s1,s2)
# print(str)
# line="welcome to the \"world\" in \'python\'  \tmy new world \nMumbai"
# print(line)

# end 
# print('a','b','c','janvi',123 , 'My','Hello', end='12')
# print("Janvi")

# sep
# print('a','b','c','janvi',123 , 'My','Hello', end='12',sep=' * ')

# Type Conversion
# a="21"
# b="22"
# print(a+b)
# print(int(a) + int(b))

# c=23
# d=89
# print(c+d)
# print(str(c) + str(d))

# b=9.0
# print(type(b))

# split Method
# a="Janvi, Ashara pareshbhai"
# print(a.split(","))


# txt = "#apple#banana#cherry#orange"
# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.split("#", 2)
# print(x)

# txt1 = "hello, my name is Peter, I am 26 years old"
# x = txt1.split(", ")
# print(x)

# txt = "apple#banana#cherry#orange"
# x = txt.split("#")
# print(x)


# name = "python"
# A=''' He said , hi janvi ,Hey I am good "I want to EAT an Apple"'''
# print(A)
# print('I Like ',name)

# a=1,2,3,43
# print(type(a))




# slicing of string

# a="harry"
# print(a[-4:-2])
# a="janvi"
# print(a[-4:-2])
# a="Atmiya University"
# print(a[0:17])
# print(a[0:17:1])
# print(a[0:17:2])
# print(len(a))
# print(a[-1: ])
# print(a[::-1])
# print(a[-8:-3])
# print(a[-3:-8])

# import time
# # Get the current time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# #Using time.strptime to parse a time string:
# time_string = "15:45:30"
# parsed_time = time.strptime(time_string, '%H:%M:%S')
# print(parsed_time)

# current_time = time.time()
# print(current_time)

# formatted_time = time.strftime('%Y-%m-%d %H:%M:%S')
# print(formatted_time)

# localtime = time.localtime()
# epoch_time = time.mktime(localtime)
# print(epoch_time)

# print ("Time calculated acc. to given seconds is : ")
# print (time.gmtime())

#Loops for,while,break,continue

# for i in range(11):
#     print('5 X',i,'=',5*i)

# for i in range(6):
#     if(i == 3):
#         print('loop end')
#         break
#     print('5 X',i,'=',5*i)
# print('\n')

# for i in range(6):
#     if(i == 3):
#         print('Skip particular iteration')
#         continue
#     print('3 X',i,'=',3*i)
    

# i=0
# while True:
#     print(i)
#     i+=1
#     if(i%100==0):     
#         break
# print('end')

# i=int(input('enter the number :'))
# while i<40:
#     i=int(input('enter the number :'))
#     print(i)
# print("Done the loop")
    
# count = 5
# while(count > 0):
#     print(count)
#     count-=1
# else:
#     print("inside else")

#Allow user to enter number when user press zero sum of all numbers
# total=0
# i=int(input('enter the number:'))
# # print(i)
# while(i>0):
#     total=total+i
#     i=int(input('enter the number:'))
# print('the sum of all number',total)

#print 1-10 square
# for i in range(1,11):
#     print(i**2)

# no=1
# while(no<=10):
#     print(no**2)
#     no+=1

#find even number of given set using for loop
# a=[20,3,4,6,7,9,11,23,60]
# for i in a:
#     if(i%2==0):
#         print(i)

#find even number of given set using for loop
# a=[20,3,4,6,7,9,11,23,60,89,90]
# b=0
# while b<len(a):
#     if a[b]%2==0:
#         print(a[b])
#     b+=1

# # a=[0,3,4,5]
# # print(len(a))

# a='JANVI ASHARA'
# b=0
# while(b<len(a)):
#     print(a[b])
#     b+=1


# colors=['red','green','blue']
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# a='janvi'
# for i in a:
#     # print(i,end=' ')
#     print(i)

#using range function
# a='Atmiya'
# n=len(a)
# for i in range(n):
#     print(a[i])

# lst=[2,4,6,3,4]
# sum=0
# for i in lst:
#     sum=sum+i
# print('the sum is',sum)

#=================i==4========not a index,it's a value============> 

# a=[1,2,3,4,5,6,7]
# for i in a:
#     print(i)
#     if i==4:
#         break

# j=(1,3,4,45,6,9,8)
# for i in j:
#     print(i)
#     if i==4:   
#         break




#Match Case (Switch case as an other Language)

# a=int(input('Enter the Number:'))
# match a:
    # case 0:
    #     print("you enter zero")
    # case 1:
    #     print("you enter one")
    # case 2:
    #     print("you enter two")
    # case 3:
    #     print("you enter three")
    # case 4:
    #     print("you enter four")
    # case 5:
    #     print("you enter five")
    # case _ if a!=90:
    #     print(a,'a is not ninty')
    # case _:
    #     print("underscore is bydefault")


# output:
#  Enter the Number:90
# underscore is bydefault

# a="Atmiya University"
# for i in a:
#     print(i)

# a="Atmiya"
# b=0
# while b<len(a):
#     print(a[b])
#     b=b+1

# a=[2,4,5,6,7]
# n=len(a)
# for i in range(n):
#     sqr=a[i]**2
#     print(sqr)

# a=[2,4,5,6,7]
# n=len(a)
# sqr=0
# for i in range(n):
#     sqr=sqr+a[i]**2
# print(sqr)

#Pattern 

# for i in range(3):
#     for j in range(4):
#         print(j,end='')
#     print()

# rows=4
# for i in range(1,rows+1):
#     print('*' * i)

# rows=1
# for i in range(4,rows-1,-1):
#     print('*' * i)


# for i in range(4):
#     for j in range(4):
#         print(i,end='')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()


# for i in range(1,6):
#     print('*' * i )
# for j in range(5,0,-1):
    # print('*' * j)

# Output;
# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *

# rows=1 ,rows-1(end cond)

# for i in range(5, 0, -1):
#     spaces = ' ' * (5 - i)
#     print(spaces + '*' * i)

# for i in range(1,5):
#     space = '0' * (5-i)
#     print(space + "*" * i)

# output

# *****
#  ****
#   ***
#    **
#     *
#     *
#    **
#   ***
#  ****


# print(1)

#format string

# li='hi , my name is {0} ,i am from {1},imy favourite country is {0}'
# name='janvi'
# country='india'
# print(li.format(name,country))

# txt="for only rs:{price:.2f}"
# print(txt.format(price=4090.987976))

# # OR
# price=45.87987987
# txt=f'price only: {price:.2f}'
# print(txt)

# for only rs:4090.99
# price only price=45.88

# print(f"{2*30}")
# nm='janvi'
# print(f"my nm is {nm} {{nm}}")
# output
# 60
# my nm is janvi {nm}


# a:int =10
# print(a)
# b: str= 'janvi'
# print(b)

# j:int = 20000000
# print(f'{j:_}')
# a=60000000
# print(f'{a:,}')

#generate a space

# var:str='janvi'
# print(f'{var:>20}')  //right
# print(f'{var:<20}') //left
# print(f'{var:^20}') //center

# n=454545.5656
# print(round(n,2))
# print(f'{n:.2f}')
# print(f'{n:.0f}')
# print(f'{n:,.3f}')

# o/p:
# 454545.57
# 454545.57
# 454546
# 454,545.566

# a:int =5
# b:int =10
# my_var : str ='hii janvi'
# print(f'{a+b = }')
# print(f'{bool(a)}')
# print(f'{my_var= }')

# janvi@janvi-ThinkPad:~/Desktop/Python$ python3 a.py
# a+b = 15
# True
# my_var= 'hii janvi'

# from datetime import datetime
# now:datetime =datetime.now()
# print(f'{now:%d.%m.%y(%H:%m:%s)}')
# print(f'{now:%c}')
# print(f'{now:%I%p}')
# o/p:
# 18.06.24(19:06:1718720344)
# Tue Jun 18 19:49:04 2024
# 07PM