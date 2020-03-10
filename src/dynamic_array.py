class DynamicArray:
	def __init__(self, capacity):
		self.capacity = capacity
		self.count = 0
		self.storage = [None] * self.capacity
	
	def insert(self, index, value):
		# Make sure you have open space
		if self.count >= self.capacity:
			self.double_size()

		# Make sure index is in range 
		if index >= self.count:
			print("Error: Index out of range")
			return
		
		# Shift everything over to the right
		# Start with the last one, move it to the right
		for i in range(self.count, index, -1):
			self.storage[i] = self.storage[i-1]

		self.storage[index] = value
		self.count += 1
	
	def append(self, value):
		self.insert(self.count, value)
	
	def double_size(self):
		self.capacity *= 2
		new_storage = [None] * self.capacity
		for i in range(self.count):
			new_storage[i] = self.storage[i]
		
		self.storage = new_storage

my_array = DynamicArray(4)