year = int(input("年份： "))
month = int(input("月份： "))
day = int(input("日期： "))

months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

if 0 < month <= 12:
    sum = months[month - 1]
else:
    print("月份输入有误")

sum += day

leap = 0

if (year % 400 == 0) or ((year % 4) == 0 and (year % 100 != 0)):
    leap = 1
if leap == 1 and month > 2:
    sum += 1

print(f"现在是 {year}年 的 第{sum}天")