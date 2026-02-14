# File handling
from os import write


# r - read
# w - Write
# a - append

# read
# file = open("data.txt","r")
# content = file.read()
# print(content)

# write
# file = open("data.txt","w")
# file.write("Hello Python \n")
# file.write("File handling example")
# file.close()

# with open("data.txt","r") as f:
#     print(f.read())

# append
def save_student(name, marks):
    with open('student.txt', 'a') as file:
        file.write(f"{name} - {marks}\n")

save_student('John', [20, 30, 40])
save_student('Jane', [20, 30, 40])
save_student('Carl', [20, 30, 40])

file = open("student.txt","r")
print(file.read())
file.close()

# r - read only
# w - write only
# a - append only
# r+ - read + write
# w+ - write + read
# a+ - append + read

