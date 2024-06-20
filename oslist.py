# import os
# folders=os.listdir("Data")
# print(folders)
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"Data/{folder}"))

# o/p:
# ['Day3', 'Day1', 'Day2']
# Day3
# []
# Day1
# []
# Day2
# []

import os
folder=os.listdir("Data")
print(os.getcwd())

#/home/janvi/Desktop/Python
os.chdir("/Python")
print(os.getcwd())
