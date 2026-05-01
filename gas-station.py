# Problem: Gas Station
# Link: https://leetcode.com/problems/gas-station/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Brute Force (try every start):
        #    ❌ O(n^2) → too slow (n up to 1e5)
        #
        # 2. Simulation with restart each time:
        #    ❌ Still quadratic in worst case
        #
        # 👉 BEST APPROACH:
        # ✅ Greedy + Prefix Insight
        #
        # Why?
        # - If total gas < total cost → impossible
        # - If starting at i fails → all stations between start and i are invalid
        # - So we can skip them (VERY IMPORTANT OPTIMIZATION)

        total = 0     # total gas balance
        curr = 0      # current running balance
        start = 0     # candidate starting index

        for i in range(len(gas)):
            gain = gas[i] - cost[i]

            total += gain
            curr += gain

            # -------------------- KEY GREEDY STEP --------------------
            if curr < 0:
                # cannot start from current 'start'
                # move start to next position
                start = i + 1
                curr = 0

        # -------------------- FINAL CHECK --------------------
        return start if total >= 0 else -1


# -------------------- HOW IT WORKS --------------------
# Example:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
#
# At index 0 → fail → skip
# At index 1 → fail → skip
# Eventually start at 3

# -------------------- KEY INSIGHT --------------------
# If you fail at i:
# → No point starting from any station between start and i

# -------------------- TIME COMPLEXITY --------------------
# O(n)

# -------------------- SPACE COMPLEXITY --------------------
# O(1)
