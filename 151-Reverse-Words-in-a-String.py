class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        word = ''
        for character in s:
            if character != ' ':
                word += character
            elif word != '':
                stack.append(word)
                word = ''

        if word != '':
            stack.append(word)

        result = ""
        while len(stack) != 0:
            result += stack[-1]
            stack.pop(-1)
            if len(stack) != 0:
                result += ' '

        return result