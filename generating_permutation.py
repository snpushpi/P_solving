def permute(nums):
    if len(nums)==0:
        return []
    if len(nums)==1:
        return [nums]
    result = []
    for i in range(len(nums)):
        for p in permute(nums[:i]+nums[i+1:]):
            result.append([nums[i]]+p)
    return result