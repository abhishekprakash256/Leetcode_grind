"""

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.




"""



"""

approch
- two pointer 
- if len(prices) == 0:
	return 0 

profit = 0 

- l , r = 0 , 1

- if prices[l] >= prices[r]:
	r += 1
	l += 1

- else:
	profit = max(profit , (prices[r] - pricesp[l]))
	r += 1






"""


class Solution:
	def maxProfit(self, prices) -> int:
		"""
		The functiont to find the max profit from the stocks selling 
		passes in leet code
		"""

		#base case 
		if len(prices) == 0 :
			return 0


		#poiinter imitilization 
		l , profit , r = 0, 0, 1 


		#start the loop 

		while r < len(prices):

			#calc the profit
			if prices[l] >= prices[r]:
				l = r 
				r += 1


			else:
				profit = max(profit, (prices[r] - prices[l]))
				r += 1


		return profit



















		
