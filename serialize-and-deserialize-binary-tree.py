# Problem: Serialize and Deserialize Binary Tree
# Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # -------------------- WHY NOT OTHER TECHNIQUES --------------------
    # 1. Inorder Traversal:
    #    ❌ Not sufficient alone → cannot reconstruct unique tree
    #
    # 2. Only storing values (no nulls):
    #    ❌ Structure lost → cannot rebuild tree correctly
    #
    # 3. Level Order (BFS):
    #    ✅ Works, but requires queue handling and careful null placement
    #
    # 👉 BEST APPROACH:
    # ✅ Preorder DFS + Null markers
    #
    # Why?
    # - Preorder gives root → left → right
    # - With "null" markers → structure is preserved
    # - Simple recursive implementation

    # -------------------- SERIALIZATION --------------------
    def serialize(self, root):
        """Encodes a tree to a single string."""
        
        # Use preorder traversal
        result = []

        def dfs(node):
            if not node:
                result.append("N")  # Null marker
                return
            
            # Store current node
            result.append(str(node.val))
            
            # Traverse left and right
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        # Join into single string
        return ",".join(result)

    # -------------------- DESERIALIZATION --------------------
    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        
        # Split data into list
        values = data.split(",")
        self.index = 0

        def dfs():
            # If null marker → return None
            if values[self.index] == "N":
                self.index += 1
                return None
            
            # Create node
            node = TreeNode(int(values[self.index]))
            self.index += 1

            # Build left and right subtree
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Tree:
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# Serialize (Preorder):
# 1,2,N,N,3,4,N,N,5,N,N
#
# Deserialize:
# Read sequentially and rebuild using recursion

# -------------------- TIME COMPLEXITY --------------------
# Serialize: O(n)
# Deserialize: O(n)

# -------------------- SPACE COMPLEXITY --------------------
# O(n)
# - recursion stack
# - output storage
