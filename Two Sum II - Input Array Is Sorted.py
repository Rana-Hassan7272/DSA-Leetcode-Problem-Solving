# Problem #4: Two Sum II - Input Array Is Sorted

# Link:https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        🔴 Brute Force Approach:

        Idea:
        - Try all pairs using two loops

        ❌ Problem:
        - Time Complexity: O(n^2)
        - Too slow for n up to 3 * 10^4


        🟡 Hash Map Approach (NOT suitable here):

        Idea:
        - Same as Two Sum (unsorted version)

        ❌ Problem:
        - Uses extra space O(n)
        - BUT question says: "must use constant extra space"
        - So hashmap is NOT allowed here


        🟢 Optimized Approach (Two Pointers - BEST):

        💡 Why this works:
        - Array is already SORTED
        - We can use left + right pointers

        🔁 Idea:
        - Start:
            left = 0
            right = n - 1

        - While left < right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                return answer

            if sum < target:
                move left forward (need bigger value)

            if sum > target:
                move right backward (need smaller value)


        🔁 Step-by-step:
        numbers = [2,7,11,15], target = 9

        left=0 (2), right=3 (15) → sum=17 > 9 → move right
        left=0 (2), right=2 (11) → sum=13 > 9 → move right
        left=0 (2), right=1 (7)  → sum=9  → FOUND


        💡 Key Insight:
        - Sorted array allows directional movement
        - No need to check all pairs

        ⚡ Complexity:
        - Time: O(n)
        - Space: O(1) ✅ (constant space as required)
        """

        # 🔹 Initialize two pointers
        left = 0
        right = len(numbers) - 1

        # 🔹 Traverse until pointers meet
        while left < right:

            current_sum = numbers[left] + numbers[right]

            # 🔹 If target found → return 1-based indices
            if current_sum == target:
                return [left + 1, right + 1]

            # 🔹 If sum is too small → move left pointer
            elif current_sum < target:
                left += 1

            # 🔹 If sum is too large → move right pointer
            else:
                right -= 1

        return []
