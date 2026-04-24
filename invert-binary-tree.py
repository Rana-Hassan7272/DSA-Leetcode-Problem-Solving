# Problem #23: Invert Binary Tree

# Link: https://leetcode.com/problems/invert-binary-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        """
        🧠 Problem (Simple Words):

        - Given a binary tree
        - Swap left and right child of EVERY node

        👉 Basically mirror the tree


        🔴 Brute Force:

        - No real brute force here, but iterative swapping with extra storage
        - Not clean


        🟢 Best Approach: Recursion (DFS)

        💡 Core Idea:

        For every node:
        → swap left and right
        → recursively do same for children


        🔁 Step-by-step:

        Node:
            4
           / \
          2   7

        After swap:
            4
           / \
          7   2


        🔁 Recursive Thinking:

        invert(node):
            swap(node.left, node.right)
            invert(node.left)
            invert(node.right)


        💡 Why recursion works best?

        - Tree naturally recursive structure
        - Visit every node once


        ⚡ Complexity:
        - Time: O(n) ✅ (visit each node once)
        - Space: O(h) recursion stack
          (h = height of tree)
        """


        # 🔹 Base case
        if root is None:
            return None

        # 🔹 Swap children
        root.left, root.right = root.right, root.left

        # 🔹 Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
