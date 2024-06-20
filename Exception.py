'''a=input('enter the number:')
try:
    for i in range(1,11):
        print(f'{int(a)} X {i} ={int(a)*i}')
except:
    print('invalid')
print("end of program")

a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
  print("Invalid  Input!")

print("Some imp lines of code")
print("End of program")'''

# try:
#     num=int(input('enter index:'))
#     a=[6,3,8,9,0]
#     print(a[num])
# except ValueError:
#     print('Number entered is not an integer')

# except IndexError:
#     print('index error')

# output:
# enter number:0
# 6
# enter number:1
# 3
# enter number:4
# index error
# enter number:eer
# Number entered is not an integer




#finally is always execute: may be function is return thay jai to pan finally to work karse j.

# def func():
#     try:
#         l=[1,2,3,4,5]
#         i=int(input("enter index: "))
#         print(l[i])
#     except:
#         print('some error')
#     finally:
#         print('i am always execute')
# # x=func()
# # print(x)
# func()
# o/p:
# enter index: 6
# some error
# i am always execute

#custom errors:

# raise keyword is generate the error

# a = int(input("Enter any value between 5 and  9 :"))

# if(a<5 or a>9):
#   raise ValueError("Value should be between 5 and 9")

#shorthand if-else
# a=3301
# b=330
# print("A")if a>b else print("=") if a==b else print("B")

# enumerate function / linter

# marks=[89,90,78,98]
# index=0
# for mark in marks:
#     print(mark)
#     if(index==2):
#         print('awesome!!!')
#     index+=1

# marks=[89,90,78,98]
# for mark in marks:
#     if(mark==78):
#         continue
#     print(mark)


#enumarate function - it is return index 
#      
# fruits=['apple','banana','mango']
# for index,fruit in enumerate(fruits):
#     print(index,fruit)

# 0 apple
# 1 banana
# 2 mango

# marks=[4,6,7,32,78]
# for index,mark in enumerate(marks,start=1):
#     print(index,mark)
#     if (index==3):
#         print("awesome")

# o/p:
# 1 4
# 2 6
# 3 7
# awesome
# 4 32
# 5 78