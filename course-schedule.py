# Problem: Course Schedule
# Link: https://leetcode.com/problems/course-schedule/

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Brute Force:
        #    ❌ Try all possible course orders → factorial complexity → impossible
        #
        # 2. Simple DFS without tracking states:
        #    ❌ Cannot detect cycles properly → may lead to infinite recursion
        #
        # 3. BFS (Kahn’s Algorithm):
        #    ✅ Valid approach (Topological Sort using indegree)
        #    But slightly more setup (queue + indegree array)
        #
        # 👉 Best intuitive approach:
        #    DFS with cycle detection using 3 states

        # -------------------- CORE IDEA --------------------
        # This is a Directed Graph problem
        # We need to check if a cycle exists
        #
        # If cycle exists → ❌ cannot finish courses
        # If no cycle → ✅ possible

        # -------------------- GRAPH BUILD --------------------
        from collections import defaultdict
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # -------------------- VISITED STATES --------------------
        # 0 = unvisited
        # 1 = visiting (currently in recursion stack)
        # 2 = visited (already checked, no cycle)
        state = [0] * numCourses

        # -------------------- DFS FUNCTION --------------------
        def dfs(course):
            # If currently visiting → cycle detected
            if state[course] == 1:
                return False

            # If already processed → no need to check again
            if state[course] == 2:
                return True

            # Mark as visiting
            state[course] = 1

            # Visit all neighbors
            for nei in graph[course]:
                if not dfs(nei):
                    return False

            # Mark as fully processed
            state[course] = 2
            return True

        # -------------------- MAIN LOOP --------------------
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Example:
# [1,0] → 0 → 1 (valid)
#
# [1,0], [0,1] → 0 → 1 → 0 (cycle ❌)
#
# While DFS:
# If we revisit a node in the SAME recursion path → cycle

# -------------------- TIME COMPLEXITY --------------------
# O(V + E)
# V = courses, E = prerequisites

# -------------------- SPACE COMPLEXITY --------------------
# O(V + E)
# - Graph storage
# - Recursion stack
