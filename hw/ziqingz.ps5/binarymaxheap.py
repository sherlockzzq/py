class Node:

	left_child = None
	right_child = None

	def __init__(self, key):
		self.key = key

class BinaryMaxHeap:

	def __init__(self, root = None):
		self.root = root
		self.heap = []

	def heapify(self, *pos):
		for i in pos:
			self.heap.append(i)

		val = sorted(self.heap, reverse = True)
		self.root = Node(val[0])
		pointer = self.root
		queue = []
		queue.append(pointer)
		i = 1
		while i < len(val):
			l = len(queue)
			while l:
				node = queue.pop(0)
				l -= 1 
				if i < len(val):
					n = Node(val[i])
					node.left_child = n
					i += 1
					queue.append(node.left_child)
				if i < len(val):
					n = Node(val[i])
					node.right_child = n
					i += 1
					queue.append(node.right_child)


	def push(self, node):
		self.heapify(node.key)

	def pop(self):
		try:
			key = self.root.key
			val = sorted(self.heap, reverse = True)
			val.pop(0)
			self.heap = []
			self.heapify(*val)
			return Node(key)
		except IndexError:
			self.root = None

	def delete(self, element):
		if element not in self.heap:
			return None
		self.heap.remove(element)
		val = self.heap
		self.heap = []
		self.heapify(*val)
		return Node(element)