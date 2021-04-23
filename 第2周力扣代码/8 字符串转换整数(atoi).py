class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        numStr=""
        getNum=False

        for c in s:
            if (c=='+' or c=='-') and getNum==False:
                getNum=True
                numStr+=c
                continue
            
            isNum=True
            try:
                int(c)
            except ValueError:
                isNum=False
            if isNum==False and c!=' ' and getNum==False:
                return 0

            if isNum==True and getNum==False:
                getNum=True
            if isNum==True and getNum==True:
                numStr+=c
                continue
            if isNum==False and getNum==True:
                break

        try:
            int(numStr)
        except ValueError:
            return 0
        
        num=int(numStr)
        if num<-2**31:
            return -2**31
        elif num>2**31-1:
            return 2**31-1
        else:
            return num
            
            
            
            