# Problem #25: Binary Tree Level Order Traversal

# Link:https://leetcode.com/problems/binary-tree-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        """
        🧠 Problem (Simple Words):

        - Traverse tree level by level
        - Return values in list of lists

        Example:
                3
               / \
              9  20
                 / \
                15  7

        Output:
        [[3], [9,20], [15,7]]


        🔴 DFS not ideal here:
        - Harder to track levels


        🟢 Best Approach: BFS (Queue)

        💡 Core Idea:

        - Use queue
        - Process nodes level by level


        🔁 Step-by-step:

        queue = [root]

        while queue not empty:
            process all nodes in current level
            add children to queue


        💡 Key Insight:
        - Queue naturally processes level-wise


        ⚡ Complexity:
        - Time: O(n)
        - Space: O(n)
        """


        if not root:
            return []

        from collections import deque
        queue = deque([root])

        result = []

        while queue:

            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
