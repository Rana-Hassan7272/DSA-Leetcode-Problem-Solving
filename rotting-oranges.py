# Problem: Rotting Oranges
# Link: https://leetcode.com/problems/rotting-oranges/

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. DFS:
        #    ❌ Cannot correctly track "minimum time"
        #    ❌ Does not simulate level-by-level spread
        #
        # 👉 BEST APPROACH:
        # ✅ Multi-Source BFS
        #
        # Why?
        # - All rotten oranges spread simultaneously
        # - BFS naturally models "time = levels"
        # - Each level = 1 minute

        from collections import deque

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # -------------------- INITIAL STATE --------------------
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))   # rotten
                elif grid[r][c] == 1:
                    fresh += 1             # count fresh

        # If no fresh oranges
        if fresh == 0:
            return 0

        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # -------------------- BFS --------------------
        while queue:
            size = len(queue)
            spread = False   # track if anything rotted this minute

            for _ in range(size):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
                        spread = True

            if spread:
                minutes += 1

        # -------------------- RESULT --------------------
        return minutes if fresh == 0 else -1


# -------------------- HOW IT WORKS --------------------
# Each BFS level = 1 minute
#
# Start from ALL rotten oranges
# Spread outward simultaneously

# -------------------- KEY INSIGHT --------------------
# Multi-source BFS:
# - Instead of 1 start node → many start nodes
# - All spread together

# -------------------- TIME COMPLEXITY --------------------
# O(m * n)

# -------------------- SPACE COMPLEXITY --------------------
# O(m * n) (queue)
