# Problem: Binary Tree Maximum Path Sum
# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Brute Force (try all paths):
        #    ❌ Exponential → too slow
        #
        # 2. Simple DFS summing all paths:
        #    ❌ Cannot handle "split path" (left + root + right)
        #
        # 👉 Key Challenge:
        # Path can:
        # - Start and end anywhere
        # - Include BOTH left and right child (split path)
        #
        # 👉 BEST APPROACH:
        # ✅ DFS with "return max gain" + global max

        # -------------------- CORE IDEA --------------------
        # At each node:
        # 1. Compute max gain from left and right
        # 2. Ignore negative paths (use max(0, child))
        # 3. Calculate "split path" = left + node + right
        # 4. Update global maximum
        # 5. Return max gain (node + max(left, right))

        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Get max gain from left and right (ignore negatives)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Current path including both sides
            current_path = node.val + left_gain + right_gain

            # Update global max
            self.max_sum = max(self.max_sum, current_path)

            # Return max gain to parent (ONLY one side allowed)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Example:
#       20
#      /  \
#    15    7
#
# At node 20:
# left_gain = 15
# right_gain = 7
#
# Path = 15 + 20 + 7 = 42 (this is answer)
#
# BUT when returning to parent:
# can only return ONE path → max(15,7) + 20

# -------------------- IMPORTANT INSIGHT --------------------
# Two different concepts:
#
# 1. "Return value" → single path (for parent)
# 2. "Global max" → can include both children (split path)

# -------------------- TIME COMPLEXITY --------------------
# O(n)
# Each node visited once

# -------------------- SPACE COMPLEXITY --------------------
# O(h)
# h = height of tree (recursion stack)
# worst case O(n)
