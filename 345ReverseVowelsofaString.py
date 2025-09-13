class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a','e','i','o','u','A','E','I','O','U']
        s = s
        lis = list(s)

        left,right = 0,len(s)-1

        while left < right:
            if lis[left] not in v:
                left += 1
            elif lis[right] not in v:
                right -= 1
            else:
                lis[left], lis[right] = lis[right], lis[left]
                left += 1
                right -= 1
        result = ''.join(lis)
        return result