# Problem #17: Move Zeroes

# Link:https://leetcode.com/problems/move-zeroes/


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """

        """
        🧠 Problem (Simple Words):

        - Move all 0's to the end
        - Keep order of non-zero elements SAME
        - Do it IN-PLACE (no extra array)

        Example:
        [0,1,0,3,12] → [1,3,12,0,0]


        🔴 Brute Force:

        Idea:
        - Create new array
        - Copy non-zero elements
        - Add zeros at end

        ❌ Problem:
        - Uses extra space O(n)
        - Not allowed


        🟢 Optimized Approach (Two Pointers) — BEST

        💡 Core Idea:

        - Maintain a pointer `pos` → where next non-zero should go
        - Traverse array:
            → If element != 0:
                swap with position `pos`
                increment pos


        🔁 Step-by-step:

        nums = [0,1,0,3,12]

        pos = 0

        i=0 → 0 → skip
        i=1 → 1 → swap(nums[1], nums[0]) → [1,0,0,3,12]
        pos=1

        i=2 → 0 → skip
        i=3 → 3 → swap(nums[3], nums[1]) → [1,3,0,0,12]
        pos=2

        i=4 → 12 → swap(nums[4], nums[2]) → [1,3,12,0,0]


        💡 Key Insight:
        - Keep pushing non-zero forward
        - Zeros automatically go to end


        ⚡ Complexity:
        - Time: O(n) ✅
        - Space: O(1) ✅


        🔥 Follow-up (Minimize operations):
        - Only swap when needed (nums[i] != 0)
        - Avoid unnecessary writes
        """


        pos = 0  # position for next non-zero

        for i in range(len(nums)):
            if nums[i] != 0:
                # swap only when needed
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
