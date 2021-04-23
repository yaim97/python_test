class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<1 or len(s)>1000:
            return False

        def searchPalindrome(s,left,right):
            while left>=0 and right<len(s):
                if s[left]==s[right]:
                    left-=1
                    right+=1
                else:
                    break
            return s[left+1:right]

        res = ""
        for i in range(len(s)):
            s1 = searchPalindrome(s,i,i)
            s2 = searchPalindrome(s,i,i+1)

            if len(res)<len(s1):
                res=s1
            if len(res)<len(s2):
                res=s2
        return res

        

