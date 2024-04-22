"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a 
file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another 
computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure 
that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
"""

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


#make the tree 

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.left = TreeNode(4)


#print the tree

def tree_printer(node):

	if node:
		print(node.val)

		tree_printer(node.left)
		tree_printer(node.right)




"""
Capture the null values and do bfs 

we implelnmt bfs using a stack iterative apprach 

cath is to capture the null values 


"""