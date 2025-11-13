class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        check = set(nums)


        for i in range(len(nums)+1):
            if i not in check:
                return i
            

        