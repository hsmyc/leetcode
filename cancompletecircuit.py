# 4.2.24

class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        total = 0
        tank = 0
        start = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0
        return start if total + tank >= 0 else -1


print(Solution().canCompleteCircuit([3, 1, 8, 4], [1, 4, 5, 6]))
