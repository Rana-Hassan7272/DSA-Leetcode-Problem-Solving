# Problem #7: Product of Array Except Self

# Link:https://leetcode.com/problems/product-of-array-except-self


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        🧠 Problem Understanding (Simple):

        You are given an array nums.

        You need to create a new array such that:
        answer[i] = product of all elements EXCEPT nums[i]

        Example:
        nums = [1,2,3,4]

        answer:
        [2*3*4, 1*3*4, 1*2*4, 1*2*3]
        → [24,12,8,6]


        🔴 Why NOT use Division?

        Idea:
        total_product = product of all elements
        answer[i] = total_product / nums[i]

        ❌ Problems:
        - Division is NOT allowed
        - Fails when array contains 0


        🔴 Brute Force:

        Idea:
        - For each index → multiply all other elements

        ❌ Time Complexity:
        - O(n^2) → too slow


        🟢 Optimized Approach (Prefix + Suffix) — BEST

        💡 Key Idea:
        For each index:
        answer[i] = (product of left elements) * (product of right elements)

        Instead of recomputing:
        - Store prefix products
        - Store suffix products


        🔁 Example:
        nums = [1,2,3,4]

        Prefix:
        [1, 1, 2, 6]
        (product before index)

        Suffix:
        [24,12,4,1]
        (product after index)

        Multiply:
        answer = [24,12,8,6]


        🔥 Space Optimization (IMPORTANT):

        Instead of using 2 arrays:
        - Use only ONE result array
        - First pass → store prefix
        - Second pass → multiply suffix on the fly

        👉 This gives O(1) extra space


        ⚙️ Workflow:

        Step 1:
        Build prefix in result

        Step 2:
        Traverse from right and maintain suffix variable

        Step 3:
        Multiply suffix with result[i]


        ⚡ Complexity:
        - Time: O(n) ✅
        - Space: O(1) ✅ (output not counted)
        """


        # 🔹 Step 1: Create result array
        n = len(nums)
        result = [1] * n

        # 🔹 Step 2: Build prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # 🔹 Step 3: Multiply with suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
