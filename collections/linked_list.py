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

		counter = 1
		current = self.element

		if not position or position > 1:
			return None

		while current and counter <= position:
			pass


	def print_list(self):
		temp = self.element
		while(temp):
			print(temp.value)
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

	# get position of an element
	ll.get_position(2).value
	
	

