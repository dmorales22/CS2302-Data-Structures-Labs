#This code is adapted from the Zybooks implementation of Red-Black trees. This code was modified be me (David Morales) to work in Python 3 with added attributes, and to use pythonian conventions. 

class RBNode(object): 
	def __init__(self, word = "", key = 0, left = None, parent = None, right = None, color = -1): 
		self.word = word #added attribute 
		self.key = 0
		self.left = None
		self.parent = None
		self.right = None
		self.color = -1 #colors use 1 and 0s instead of strings. 

class RedBlack(object): 
	#0 is black, 1 is red. Where is commented. 
	def __init__(self, root = None): 
		self.root = None
		
	def bst_insert(self, node):
		if (self.root == None):
			self.root = node
			node.left = None 
			node.right = None
			
		else:
			cur = self.root
			while (cur != None): 
				if (node.key < cur.key):
					if (cur.left == None):
						cur.left = node
						cur = None
					else:
						cur = cur.left
				else:
					if (cur.right == None):
						cur.right = node
						cur = None
					else:
						cur = cur.right 
						
			node.left = None 
			node.right = None 
		
	def rb_insert(self, words, key):
		node = RBNode(words, key)
		node.key = key 
		#print(node.word, node.key)
		
		self.bst_insert(node)
		node.color = 1 #red 
		self.rb_balance(node)
		
	def rb_balance(self, node):
		if (node.parent == None): 
			node.color = 0 #black 
			return
		
		if (node.parent.color == 0): #black
			return

		parent = node.parent
		grandparent = self.rb_get_grandparent(node)
		uncle = self.rb_get_uncle(node)
		
		if (uncle != None and uncle.color == 1): #red 
			parent.color = uncle.color = 0 #black
			grandparent.color = 1 #red 
			self.rb_balance(grandparent)
			return
			
		if (node == parent.right and parent == grandparent.left):
			self.rb_rotate_left(parent)
			node = parent
			parent = node.parent
			
		elif (node == parent.left and parent == grandparent.right):
			self.rb_rotate_right(parent)
			node = parent
			parent = node.parent
			
		parent.color = 0 #black 
		grandparent.color = 1 #red 
		
		if (node == parent.left):
			self.rb_rotate_right(grandparent)
			
		else:
			self.rb_rotate_left(grandparent)
			
	def rb_get_grandparent(self, node): 
		if (node.parent == None):
			return None 
		
		return node.parent.parent
		
	def rb_get_uncle(self, node):
		grandparent = None 
		if (node.parent != None):
			grandparent = node.parent.parent
			
		if (grandparent == None):
			return None 
			
		if (grandparent.left == node.parent):
			return grandparent.right
			
		else:
			return grandparent.left
			
	
	def rb_rotate_left(self, node): 
		right_left_child = node.right.left
		if (node.parent != None):
			self.rb_replace_child(node.parent, node, node.right)
		else:
			self.root = node.right
			self.root.parent = None

		self.rb_set_child(node.right, "left", node)
		self.rb_set_child(node, "right", right_left_child)
		
	def rb_rotate_right(self, node): 
		left_right_child = node.left.right
		if (node.parent != None):
			self.rb_replace_child(node.parent, node, node.left)
		else:
			self.root = node.left
			self.root.parent = None
			
		self.rb_set_child(node.left, "right", node)
		self.rb_set_child(node, "left", left_right_child)
	
	def rb_set_child(self, parent, which_child, child): 
		if (which_child != "left" and which_child != "right"):
			return False
		
		if (which_child == "left"):
			parent.left = child
		
		else:
			parent.right = child
		
		if (child != None):
			child.parent = parent
			
		return True
		
	def rb_replace_child(self, parent, current_child, new_child):
		if (parent.left == current_child):
			return self.rb_set_child(parent, "left", new_child)
			
		elif (parent.right == current_child):
			return self.rb_set_child(parent, "right", new_child)
			
		return False