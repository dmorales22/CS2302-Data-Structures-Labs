import LRU as lru

def main(): 
	new_lru = lru.LRU(10)
	new_lru.put(1, "Test")
	new_lru.put(2, "Opp")
	new_lru.put(3, "Test")
	new_lru.put(4, "opp")
	new_lru.put(5, "testtt") 
	new_lru.put(6, "asdsad")
	new_lru.put(8, "ddd") 
	new_lru.put(9, "3323")
	new_lru.put(10, "Last")
	new_lru.put(11, "sdds") 
	new_lru.put(11, "sddsss") 
	new_lru.put(8, "wiped")
	new_lru.put(9, "wiped")
	new_lru.put(6, "wiped")
	new_lru.put(11, "wiped")
	new_lru.put(6, "testssss")
	new_lru.put(12, "1222")
	empty = new_lru.get(12)
	print(empty)
	new_lru.print_inorder()


main()