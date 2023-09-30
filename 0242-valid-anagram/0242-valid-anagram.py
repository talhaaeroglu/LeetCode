class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        for ch in s:
            if ch not in mapS.keys():
                mapS[ch] = 1
            else:
                mapS[ch] += 1
        for ch in t:
            if ch not in mapT.keys():
                mapT[ch] = 1
            else:
                mapT[ch] += 1

        return mapS == mapT