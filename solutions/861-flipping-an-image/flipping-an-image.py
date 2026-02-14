class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        
        for i in range(n):
            left, right = 0, n - 1
            while left <= right:
                if left == right:
                    image[i][left] ^= 1
                else:
                    image[i][left], image[i][right] = image[i][right] ^ 1, image[i][left] ^ 1
                left += 1
                right -= 1
        
        return image