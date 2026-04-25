#Problem:Number of Islands

#Link: https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Brute Force:
        #    Checking every possible group separately → very complex and redundant.
        #
        # 2. Union-Find (Disjoint Set):
        #    Works, but requires extra parent/rank arrays → more complex to implement.
        #
        # 3. BFS vs DFS:
        #    Both are valid, but DFS is simpler to code using recursion.
        #
        # 👉 So we use DFS (Flood Fill) because:
        #    - Simple implementation
        #    - Efficient traversal
        #    - No extra data structures needed (except recursion stack)

        # -------------------- CORE IDEA --------------------
        # Whenever we see '1' (land), it means a new island.
        # Then we "sink" the whole island using DFS by converting all connected '1's into '0'.
        # This prevents counting the same island multiple times.

        # -------------------- DFS FUNCTION --------------------
        def dfs(r, c):
            # Boundary + water check
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
                return
            
            # Mark current land as visited (sink it)
            grid[r][c] = '0'

            # Explore all 4 directions (up, down, left, right)
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # -------------------- MAIN LOGIC --------------------
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        for r in range(rows):
            for c in range(cols):
                # If we find land, it's a new island
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c)  # remove entire island

        return island_count


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Example:
# 1 1 0
# 1 0 0
# 0 0 1
#
# Step 1: find first '1' → island_count = 1
# DFS will convert all connected '1's → becomes 0
#
# Step 2: continue scanning → find another '1'
# island_count = 2
#
# Final answer = 2

# -------------------- TIME COMPLEXITY --------------------
# O(m * n)
# Each cell is visited exactly once

# -------------------- SPACE COMPLEXITY --------------------
# O(m * n) in worst case (recursion stack if all are '1')
# Average case is much lower
