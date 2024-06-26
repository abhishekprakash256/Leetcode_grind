"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

"""

#test cases 

test_lst,k = [1,2,3,4], 2 
out = [3,4,1,2]


test_lst2 , k2  = [1], 5 
out2 = [1]

test_lst3,k3 = [1,2,3,4,5,6], 5
out3 = [3,4,5,6,1,2]


test_lst4 , k4 = [1,2,3,4,5,6,7], 3
out4 = [5,6,7,1,2,3,4]

test_lst5 ,k5 = [-1,-100,3,99], 2
out5 = [3,99,-1,-100]



#brute force soln 

class Solution(object):
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: None Do not return anything, modify nums in-place instead.
		"""

		for i in range(0,k):

			ele = nums.pop()

			nums.insert(0,ele)

		return nums

	def rotate_optimal(self,nums,k):
		"""
		Rotate the array using optimnal soln 
		"""

		#rotate the arrray 

		k = k%len(nums)

		left,right = 0, len(nums) - 1

		while left < right:

			nums[left], nums[right] = nums[right], nums[left]
			left +=1
			right -=1

		

		left = 0
		right = k-1

		while left < right:
			nums[left], nums[right] = nums[right], nums[left]
			left +=1
			right -=1


		left = k
		right = len(nums) - 1

		while left < right:
			
			nums[left],nums[right] = nums[right] , nums[left]
			left +=1
			right -=1


		return nums 







if __name__ == "__main__":
	sol = Solution()
	res = sol.rotate_optimal(test_lst5,k5)

	print(res)