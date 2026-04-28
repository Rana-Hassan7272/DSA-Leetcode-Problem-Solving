# Problem: Sliding Window Median
# Link: https://leetcode.com/problems/sliding-window-median/

import heapq
from collections import defaultdict

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """

        # -------------------- WHY THIS APPROACH --------------------
        # Two Heaps + Lazy Deletion
        # - Max heap (small) → left half
        # - Min heap (large) → right half
        # - delayed → handles removals

        self.small = []   # max heap (negative values)
        self.large = []   # min heap
        self.delayed = defaultdict(int)

        self.small_size = 0
        self.large_size = 0

        # -------------------- HELPERS --------------------
        def prune(heap):
            while heap:
                num = -heap[0] if heap is self.small else heap[0]
                if self.delayed[num]:
                    self.delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            # balance sizes
            if self.small_size > self.large_size + 1:
                val = -heapq.heappop(self.small)
                heapq.heappush(self.large, val)
                self.small_size -= 1
                self.large_size += 1
                prune(self.small)

            elif self.small_size < self.large_size:
                val = heapq.heappop(self.large)
                heapq.heappush(self.small, -val)
                self.large_size -= 1
                self.small_size += 1
                prune(self.large)

        def add(num):
            if not self.small or num <= -self.small[0]:
                heapq.heappush(self.small, -num)
                self.small_size += 1
            else:
                heapq.heappush(self.large, num)
                self.large_size += 1
            balance()

        def remove(num):
            self.delayed[num] += 1

            if num <= -self.small[0]:
                self.small_size -= 1
                if num == -self.small[0]:
                    prune(self.small)
            else:
                self.large_size -= 1
                if self.large and num == self.large[0]:
                    prune(self.large)

            balance()

        def get_median():
            if k % 2:
                return float(-self.small[0])
            return (-self.small[0] + self.large[0]) / 2.0

        # -------------------- MAIN --------------------
        result = []

        for i in range(len(nums)):
            add(nums[i])

            if i >= k:
                remove(nums[i - k])

            if i >= k - 1:
                result.append(get_median())

        return result


# -------------------- TIME --------------------
# O(n log k)

# -------------------- SPACE --------------------
# O(n)
