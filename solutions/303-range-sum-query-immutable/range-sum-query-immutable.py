class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        current_total = 0
        for num in nums:
            current_total += num
            self.prefix.append(current_total)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix[right]
        left_sum = self.prefix[left - 1] if left > 0 else 0
        
        return right_sum - left_sum