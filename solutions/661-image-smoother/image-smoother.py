class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n:
                            total += img[ni][nj]
                            count += 1
                
                result[i][j] = total // count
        
        return result