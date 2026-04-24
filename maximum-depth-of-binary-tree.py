# Problem #24: Maximum Depth of Binary Tree

# Link:https://leetcode.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        """
        🧠 Problem (Simple Words):

        - Given a binary tree
        - Find the longest path from root to any leaf
        - Count number of nodes in that path

        👉 That count = maximum depth


        🔴 Brute Force Thinking:

        - Try all paths → find longest

        ❌ Not practical


        🟢 Best Approach: Recursion (DFS)

        💡 Core Idea:

        - Depth of a node =
            1 + max(depth of left subtree, depth of right subtree)

        👉 Because:
        - You go down both sides
        - Take the longer one


        🔁 Recursive Formula:

        depth(node):
            if node is null:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            return 1 + max(left, right)


        🔁 Example:

                3
               / \
              9  20
                /  \
               15   7

        depth(3):
            = 1 + max(depth(9), depth(20))
            = 1 + max(1, 2)
            = 3


        💡 Why recursion works best?

        - Tree is naturally recursive
        - Solve smaller subtrees first


        ⚡ Complexity:
        - Time: O(n) ✅ (visit each node once)
        - Space: O(h) recursion stack
        """


        # 🔹 Base case
        if root is None:
            return 0

        # 🔹 Recursive case
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
