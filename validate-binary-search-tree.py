# Problem #26: Validate Binary Search Tree

# Link:https://leetcode.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        """
        🧠 Problem (Simple Words):

        - Check if a binary tree is a VALID BST

        👉 BST rules:
        - Left subtree < node
        - Right subtree > node
        - This must hold for ALL nodes (not just immediate children)


        🔴 Common Wrong Approach:

        ❌ Only checking:
            node.left < node < node.right

        👉 Why wrong?

        Example:
                5
               / \
              1   4
                 / \
                3   6

        Here:
        - 4 < 5 ❌ (violates BST)
        - But local checks may miss this


        🟢 Correct Approach: Range Validation (DFS)

        💡 Core Idea:

        Each node must lie within a valid range

        Initially:
        root → (-∞, +∞)

        For left child:
        range = (min, node.val)

        For right child:
        range = (node.val, max)


        🔁 Recursive Rule:

        isValid(node, low, high):

            if node is None:
                return True

            if node.val <= low OR node.val >= high:
                return False

            return:
                isValid(left, low, node.val)
                AND
                isValid(right, node.val, high)


        🔁 Example:

        root = 5

        left subtree range: (-inf, 5)
        right subtree range: (5, inf)


        💡 Key Insight:
        - Every node carries its own valid range
        - Not just parent comparison


        ⚡ Complexity:
        - Time: O(n) ✅
        - Space: O(h) recursion stack
        """


        def helper(node, low, high):
            if not node:
                return True

            # 🔹 Check BST condition
            if node.val <= low or node.val >= high:
                return False

            # 🔹 Recurse left and right
            return (helper(node.left, low, node.val) and
                    helper(node.right, node.val, high))

        return helper(root, float('-inf'), float('inf'))
