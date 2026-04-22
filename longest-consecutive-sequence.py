# Problem #10: Longest Consecutive Sequence

# Link:https://leetcode.com/problems/longest-consecutive-sequence/



class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        🧠 Problem (Simple Words):

        Given an unsorted array,
        find the length of the longest sequence of consecutive numbers.

        👉 Order in array does NOT matter
        👉 Sequence must be consecutive numbers

        Example:
        [100,4,200,1,3,2]
        → sequence: [1,2,3,4]
        → length = 4


        🔴 Why NOT Sorting?

        Idea:
        - Sort array, then count consecutive

        ❌ Problem:
        - Time Complexity = O(n log n)
        - Question requires O(n)
        → So sorting is NOT allowed


        🔴 Brute Force:

        Idea:
        - For each number, keep checking next numbers (num+1, num+2...)

        ❌ Problem:
        - Can become O(n^2) in worst case


        🟢 Optimized Approach (HashSet) — BEST

        💡 Key Idea:
        - Store all numbers in a set → O(1) lookup
        - Only start counting from the BEGINNING of a sequence

        👉 Important Trick:
        A number is start of sequence IF:
            num - 1 NOT in set

        This avoids unnecessary work


        🔁 Step-by-step:

        nums = [100,4,200,1,3,2]

        Set = {1,2,3,4,100,200}

        Check:
        1 → (1-1=0 not in set) → start sequence
            → 1,2,3,4 → length = 4

        2 → (2-1=1 in set) → skip ❌
        3 → skip ❌
        4 → skip ❌

        100 → start → length = 1
        200 → start → length = 1


        💡 Key Insight:
        - Only start from "sequence starters"
        - Each number visited once → O(n)


        ⚡ Complexity:
        - Time: O(n) ✅
        - Space: O(n)
        """


        # 🔹 Convert list to set for O(1) lookups
        num_set = set(nums)

        longest = 0

        # 🔹 Iterate through numbers
        for num in num_set:

            # 🔹 Check if it's the start of a sequence
            if num - 1 not in num_set:

                current = num
                length = 1

                # 🔹 Expand the sequence
                while current + 1 in num_set:
                    current += 1
                    length += 1

                # 🔹 Update longest length
                if length > longest:
                    longest = length

        return longest
