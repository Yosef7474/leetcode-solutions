class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}

        for i in range(len(s)):
            if s[i] in sCount:
                sCount[s[i]]+=1
            else:
                sCount[s[i]] = 1
        for j in range(len(t)):
            if t[j] in tCount:
                tCount[t[j]]+=1
            else:
                tCount[t[j]] = 1
        return sCount == tCount
            
        



        