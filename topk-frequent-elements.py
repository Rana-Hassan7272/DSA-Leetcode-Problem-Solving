# Problem #6: Top K Frequent Elements

# Link:https://leetcode.com/problems/top-k-frequent-elements


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        """
        🧠 What is the problem (in simple words)?

        You are given:
        - An array of numbers
        - A number k

        You need to:
        - Return the k numbers that appear MOST frequently

        📌 Example:
        nums = [1,1,1,2,2,3], k = 2

        Frequencies:
        1 → 3 times
        2 → 2 times
        3 → 1 time

        👉 Answer: [1, 2]


        🔑 Core Idea:

        This problem has 2 main steps:

        Step 1:
        → Count frequency of each number

        Step 2:
        → Get top k highest frequency elements


        🔴 Why NOT sorting?

        If we sort based on frequency:
        → Time Complexity = O(n log n) ❌

        But problem requires:
        → Better than O(n log n)

        So sorting is NOT optimal


        🚀 Optimized Approach: HashMap + Bucket Sort

        💡 Mental Model:

        Instead of sorting, we group numbers by frequency

        Frequency → Numbers
        1 → [3]
        2 → [2]
        3 → [1]


        ⚙️ Step-by-step:

        ✅ Step 1: Count frequencies

        nums = [1,1,1,2,2,3]
        → {1:3, 2:2, 3:1}


        ✅ Step 2: Create buckets

        👉 Index = frequency
        👉 Value = list of numbers

        Example:
        index:   0   1   2   3
        bucket: [ ] [3] [2] [1]


        ✅ Step 3: Traverse from back

        Start from highest frequency:

        freq = 3 → [1]
        freq = 2 → [2]

        Stop when k elements collected

        👉 Answer = [1, 2]


        ⚡ Complexity:
        Time: O(n) ✅
        Space: O(n)


        ⚖️ Alternative: Heap (Min Heap)

        Idea:
        - Keep heap of size k
        - Insert based on frequency

        Complexity:
        - O(n log k) ✅

        🤔 When to use Heap?
        - When data is streaming
        - When k is very small


        🥇 Final Strategy (Interview):

        Say:
        - First count frequencies using hashmap
        - Then use bucket sort to avoid sorting
        - Traverse from highest frequency to get k elements
        """


        # 🔹 Step 1: Count frequencies
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1


        # 🔹 Step 2: Create buckets (index = frequency)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            bucket[freq].append(num)


        # 🔹 Step 3: Traverse from highest frequency
        result = []

        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
