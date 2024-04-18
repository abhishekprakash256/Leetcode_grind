"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a 

neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 
"""

"""

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

[1,3,4,9,1,0]

binary search 

modified 





"""

class Solution():
    def findPeakElement(self,nums):
        """
        Find the peak element 
        """

        l , r = 0 , len(nums) - 1 

        while l <= r :
            
            mid = l +  (r - l ) // 2 

            if nums[mid] > nums[mid + 1 ]:

                l = mid + 1

            else:
                r = mid - 1

        return l 


#take a break and solve the question again 

