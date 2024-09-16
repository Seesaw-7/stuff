class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        num_stations = len(gas)
        sub = [x-y for x,y in zip(gas, cost)]

        if sum(sub) < 0:
            return -1

        amt = 0
        temp = [0] * num_stations

        for i in range(num_stations):
            amt += sub[i]
            temp[i] = amt

        min_val = min(temp)
        idx = temp.index(min_val)
        if idx == num_stations - 1:
            return 0
        else:
            return idx + 1
