解法1：时间复杂度O(m+n)，空间复杂度O(m+n)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mergeList=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                mergeList.append(nums1[i])
                i+=1
            else:
                mergeList.append(nums2[j])
                j+=1

        while i<len(nums1):
            mergeList.append(nums1[i])
            i+=1
        while j<len(nums2):
            mergeList.append(nums2[j])
            j+=1
        
        if len(mergeList)%2!=0:
            return float(mergeList[(len(mergeList)-1)/2])
        else:
            t=len(mergeList)/2
            return float((mergeList[t-1]+mergeList[t]))/2

解法2：时间复杂度O(m+n)，空间复杂度O(1)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sumLen=len(nums1)+len(nums2)
        retPre=-1
        ret=-1
        p=0
        q=0

        for i in range(int(sumLen/2)+1):
            retPre=ret
            if p<len(nums1) and (q>=len(nums2) or nums1[p]<=nums2[q]):
                ret=nums1[p]
                p+=1
            else:
                ret=nums2[q]
                q+=1
        
        if sumLen%2==0:
            return float(retPre+ret)/2
        else:
            return float(ret)

解法3：时间复杂度O(log(min(m,n)))，空间复杂度O(1)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        if m>n:
            temp=nums1
            nums1=nums2
            nums2=temp
            m=len(nums1)
            n=len(nums2)
        
        iMin=0
        iMax=m
        while iMin<=iMax:
            i=(iMin+iMax)/2
            j=(m+n+1)/2-i
            if j!=0 and i!=m and nums2[j-1]>nums1[i]:
                iMin=i+1
            elif i!=0 and j!=n and nums1[i-1]>nums2[j]:
                iMax=i-1
            else:
                maxLeft=0
                if i==0: maxLeft=nums2[j-1]
                elif j==0: maxLeft=nums1[i-1]
                else: maxLeft=max(nums1[i-1],nums2[j-1])

                if (m+n)%2==1: return float(maxLeft)

                maxRight=0
                if i==m: maxRight=nums2[j]
                elif j==n: maxRight=nums1[i]
                else: maxRight=min(nums1[i],nums2[j])

                return float(maxLeft+maxRight)/2
