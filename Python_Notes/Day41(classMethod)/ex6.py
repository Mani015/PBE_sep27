class MyClass:
	def __init__(self, value):
		self.value = value

	@staticmethod
	def get_max_value(x, y):
		return max(x, y)

# Create an instance of MyClass
obj = MyClass(10)

print(MyClass.get_max_value(20, 30))

print(obj.get_max_value(20, 30))

