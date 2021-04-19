class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<1 or len(s)>15:
            return False

        rnum=0

        if "IV" in s:
            rnum+=4
            s=s.replace("IV",'')
        if "IX" in s:
            rnum+=9
            s=s.replace("IX",'')
        if "XL" in s:
            rnum+=40
            s=s.replace("XL",'')
        if "XC" in s:
            rnum+=90
            s=s.replace("XC",'')
        if "CD" in s:
            rnum+=400
            s=s.replace("CD",'')
        if "CM" in s:
            rnum+=900
            s=s.replace("CM",'')

        for c in s:
            if c=='I': rnum+=1
            if c=='V': rnum+=5
            if c=='X': rnum+=10
            if c=='L': rnum+=50
            if c=='C': rnum+=100
            if c=='D': rnum+=500
            if c=='M': rnum+=1000

        if rnum>=1 and rnum<=3999:
            return rnum
        else:
            return False