# import janvi as ja
# ja.welcome()

# o/p:
# hii,you are welcome
# hii,you are welcome


# from janvi import *
# welcome()
# print(welcome)

# o/p:
# hii,you are welcome
# hii,you are welcome
# <function welcome at 0x75496b0860e0>

# from janvi import welcome,stri
# welcome()
# print(stri)

# o/p:
# hii,you are welcome
# janvi is a good girl

# import janvi as ja
# ja.welcome()
# print(ja.janvi)

# o/p:
# ii,you are welcome
# janvi is a good girl

# import janvi as ja
# ja.welcome()

# def main():
#     print("Running script directly")
# if __name__ == "__main__":
#     main()

# import os
# os.mkdir("Data")  //create a foder name with data

#with file
# import os
# if(not os.path.exists("data")):
#     os.mkdir("data")
#     print("create directory :data")
# for i in range(5):
#     os.mkdir(f"data/Day{i+1}")
#     file_name=f"data/Day{i+1}/main.py"
#     if not os.path.exists(file_name):
#         with open(file_name,'w') as fp:
#             fp.write("")
#             print(f"Created file: {file_name}")
#     else:
#         print(f"File '{file_name}' already exists")

# import os
# if(not os.path.exists("Test")):
#     os.mkdir("Test")
#     print("created Test")
# else:
#     print("already exists")
# for i in range(10):
#     os.mkdir(f"Test/script{i+1}")
#     file_nm=f"Test/script{i+1}/janvi.py"
#     if(not os.path.exists(file_nm)):
#         with open(file_nm,'w') as f:
#             f.write("hello janvi")
#             print(f"file is created :{file_nm}")
#     else:
#         print(f"file is exits{file_nm}")


# import os
# if(not os.path.exists("Data")):
#     os.mkdir("Data")
# for i in range(3):
#     os.mkdir(f"Data/Day{i+1}")

# import os
# for i in range(3):
#     os.rename(f"Data/Day {i+1}",f"Test/test {i+1}")
