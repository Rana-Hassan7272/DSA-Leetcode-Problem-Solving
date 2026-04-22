# Problem #12: Subarray Sum Equals K

# Link:https://leetcode.com/problems/subarray-sum-equals-k


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """
        🧠 Problem (Simple Words):

        Given an array,
        count how many subarrays have sum = k

        👉 Subarray = continuous elements

        Example:
        nums = [1,1,1], k = 2
        → subarrays: [1,1] (index 0-1), [1,1] (index 1-2)
        → answer = 2


        🔴 Brute Force:

        Idea:
        - Try all subarrays
        - Calculate sum each time

        ❌ Time Complexity:
        - O(n^2)
        - Too slow for large input


        🟢 Optimized Approach (Prefix Sum + HashMap) — BEST

        💡 Core Idea:

        Instead of checking all subarrays,
        we use prefix sum to track cumulative sum

        prefix_sum[i] = sum from index 0 to i


        🔑 Important Equation:

        If:
        current_sum - previous_sum = k

        Then:
        previous_sum = current_sum - k

        👉 So we check:
        "Have we seen (current_sum - k) before?"


        🔁 Step-by-step:

        nums = [1,2,3], k = 3

        prefix_sum = 0
        map = {0:1}  (IMPORTANT initialization)

        Step 1:
        sum = 1
        check (1-3=-2) → not found

        Step 2:
        sum = 3
        check (3-3=0) → found → count += 1

        Step 3:
        sum = 6
        check (6-3=3) → found → count += 1

        👉 Answer = 2


        💡 Why map = {0:1}?

        - Handles case when subarray starts from index 0


        ⚡ Complexity:
        - Time: O(n) ✅
        - Space: O(n)
        """


        # 🔹 HashMap: prefix_sum → frequency
        prefix_map = {0: 1}

        current_sum = 0
        count = 0

        # 🔹 Traverse array
        for num in nums:
            current_sum += num

            # 🔹 Check if (current_sum - k) exists
            if (current_sum - k) in prefix_map:
                count += prefix_map[current_sum - k]

            # 🔹 Store current_sum in map
            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

        return count
