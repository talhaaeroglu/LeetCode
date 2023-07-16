class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        plantableCount = 0
        for i in range(len(flowerbed)):
            if len(flowerbed) == 1 and flowerbed[0] == 0:
                plantableCount = 1
                break
            if i == 0 and flowerbed[0] == 0 and flowerbed[1] == 0:
                plantableCount += 1
                flowerbed[i] = 1 
            elif i == len(flowerbed) -1 and flowerbed[len(flowerbed) -1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
                plantableCount += 1
                flowerbed[i] = 1  
            else:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    plantableCount += 1
                    flowerbed[i] = 1

        if n <= plantableCount:
            return True
        else:
            return False

            