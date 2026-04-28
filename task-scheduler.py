# Problem: Task Scheduler
# Link: https://leetcode.com/problems/task-scheduler/

from collections import Counter
import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Brute Force Simulation:
        #    ❌ Try all permutations → impossible
        #
        # 2. Simple Greedy without structure:
        #    ❌ Hard to track cooldown correctly
        #
        # 👉 BEST APPROACHES:
        # ✅ Mathematical Formula (most optimal)
        # ✅ OR Heap + Queue simulation (more intuitive)
        #
        # Here we use:
        # ✅ Max Heap + Queue (classic heap pattern)

        # -------------------- CORE IDEA --------------------
        # Always execute the task with highest remaining frequency
        # Use max heap for picking most frequent task
        #
        # After executing a task:
        # → it goes into cooldown queue for n time
        #
        # Queue stores: (available_time, remaining_count)

        # -------------------- STEP 1: COUNT --------------------
        freq = Counter(tasks)

        # -------------------- STEP 2: MAX HEAP --------------------
        # Python has min heap → use negative values
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        # -------------------- STEP 3: COOLDOWN QUEUE --------------------
        from collections import deque
        cooldown = deque()  # (time_available, count)

        time = 0

        # -------------------- MAIN LOOP --------------------
        while max_heap or cooldown:
            time += 1

            if max_heap:
                count = 1 + heapq.heappop(max_heap)  # reduce count

                if count != 0:
                    # Put into cooldown
                    cooldown.append((time + n, count))

            # Check if any task finished cooldown
            if cooldown and cooldown[0][0] == time:
                _, ready_count = cooldown.popleft()
                heapq.heappush(max_heap, ready_count)

        return time


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Example:
# tasks = [A,A,A,B,B,B], n = 2
#
# Step-by-step:
# A B idle A B idle A B
#
# Always pick most frequent task first
# Then enforce cooldown using queue

# -------------------- TIME COMPLEXITY --------------------
# O(n log 26) ≈ O(n)
# (since max 26 tasks)

# -------------------- SPACE COMPLEXITY --------------------
# O(1)
# (fixed size due to only 26 uppercase letters)
