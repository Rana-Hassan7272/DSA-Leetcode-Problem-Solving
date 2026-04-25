# Problem: Clone Graph
# Link: https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Simple Copy (without map):
        #    ❌ Fails because graph has cycles → infinite loop
        #    ❌ Also duplicates nodes multiple times
        #
        # 2. Iterative BFS without visited map:
        #    ❌ Same issue → cycles cause repeated processing
        #
        # 👉 Key Insight:
        #    We MUST store already cloned nodes (visited map)
        #
        # 3. DFS vs BFS:
        #    Both work fine
        #    👉 DFS is simpler to implement recursively
        #
        # So we use:
        # ✅ DFS + HashMap (original → clone)

        # -------------------- EDGE CASE --------------------
        if not node:
            return None

        # -------------------- HASHMAP --------------------
        # Maps original node → cloned node
        old_to_new = {}

        # -------------------- DFS FUNCTION --------------------
        def dfs(curr):
            # If already cloned, return it
            if curr in old_to_new:
                return old_to_new[curr]

            # Create clone node
            clone = Node(curr.val)
            old_to_new[curr] = clone  # store before recursion (important for cycles)

            # Clone neighbors
            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        # -------------------- MAIN CALL --------------------
        return dfs(node)


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Graph example:
# 1 -- 2
# |    |
# 4 -- 3
#
# Step 1: Start from node 1 → create clone(1)
# Step 2: Visit neighbors (2, 4)
# Step 3: For each neighbor → recursively clone
# Step 4: Use hashmap to avoid re-cloning same node
#
# 👉 Important:
# We store node in hashmap BEFORE exploring neighbors
# This prevents infinite loops in cyclic graphs

# -------------------- TIME COMPLEXITY --------------------
# O(V + E)
# V = number of nodes
# E = number of edges

# -------------------- SPACE COMPLEXITY --------------------
# O(V)
# - HashMap storage
# - Recursion stack (worst case)
