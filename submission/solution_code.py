
from typing import Dict, List

# ---------------- P015 - Depth-First Search (DFS) ----------------
def dfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    result = []

    def dfs_helper(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph.get(node, []):
                dfs_helper(neighbor)

    dfs_helper(start)
    return result


# ---------------- P016 - Check Duplicates ----------------
def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


# ---------------- P017 - Longest Increasing Subsequence ----------------
def length_of_LIS(nums: List[int]) -> int:
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# ---------------- Test Cases ----------------
if __name__ == "__main__":
    print("Testing P015 - DFS")
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    print("DFS from node 2:", dfs(graph, 2))  # Expected: [2, 0, 1, 3]

    print("\nTesting P016 - Contains Duplicate")
    print(contains_duplicate([1, 2, 3, 1]))  # Expected: True
    print(contains_duplicate([1, 2, 3]))    # Expected: False

    print("\nTesting P017 - Longest Increasing Subsequence")
    print(length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Expected: 4
    print(length_of_LIS([1, 3, 6, 7, 9]))               # Expected: 5
    print(length_of_LIS([5, 4, 3, 2, 1]))               # Expected: 1
