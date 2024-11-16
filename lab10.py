#task 1
from ctypes.wintypes import tagMSG

a = input()
w = ""
for i in a:
    w = i + w
if (a == w):
    print("Yes")
else:
    print("No")
print(w)


#task 2
s = int(input())
days = s // 86400
remaining_seconds = s % 86400

hours = remaining_seconds // 3600
remaining_seconds %= 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"{days}:{hours:02}:{minutes:02}:{seconds:02}")
#task 3
nums_b = input()
nums = [int(num.strip()) for num in nums_b.split(",")]
nums_t = tuple(nums)
print(nums)
print(nums_t)
#task 4
l = ["asd", 1231, "3212321", "track"]
print(l[0], l[-1])
#task 5
file = input()
if "." in file:
    extension = file.split(".")[-1]
    if extension:
        print(f"The file extension is: {extension}")
    else:
        raise ValueError("File extension cannot be determined.")
else:
    raise ValueError("File extension cannot be determined.")
#task 6
n = int(input())
count = n + ((n * 10) + n) + ((n * 100) + ((n * 10) + n))
print(count)
#task 7
nums = [123, 22, 140, 30, 33, 237, 10, 11, 45, 42]
for i in nums:
    if i % 2 == 0:
        print(i)
    if i == 237:
        break
    else:
        continue
