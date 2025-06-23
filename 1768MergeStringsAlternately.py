class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        for i in range(len(a)):
            if i<len(word1):
                c += word1[i]
            if i<len(b):
                c += word2[i]
            i += i
        return c