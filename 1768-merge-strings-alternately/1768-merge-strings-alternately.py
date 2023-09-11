class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""    
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(word1) or ptr2 < len(word2):
            if ptr1 < len(word1):
                res += word1[ptr1]
                ptr1+=1
            if ptr2 < len(word2):
                res+= word2[ptr2]
                ptr2+=1
        return res