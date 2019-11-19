class Node(object): 
	def __init__(self, key, value, prev = None, next = None, empty = False): #Constructor for the node (doubly linked list node).
		self.key = key
		self.value = value
		self.prev = prev
		self.next = next
		self.empty = empty
		
class LRU(object): 
	def __init__(self, max_capacity, size = 0, head = None, tail = None, table = {}): #Constructor for LRU. Set up like a doubly linked list with a hash table.
		self.size = size
		self.head = head 
		self.tail = tail
		self.table = table
		self.max_capacity = max_capacity
		
	def get(self, key): #Uses the dictionary get() function to get the node.value. O(1)
		if (self.head is None):
			return -1 
		
		found_node = self.table.get(key) 
		
		if found_node == None: 
			return -1 
	
		return found_node.value
	
	def put(self, key, value):  #Put function creates the nodes, the linked list, and populate the hash table. 
		if (self.head is None):  #If linked-list is empty, then it creates a new node and makes it the head. 
			self.head = Node(key, value)
			self.tail = self.head
			self.table[key] = self.head
			self.size += 1
			return
			
		if (key in self.table): #Checks if key is already in the table, then overrides the key values.
			if(key == self.head.key): 
				self.head.value = value

			node = self.table.get(key)
			node.value = value 
			return
			
		if (self.size >= self.max_capacity): #If size is at max_capacity. 
			if (self.tail.next is None): #If the tail node is at the end of the list, it overrides the head. 
				head_key = self.table.pop(self.head.key)
				self.head.key = key 
				self.head.value = value 
				node = Node(key, value) 
				self.table[key] = node
				self.tail = self.head
				return
				
			else: 
				node = self.tail.next #If tail is not at the end of list, and it overrides the next node that needs the overridden.
				pop_key = self.table.pop(node.key)
				node.key = key
				node.value = value
				self.tail = node
				self.table[key] = node
				return
				
		node = Node(key, value) #If the list is not fully populated, so it adds nodes and the updates the dictionary. 
		self.tail.next = node
		node.prev = self.tail
		self.tail = node 
		self.table[key] = node
		self.size = self.size + 1
		return
		
	def size(self):  #Returns self.size. put() function keeps track of size of the cache.
		return self.size

	def max_capacity(self): #Returns self.max_capacity. The variable is defined when creating a new LRU. 
		return self.max_capacity
		
	def print_inorder(self): #Prints the linked-list in order of the LRU. 
		if self.head is None: 
			print("It's empty!") 
			return 
		
		iter = self.head 
		
		while(iter != None): 
			print("Key:", iter.key, "Value:", iter.value) 
			iter = iter.next 
		print("\n")
		print("Current size:", self.size)
		print("Max capicity:", self.max_capacity)