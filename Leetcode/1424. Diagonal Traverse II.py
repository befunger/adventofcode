class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        for i,row in enumerate(nums):
            for j,val in enumerate(row):
                if len(res) <= i+j:
                    res.append([])
                res[i+j].append(val)
        return [a for row in res for a in reversed(row)]
