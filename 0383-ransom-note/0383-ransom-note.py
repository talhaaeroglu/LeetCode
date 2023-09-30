class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = {}
        for ch in magazine:
            if ch not in hashMap.keys():
                hashMap[ch] = 1
            else:
                hashMap[ch] += 1
        for ch in ransomNote:
            if ch in hashMap.keys() and hashMap[ch] >= 1:
                hashMap[ch] -= 1
            else:
                return False
        return True
                
            