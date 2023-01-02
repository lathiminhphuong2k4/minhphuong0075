def has_lucky_number(nums):
    a=False
    for x in nums:
        if x%7==0:
            a=True
            break
    return a
nums=[2,6,7,9]
print(has_lucky_number(nums))