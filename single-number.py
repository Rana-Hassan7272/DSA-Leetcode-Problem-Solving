# Problem #11: Single Number

# Link:https://leetcode.com/problems/single-number


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        🧠 Problem (Simple Words):

        - Every element appears twice
        - Only ONE element appears once
        👉 Find that single element

        Example:
        [2,2,1] → answer = 1


        🔴 Why NOT Brute Force?

        Idea:
        - Count frequency for each element

        ❌ Problem:
        - Time: O(n^2)
        - Too slow


        🔴 Why NOT HashMap?

        Idea:
        - Store counts in dictionary

        ❌ Problem:
        - Time: O(n) ✅
        - Space: O(n) ❌ (not allowed, need O(1))


        🟢 Best Approach: XOR (Bit Manipulation)

        💡 Why XOR works (VERY IMPORTANT):

        XOR Rules:
        1. a ^ a = 0
        2. a ^ 0 = a
        3. XOR is commutative:
           a ^ b ^ a = b

        👉 Meaning:
        - Duplicate numbers cancel out
        - Only unique number remains


        🔁 Example:

        nums = [4,1,2,1,2]

        Step-by-step:
        result = 0

        0 ^ 4 = 4
        4 ^ 1 = 5
        5 ^ 2 = 7
        7 ^ 1 = 6
        6 ^ 2 = 4

        👉 Final result = 4


        💡 Key Insight:
        - All duplicates disappear
        - Only single number stays


        ⚡ Complexity:
        - Time: O(n) ✅
        - Space: O(1) ✅ (perfect match)


        🔥 Why this is BEST:

        - No extra memory
        - One pass
        - Uses mathematical property
        """


        # 🔹 Initialize result
        result = 0

        # 🔹 XOR all elements
        for num in nums:
            result ^= num

        return result
