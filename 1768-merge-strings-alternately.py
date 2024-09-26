class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer = 0
        result = ""

        while pointer < len(word1) and pointer < len(word2):
            result += word1[pointer] + word2[pointer]
            pointer += 1

        if len(word1) > len(word2):
            result += word1[pointer:]
        if len(word1) < len(word2):
            result += word2[pointer:]

        return result
