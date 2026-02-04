class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        
        result = []
        
        for num in nums:
            count = sorted_nums.index(num)
            result.append(count)
        
        return result