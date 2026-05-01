# Problem: Set Matrix Zeroes
# Link: https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Brute Force (update immediately):
        #    ❌ Wrong — newly set zeros propagate incorrectly
        #
        # 2. Extra row/col arrays (O(m+n)):
        #    ❌ Works but not constant space
        #
        # 👉 BEST APPROACH:
        # ✅ Use first row & first column as markers (O(1) space)
        #
        # Why?
        # - We reuse matrix itself to track which row/col to zero
        # - Achieves in-place requirement

        rows, cols = len(matrix), len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # -------------------- CHECK FIRST ROW --------------------
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        # -------------------- CHECK FIRST COLUMN --------------------
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True
                break

        # -------------------- MARK USING FIRST ROW/COL --------------------
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # -------------------- APPLY MARKS --------------------
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # -------------------- HANDLE FIRST ROW --------------------
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # -------------------- HANDLE FIRST COLUMN --------------------
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0


# -------------------- HOW IT WORKS --------------------
# Step 1: Use first row & column as flags
# Step 2: Mark rows/cols that should become zero
# Step 3: Update matrix based on markers
# Step 4: Finally fix first row/column

# -------------------- KEY INSIGHT --------------------
# Instead of extra arrays:
# → reuse matrix edges as storage

# -------------------- TIME COMPLEXITY --------------------
# O(m * n)

# -------------------- SPACE COMPLEXITY --------------------
# O(1)
