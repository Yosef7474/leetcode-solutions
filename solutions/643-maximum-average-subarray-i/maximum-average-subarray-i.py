class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k

        currentSum = sum(nums[l:r])
        maxSum = currentSum

        while r < len(nums):
            currentSum += nums[r]
            currentSum -= nums[l]
            r +=1
            l +=1

            if currentSum > maxSum: 
                maxSum = max(maxSum, currentSum)
        
        return maxSum / k

        