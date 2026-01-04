num = "100101"

decimal_nums = [int(n) * pow(2, idx) for idx, n in enumerate(reversed(num))]
acc = 0
for n in decimal_nums:
    acc += n

print(acc)
