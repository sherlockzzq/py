class Node:
        next = 1
	def __init__(self, data, next_node = None):
		self.data = data
		self.next_node = next_node

class LinkedList:
	def __init__ (self, head, length = 1):
		self.head = head
		self.length = 1

	def insert(self, node, index = None):
		if self.head == None:
			self.head = node
			self.length = 1
		elif index == None:
			n = self.head
			while n.next_node != None:
				n = n.next_node
			n.next_node = node
		else:
			n = Node(0)
			a = n
			n.next_node = self.head
			while index > 0 and n != None:
				n = n.next_node
				index -= 1
			node.next_node = n.next_node
			n.next_node = node
			self.length += 1
			self.head = a.next_node

	def remove(self, index):
		if index >= self.length or self.head == None:
			return None
		else:
			node = Node(0)
			a = node
			node.next_node = self.head 
			while index > 0:
				node = node.next_node
				index -= 1
			n = node.next_node
			node.next_node = node.next_node.next_node
			self.length -= 1
			self.head = a.next_node
			return n

	def find(self, data):
		index = 0
		node = self.head
		while node != None:
			if node.data == data:
				return index
			node = node.next_node
			index += 1

		return 0

