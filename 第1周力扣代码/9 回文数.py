class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<-2**31 or x>=2**31:
            return False

        if x<0:
            return False

        nums=[]

        while x!=0:
            mod=int(x)%10
            nums.append(mod)
            x=x/10

        low=0
        high=len(nums)-1
        while low<=high:
            if nums[low]==nums[high]:
                low+=1
                high-=1
            else:
                return False

        return True