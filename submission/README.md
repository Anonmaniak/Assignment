Code Submission - Python

Problem P015 – Depth-First Search (DFS): Traverse an undirected graph from a starting node using DFS.

Approach:
- Use a recursive helper function to explore all reachable nodes.
- Maintain a `visited` set to avoid cycles.
- Append visited nodes to the result list.

Example:
Input: graph = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}, start = 2  
Output: [2, 0, 1, 3]

---

Problem P016 – Check Duplicates: Check if any element appears more than once.

Approach:
- Use a `set` to compare length against original list.
- Return True if duplicate exists.

Example:
Input: [1, 2, 3, 1] → Output: True  
Input: [1, 2, 3] → Output: False

---

Problem P017 – Longest Increasing Subsequence: Find the longest increasing subsequence in an array.

Approach:
- Dynamic programming (`dp[i]` is length of LIS ending at index i)
- For each pair `(j, i)` where `j < i`, update `dp[i]` if `nums[i] > nums[j]`.

Example:
Input: [10,9,2,5,3,7,101,18]  
Output: 4 

Input:  [1,3,6,7,9]
output: 5

Input: [5,4,3,2,1] 
output: 1