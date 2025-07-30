print("Topic: Check if any value appears at least twice in the array.")

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))

nums = [1,2,3,1]
print(contains_duplicate(nums))