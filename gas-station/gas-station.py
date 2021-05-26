class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        cycled = False
        for j in range(0,l):
            bal = gas[j]
            idx, prev = j, 0
            for i in range(j+1, l+j+1):
                prev = idx
                idx = i % l
                # print(prev, idx, cost[prev], end=' ')
                bal = bal - cost[prev]
                # print(f'{idx}({bal})', end=' ')
                if bal < 0:
                    break
                bal += gas[idx]
            if idx == j and bal >= 0:
                return j
        return -1
        