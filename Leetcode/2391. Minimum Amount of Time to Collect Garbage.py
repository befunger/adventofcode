class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # For each truck, find the last house with its trash (iterate from end until first garbage of right type)
        # Time needed is the sum of travel times up until that house + number of total garbage (sum while iterating)
        # Do for all 3 trucks
        garb_dict = {"G" : 0, "P" : 0, "M" : 0}
        for i in range(len(garbage)-1, -1, -1):
            for key in garb_dict:
                if garb_dict[key] > 0:
                    garb_dict[key] += travel[i]
            for char in garbage[i]:
                garb_dict[char] += 1
        return garb_dict["G"] + garb_dict["P"] + garb_dict["M"]
