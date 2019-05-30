profit = int(input("请输入当年利润： "))

profit_list = [1000000, 600000, 400000, 200000, 100000, 0]

rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

bonus = 0

for i in range(0, 6):
    if profit > profit_list[i]:
        bonus += (profit - profit_list[i]) * rate[i]
        print((profit - profit_list[i]) * rate[i])
        profit = profit_list[i]

print(f"当月获得的奖金总额为： {bonus}")
