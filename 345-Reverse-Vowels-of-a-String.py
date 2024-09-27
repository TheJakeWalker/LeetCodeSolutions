class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        for letter in s:
            if letter in vowels:
                stack.append(letter)

        index = 0
        answer = ""
        while index < len(s):
            if s[index] in vowels:
                answer = answer + stack[-1]
                stack.pop(-1)
            else:
                answer = answer + s[index]
            index += 1

        return answer
