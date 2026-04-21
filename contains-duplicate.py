# Problem #2: Contains Duplicate

# Link:https://leetcode.com/problems/contains-duplicate


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        🔴 Brute Force Approach:

        Idea:
        - Compare every element with every other element
        - Use two loops (i, j)

        Example:
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True

        ❌ Problem:
        - Outer loop → n
        - Inner loop → n
        - Total Time Complexity → O(n^2)

        👉 Not efficient for large inputs (n up to 10^5)


        🟢 Optimized Approach (Hashing / Set):

        Idea:
        - Use a set to store elements we've already seen
        - While traversing:
            → If element already exists in set → duplicate found
            → Else → add it to set

        🔁 Step-by-step:
        nums = [1,2,3,1]

        Step 1: seen = {}
        Step 2: add 1 → {1}
        Step 3: add 2 → {1,2}
        Step 4: add 3 → {1,2,3}
        Step 5: see 1 again → already in set → return True

        💡 Key Insight:
        - Set lookup is O(1)
        - So total complexity becomes O(n)


        ⚡ Complexity:
        - Time: O(n)
        - Space: O(n)
        """

        # 🔹 Create an empty set
        seen = set()

        # 🔹 Traverse the list
        for num in nums:

            # 🔹 If already seen → duplicate found
            if num in seen:
                return True

            # 🔹 Otherwise add to set
            seen.add(num)

        # 🔹 No duplicates found
        return False
