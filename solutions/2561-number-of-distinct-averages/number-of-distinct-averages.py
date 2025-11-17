class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r =len(nums)-1

        distinct = set()

        while l<r:

            count = 0
            if len(nums) == 2:
                return 1

            else:
                num =  (nums[l] + nums[r]) / 2
                distinct.add(num)
                l+=1
                r-=1

        return len(distinct)
        