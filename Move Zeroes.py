nums = [0,1,0,3,12]
pos = []
for i in range(len(nums)):
    if nums[i] == 0:
        pos.append(i)
print(pos)
leng = len(pos)
k = 0
for i in pos:
    nums.pop(i-k)
    k += 1
print(nums)
for l in range(leng):
    nums.append(0)
print(nums)






