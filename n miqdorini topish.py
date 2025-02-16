a = int(input())
nums = []
for i in range(100,1000):
    count = 0
    for j in str(i):
        if j == str(a):
            count += 1
    if count == 2:
        nums.append(i)
print(nums)