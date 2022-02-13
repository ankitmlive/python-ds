# A Python file to demonstrate Linked-List in Python

class Element(object):
	"""A element class for elements in plinked list """
	def __init__(self, value):
		super(Element, self).__init__()
		self.next = None
		self.value = value

class LinkedList(object):
	def __init__(self, element) -> None:
		self.element = None
