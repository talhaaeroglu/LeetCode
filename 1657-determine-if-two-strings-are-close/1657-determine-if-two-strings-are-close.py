class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        hm1 = {}
        hm2 = {}
        for i in range(len(word1)):
            if word1[i] in hm1:
                hm1[word1[i]] += 1
            if word1[i] not in hm1:
                hm1[word1[i]] = 1
            if word2[i] in hm2:
                hm2[word2[i]] += 1     
            if word2[i] not in hm2:
                hm2[word2[i]] = 1     

        return set(hm1.keys()) == set(hm2.keys()) and sorted(hm1.values()) == sorted(hm2.values())
