# Problem: Pacific Atlantic Water Flow
# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Brute Force (start DFS from every cell):
        #    ❌ For each cell, try reaching both oceans → O((m*n)*(m*n)) → too slow
        #
        # 2. Forward Simulation (water flow from cell to ocean):
        #    ❌ Hard to track + repeated work
        #
        # 👉 Key Insight:
        #    Instead of going FROM cell → ocean
        #    Reverse thinking: go FROM ocean → cells
        #
        # 3. BFS vs DFS:
        #    Both valid
        #    👉 DFS is simpler to implement recursively

        # -------------------- CORE IDEA --------------------
        # Water flows from high → low
        #
        # Reverse:
        # Start from oceans and go to cells where:
        # neighbor height >= current height
        #
        # Find:
        # - Cells reachable from Pacific
        # - Cells reachable from Atlantic
        #
        # Answer = Intersection of both

        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        # -------------------- DFS FUNCTION --------------------
        def dfs(r, c, visited):
            visited.add((r, c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check bounds and height condition
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):
                    
                    dfs(nr, nc, visited)

        # -------------------- START FROM OCEANS --------------------
        # Pacific → top row + left column
        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic → bottom row + right column
        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        # -------------------- FIND INTERSECTION --------------------
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Instead of checking each cell → ocean,
# we flood from oceans inward (reverse flow)
#
# Pacific reach → cells that can flow INTO Pacific
# Atlantic reach → cells that can flow INTO Atlantic
#
# Final = cells reachable from BOTH

# -------------------- TIME COMPLEXITY --------------------
# O(m * n)
# Each cell visited at most twice (Pacific + Atlantic)

# -------------------- SPACE COMPLEXITY --------------------
# O(m * n)
# - visited sets
# - recursion stack
