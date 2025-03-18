class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #if sol exists
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0 #position
        #greedy approach
        for i in range(len(gas)):
            total += (gas[i]-cost[i])

            if total < 0:
                total = 0 #reset total
                res = i + 1 #start position such that total never went below zero
        return res