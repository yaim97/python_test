class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0

        len=0
        nums = []
        if int(x)<0:
            temp=-x
        else:
            temp=x

        while temp!=0:
            len+=1
            nums.append(int(temp%10))
            temp = int(temp) / 10

        if int(x)<0:
            num="-"
        else:
            num=""
        for i in range(len):
            num+=str(nums[i])

        if int(num)<-2**31 or int(num)>=2**31:
            return 0
        else:
            return int(num)