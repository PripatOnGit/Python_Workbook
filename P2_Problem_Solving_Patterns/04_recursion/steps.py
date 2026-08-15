def cal_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return cal_stairs(n-1) + cal_stairs(n-2)

print(cal_stairs(5))
print(cal_stairs(40))