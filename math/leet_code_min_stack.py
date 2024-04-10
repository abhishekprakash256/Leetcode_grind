"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""



class MinStack():

    def __init__(self):
    	"""
		initilaize the stack like a list
    	"""
    	self.stack = [] 
        

    def push(self, val: int) -> None:
    	"""
    	The function to push data into the stack
    	"""
    	self.stack.append(val)

        

    def pop(self) -> None:
    	"""
		The pop from the list
    	"""
    	self.stack.pop(len(self.stack)-1)
        

    def top(self) -> int:
    	"""
		Get the top element from the list
    	"""
    	return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
    	"""
		The function to get the min value friom the stack
    	"""

    	return min(self.stack)

        

    def getMin(self) -> int:
    	"""
		The function to get the min value friom the stack
    	"""

    	return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()