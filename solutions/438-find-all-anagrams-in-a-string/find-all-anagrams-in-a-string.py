class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        window = Counter()
        result = []
        left, right = 0, 0

        while right < len(s):
            window[s[right]] += 1
            right += 1

            if right - left == len(p):
                if window == target:
                    result.append(left)
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
        return result
