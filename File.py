# f=open('abc.txt','r')
# print(f.read())
# f.close()

# with open('myfile.txt','w') as f:
#     f.write("hello world!!!!")

#writelines
# f=open('myfile.txt','r')
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#         break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"marks of student {i} in Maths is : {m1}")
#     print(f"marks of student {i} in science is : {m2}")
#     print(f"marks of student {i} in english is : {m3}")
#     print(line)

#Writelines
# f=open('myfile1.txt','w')
# lines=['line1\n','line2\n','line3\n']
# f.writelines(lines)
# f.close()

# f=open('myfile2.txt','w')
# lines=['line1','line2','line3']
# for line in lines:
#     f.write(line+'\n')
# f.close()

# with open('abc.txt','r') as f:
#     print(type(f))
#     f.seek(10) //move to next to 10 bytes
#     data=f.read(5) //read after move only 5 char
#     print(data)


# a=[1,2]
# print(a*3)

# with open('abc.txt','r') as f:
#     print(type(f))
#     f.seek(10) 
#     print(f.tell())  //ketla char pachi read karvanu che te k..
#     data=f.read(5)
#     print(data)

# o/p:
# <class '_io.TextIOWrapper'>
# 10
# you a

# with open('abcd.txt','w') as f:
#     f.write("hello world")
#     f.truncate(5) //how many char display
# with open('abcd.txt','r') as f:
#     print(f.read())

f=open("abc.txt",'a+')
s=" "
while s!="*":
    s=input()
    if s!="*":
        f.write(s+"\n")
    f.seek(0,0)
    data=f.read()
    print(data)
f.close()
