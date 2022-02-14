# A Python file to demonstrate Linked-List in Python

class Element(object):
	"""A element class for elements in linked list """
	def __init__(self, value):
		self.next = None
		self.value = value

class LinkedList(object):
	def __init__(self, element):
		self.element = None

	def append(self, new_element):
		""" function to append element in linked list """
		current = self.element
		if self.element:
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.element = new_element
	
	def get_position(self, position):
		"""Get an element from a particular position.
		Assume the first position is "1".
		Return "None" if position is not in the list."""

		if self.element and position:
			pass


if __name__ == '__main__':
	""" main function to execute test case """
	pass
