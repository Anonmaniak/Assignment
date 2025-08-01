print("Topic: Find the length of the longest increasing subsequence in an array.")

from typing import List

def length_of_LIS(nums: List[int]) -> int:
    if not nums:
        return 0
    
    dp = [1]* len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)

nums = [10,9,2,5,3,7,101,18]
print(length_of_LIS(nums))