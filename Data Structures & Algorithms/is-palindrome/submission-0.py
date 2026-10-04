class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        c=0

        s1=""
        for m in s:
            if m.isalnum():   
                s1 += m.lower()

        n = len(s1)
        for i in range(n//2):
            if s1[i] != s1[n-i-1]:
                return False
            else:
                c=c+1
        if (c==n//2):
            return True