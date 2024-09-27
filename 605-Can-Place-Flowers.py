class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowersLeft = n

        if n == 0:
            return True

        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False
            else:
                return True

        if flowerbed[count] == 0 and flowerbed[count + 1] == 0:
            flowerbed[count] = 1
            flowersLeft -= 1
        count += 1

        while count < len(flowerbed) - 1:
            if flowerbed[count] == 0 and flowerbed[count + 1] != 1 and flowerbed[count - 1] != 1:
                flowerbed[count] = 1
                flowersLeft -= 1
            count += 1

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowersLeft -= 1

        if flowersLeft < 1:
            return True
        else:
            return False
