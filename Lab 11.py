#task 1
def get_unique_elements(list1, list2):
    return [element for element in list1 if element not in list2]
n = int(input())
m = int(input())
list1 = []
list2 = []
for i in range(n):
    list1.append(int(input()))
for i in range(m):
    list2.append(int(input()))

result = get_unique_elements(list1, list2)
print("Elements in list1 not in list2:", result)

#task 2
import os

def list_files_in_directory(directory):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        return files
    except FileNotFoundError:
        return f"The directory {directory} does not exist."
    except PermissionError:
        return f"Permission denied to access {directory}."
directory = "C:/Users/blank/Desktop/Новая папка"
files = list_files_in_directory(directory)
print("Files in directory:", files)

#task 3
number = int(input())
number = abs(number)
digit_sum = 0
for digit in str(number):
    digit_sum += int(digit)
print(digit_sum)

#task 4
string = input()
character = input()
count = 0
for char in string:
    if char == character:
        count += 1
print(character, ":",count)

#task 5
a = int(input())
b = int(input())
a, b = b, a
print(a, b)

#task 6
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
divisible = list(map(lambda x: x % 15, numbers))
print(divisible)

#task 7
m = int(input())
sequence = []
for i in range(m):
    sequence.append(int(input()))
if len(sequence) == len(set(sequence)):
    print("unique")
else:
    print("not unique")