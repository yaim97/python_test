class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)<0 or len(strs)>200:
            return False
        
        com_str=""

        if len(strs)==0:
            return com_str

        
        min_len=len(strs[0])
        for str in strs:
            if len(str)<0 or len(str)>200:
                return False
            if min_len>len(str):
                min_len=len(str)

        flag=True
        for i in range(min_len):
            c=strs[0][i]
            for j in range(1,len(strs)):
                if c!=strs[j][i]:
                    flag=False
            if flag==True:
                com_str+=c
            else:
                break 

        return com_str