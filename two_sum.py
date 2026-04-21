#Problem: Two Sum
#Link: https://leetcode.com/problems/two-sum/

# 🔴 1. Brute Force (i, j approach)

# Idea:
# Use two loops
# Try every pair (i, j)
# Check if:
# nums[i] + nums[j] == target

# Why it's slow:
# Outer loop → n
# Inner loop → n
# Total → O(n^2)

# Visualization:
# i = 0 → check with all j
# i = 1 → check with all j
# ...
# 👉 Works but inefficient for large input


# 🟢 2. Optimized Approach (Hash Map) — BEST

# Core Idea:
# Instead of checking every pair, we:
# - Store numbers we've seen in a hash map
# - For each number, compute:
#   remaining = target - current_number
# - Then check:
#   "Have I already seen this remaining number?"


# 🔁 Step-by-step example

# nums = [2, 7, 11, 15], target = 9

# Step | num | remaining | HashMap   | Action
# 1    | 2   | 7         | {}        | store 2
# 2    | 7   | 2         | {2:0}     | FOUND → return


# 💡 Key Insight:

# Instead of:
# find pair

# We do:
# for each num:
#     check if (target - num) already exists


# ⚡ Time & Space Complexity

# Approach       Time      Space
# Brute Force    O(n^2)    O(1)
# Hash Map       O(n)      O(n)


# 🧠 Python Code (Optimal Solution)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 🔹 Hash map to store value -> index
        num_map = {}

        # 🔹 Traverse the list
        for i in range(len(nums)):

            # Current number
            current = nums[i]

            # 🔹 Find remaining value needed to reach target
            remaining = target - current

            # 🔹 Check if remaining already exists in hashmap
            if remaining in num_map:
                # Found the pair → return indices
                return [num_map[remaining], i]

            # 🔹 Store current number with its index
            num_map[current] = i

        # (Problem guarantees one solution, so this won't run)
        return []
