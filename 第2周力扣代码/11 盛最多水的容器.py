class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        ret=0
        left=0
        right=len(height)-1
        while left<right:
            ret=max(ret,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ret

                    