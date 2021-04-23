class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        temp=nums[0]
        i=1 
        while True:
            if i>=len(nums):
                break
            if nums[i]==temp:
                nums.remove(temp)
            else:
                temp=nums[i]
                i+=1
        return len(nums)
