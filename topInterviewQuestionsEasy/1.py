def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    print(nums)
    return i + 1

foo = [1,2,3,4,4,5]
print(foo)
print(removeDuplicates(foo))
