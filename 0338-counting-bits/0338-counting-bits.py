class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = sum(1 for bit in bin(i) if bit == '1')
            res.append(count)
        return res