class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for i in accounts:
            if sum(i) > max:
                max = sum(i)
        return max

        