class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<2 or len(nums)>10**3:
            return False

        for data in nums:
            if data<-10**9 or data>10**9:
                return False

        if target<-10**9 or target>10**9:
            return False

        index=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    index.append(i)
                    index.append(j)

        return index