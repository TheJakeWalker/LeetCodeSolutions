"""
This problem asked to be completed without using division. So I used prefix/suffix lists of the respective products.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1]
        suffix = [1]

        for number in range(len(nums)):
            prefix.append(nums[number] * prefix[number])

        nums.reverse()
        for number in range(len(nums)):
            suffix.append(nums[number] * suffix[number])

        suffix.reverse()
        answer = []
        for index in range(len(nums)):
            answer.append(prefix[index] * suffix[index + 1])

        return answer