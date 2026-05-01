# Problem: Parallel Courses II
# Link: https://leetcode.com/problems/parallel-courses-ii/

class Solution(object):
    def minNumberOfSemesters(self, n, relations, k):
        """
        :type n: int
        :type relations: List[List[int]]
        :type k: int
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Simple BFS / Topological Sort:
        #    ❌ Fails because we can take ONLY k courses per semester
        #    ❌ Need to choose optimal subset each time
        #
        # 👉 BEST APPROACH:
        # ✅ Bitmask + BFS (State Compression)
        #
        # Why?
        # - n <= 15 → small enough for bitmask (2^n states)
        # - Each state = set of completed courses
        # - BFS ensures minimum semesters

        from collections import deque

        # -------------------- BUILD PREREQUISITES MASK --------------------
        prereq = [0] * n
        for u, v in relations:
            u -= 1
            v -= 1
            prereq[v] |= (1 << u)

        # -------------------- BFS --------------------
        full_mask = (1 << n) - 1
        queue = deque([(0, 0)])  # (mask, semesters)
        visited = set([0])

        while queue:
            mask, steps = queue.popleft()

            # all courses taken
            if mask == full_mask:
                return steps

            # -------------------- FIND AVAILABLE COURSES --------------------
            available = []
            for i in range(n):
                # not taken yet & prerequisites satisfied
                if not (mask & (1 << i)) and (prereq[i] & mask) == prereq[i]:
                    available.append(i)

            # -------------------- GENERATE COMBINATIONS --------------------
            # If <= k → take all
            if len(available) <= k:
                new_mask = mask
                for i in available:
                    new_mask |= (1 << i)

                if new_mask not in visited:
                    visited.add(new_mask)
                    queue.append((new_mask, steps + 1))

            else:
                # choose k courses among available
                from itertools import combinations

                for combo in combinations(available, k):
                    new_mask = mask
                    for i in combo:
                        new_mask |= (1 << i)

                    if new_mask not in visited:
                        visited.add(new_mask)
                        queue.append((new_mask, steps + 1))


# -------------------- HOW IT WORKS --------------------
# mask = bit representation of completed courses
#
# Example (n=4):
# mask = 0101 → courses 0 and 2 completed
#
# BFS explores all possibilities level by level
# Each level = 1 semester

# -------------------- KEY INSIGHT --------------------
# State = completed courses
# Transition = take up to k valid courses

# -------------------- TIME COMPLEXITY --------------------
# O(2^n * n + combinations)
# manageable since n <= 15

# -------------------- SPACE COMPLEXITY --------------------
# O(2^n)
