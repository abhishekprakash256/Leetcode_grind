"""
The program to find the 3 sum of the list 
such that i != j, i != k, and j != k, and
and sum is 0 
"""

nums = [-1,0,1,2,-1,-4]
out = [[-1,-1,2],[-1,0,1]]

nums2 = [0,1,1]
out2 = []


class Solution():
	def threeSum(self, nums):
		"""
		The program to make the 3 sum 
		"""
		#sort the array 
		nums.sort()
		k = len(nums) - 1
		res_lst = []


		for i in nums: 

			j = i + 1 
			sum = nums[i] + nums[j] + nums[k]

			#start the loop
			while l <= r:

				if sum  == 0 and i != j and i= k and j = k:
					res_lst.append([nums[i],nums[j],nums[k]])

				elif sum > 0:
					l -=1

				else:
					r +=1

		
		return res_lst


sol = Solution()
res = sol.threeSum(nums)

print(res)








		