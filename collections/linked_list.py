# A Python file to demonstrate Linked-List in Python

class Element(object):
	"""A element class for elements in linked list """
	def __init__(self, value):
		self.next = None
		self.value = value

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def append(self, new_element):
		""" function to append element in linked list """
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element
	
	def get_position(self, position):
		"""Get an element from a particular position.
		Assume the first position is "1".
		Return "None" if position is not in the list."""

		# create a counter to manage position and counter relation
		counter = 1
		current = self.head

		# return None if unwanted condition
		if not position or position < 1:
			return None

		# iterate through all elements and mange counter simultaneously
		# if position == counter ==> retunr respective element
		while current and counter <= position:
			if counter == position:
				return current
			current = current.next
			counter += 1
		
		# return None if not any conditon met
		return None
	
	def insert(self, new_element, position):
		"""Insert a new node at the given position.
		Assume the first position is "1".
		Inserting at position 3 means between
		the 2nd and 3rd elements."""
		
		counter = 1
		current = self.head

		if position > 1:
			while current and counter < position:
				if counter == position - 1:
					new_element.next = current.next
					current.next = new_element
				current = current.next
				counter += 1
		elif position == 1:
			new_element.next = self.head
			self.head = new_element
		
	def delete(self, value):
		"""Delete the first node with a given value."""
		
		counter = 1
		current = self.head

		pass

	def print_list(self):
		temp = self.head
		while(temp):
			print(temp.value, end=" ")
			temp = temp.next


if __name__ == '__main__':
	""" main function to execute test case """

	# create some elements
	e1 = Element(1)
	e2 = Element(2)
	e3 = Element(3)
	e4 = Element(4)

	# create LinkedList with first element as head
	ll = LinkedList(e1)

	# append more elements to linked list
	ll.append(e2)
	ll.append(e3)
	ll.append(e4)

	# print all item in linked list
	print("Printing all values in linked list:")
	ll.print_list()
	print("\n")

	# get position of an element
	print("Value at 1st Position", ll.get_position(1).value)
	print("Value at 2st Position", ll.get_position(2).value)
	print("Value at 4rth Position", ll.get_position(4).value)

	# insert a new element on postiton 3 means (between 2 and 3)
	e5 = Element(5) 
	ll.insert(e5, 3)

	# now again print all item in linked list to get new added list
	ll.print_list()

	# Test delete
	ll.delete(1)
	# Should print 2 now
	print(ll.get_position(1).value)
	# Should print 4 now
	print(ll.get_position(2).value)
	# Should print 3 now
	print: ll.get_position(3).value
	
	

