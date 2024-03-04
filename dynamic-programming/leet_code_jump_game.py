"""

You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

"""


nums = [2,3,1,1,4]
out = True 



nums2 = [3,2,1,0,4]
out2 = False




"""
make the algo -- 



"""


class Solution():

	def canJump(self,nums):
		"""
		The function to find the brute force soln of can jump 
		"""

		goal = len(nums) - 1

		#start the loop 

		for i in range(len(nums)-1,-1,-1):

			if i + nums[i] >= goal :
				goal = i 

		return True if goal == 0 else False


		



if __name__ == '__main__':
	
	sol = Solution()

	print(sol.canJump(nums2))