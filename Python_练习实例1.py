# 方法1
num_list = []

for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if (a != b) and (a != c) and (b != c):
                num_list.append(a * 100 + b * 10 + c)

print(f"互不相同且无重复的三位数一共有 {len(num_list)} 个")
print(num_list)

# 方法2
list_num = [1, 2, 3, 4]

list = [i * 100 + j * 10 + k for i in list_num for j in list_num for k in list_num if (i != j and i != k and j != k)]

print(f"互不相同且无重复的三位数一共有 {len(list)} 个")
print(list)


# 方法3
from itertools import permutations


list_num = []

for i in permutations([1, 2, 3, 4], 3):
    list_num.append(i)

print(len(list_num))
print(list_num)
