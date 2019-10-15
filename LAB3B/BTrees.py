class TreeNode(object): 
	def __init__(self, word = None, key = 0): 
		self.word = word 
		self.key = 0
		self.left = None
		self.parent = None
		self.right = None
		
class AVLTree(object): 
	def __init__(self, node = None): 
		self.node = None 
		self.height = -1  
		self.parent = None
		self.root = None  
		
	def avl_insertion(self, words, key): 
		node = TreeNode(words, key)
   
		if (self.root == None): 
			self.root = node
			node.parent = None 
			return 

		cur = self.root 
		while (cur != None): 
			if (node.key < cur.key): 
				if (cur.left == None): 
					cur.left = node
					node.parent = cur
					cur = None
         
				else:
					cur = cur.left
			else:
				if (cur.right == None): 
					cur.right = node
					node.parent = cur
					cur = None
         
				else:
					cur = cur.right

		node = node.parent
		
		while (node != None): 
			self.avl_rebalance(node)
			node = node.parent
	
	def avl_rebalance(self, node): 
		self.avl_update_height(node)        
		if (self.avl_get_balance(node) == -2): 
			if (self.avl_get_balance(node.right) == 1): # Double rotation case.
				self.avl_rotate_right(node.right)
			
			return self.avl_rotate_left(tree, node)
		
		elif (self.avl_get_balance(node) == 2): 
			if (self.avl_get_balance(node.left) == -1):  #Double rotation case.
				self.avl_rotate_left(tree, node.left)
		
			return self.avl_rotate_right(tree, node)
  
		return node
		
	def avl_update_height(self, node): 
		left_height = -1
		
		if (node.left != None):
			left_height = node.left.height
		
		right_height = -1
		
		if (node.right != None):
			right_height = node.right.height
		
		node.height = max(left_height, right_height) + 1
	
	def avl_get_balance(self, node):
		left_height = -1
		
		if (node.left != None):
			left_height = node.left.height
			
		right_height = -1
		if (node.right != None):
			right_height = node.right.height
		
		return left_height - right_height
	
	def avl_rotate_right(self, node): 
		left_right_child = node.left.right
		if (node.parent != None):
			self.avl_replace_child(node.parent, node, node.left)
		else: # node is root
			self.root = node.left
			self.root.parent = None
	
		self.avl_set_child(node.left, "right", node)
		self.avl_set_child(node, "left", left_right_child)

	def avl_replace_child(self, parent, curr_child, new_child): 
		if (parent.left == curr_child):
			return self.avl_set_child(parent, "left", new_child)
		elif (parent.right == curr_child):
			return self.avl_set_child(parent, "right", new_child)
		return False
		
	def avl_set_child(self, parent, which_child, child): 
		if (which_child != "left" and which_child != "right"):
			return False
		
		if (whichChild == "left"):
			parent.left = child
			
		else:
			parent.right = child
			
		if (child != None):
			child.parent = parent
		
		self.avl_update_height(parent)
		return True

	def avl_rotate_left(self, node): 
		right_left_child = node.right.left
		if (node.parent != None):
			self.avl_replace_child(node.parent, node, node.right)
		else: # node is root
			self.root = node.right
			self.root.parent = None
	
		self.avl_set_child(node.right, "left", node)
		self.avl_set_child(node, "right", right_left_child)
	
