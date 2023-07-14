class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ptr = 0
        ret = ''
        while(ptr<len(word1) or ptr < len(word2)):
            if ptr < len(word1):
                ret += word1[ptr]
            if ptr < len(word2):
                ret += word2[ptr]
            ptr+=1
        return ret
        