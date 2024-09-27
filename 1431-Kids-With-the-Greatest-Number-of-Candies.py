class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mostCandies = 1
        for amount in candies:
            if mostCandies < amount:
                mostCandies = amount

        result = []

        for kid in candies:
            if kid + extraCandies >= mostCandies:
                result.append(True)
            else:
                result.append(False)

        return result
