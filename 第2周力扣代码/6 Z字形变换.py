class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1: return s
        
        strRows=[]
        minLen=len(s)
        if minLen>numRows: minLen=numRows
        for i in range(minLen):
            strRows.append("")

        curRow=0
        go=False
        for c in s:
            strRows[curRow]+=c
            if curRow==0 or curRow==numRows-1:
                if go==False: go=True
                else: go=False
            if go==True: curRow+=1
            else: curRow-=1
        
        ret=""
        for str_ in strRows:
            ret+=str_
        return ret

        