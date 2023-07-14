class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ret = []
        _max = max(candies)
        for candy in candies:
            if candy + extraCandies >= _max:
                ret.append(True)
            else:
                ret.append(False)
        return ret