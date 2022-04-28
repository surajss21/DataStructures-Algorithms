class Stack:
	def __init__(self, size):
		self.stack = [0]*size
		self.top = -1
		self.size = size

	def push(self, element):
		if(self.isFull()):
			print("Cannot push more elements, stack reached its max size")
		else:
			self.top += 1
			self.stack[self.top] = element
		pass

	def pop(self):
		if(self.isEmpty()):
			print("Cannot pop the elemenst because stack is empty :(")
		else:
			temp = self.stack[self.top]
			self.stack[self.top] = 0
			print(f"The poped element is : {temp}")
			self.top -= 1

	def isEmpty(self):
		if(self.top == -1):
			return True
		return False

	def isFull(self):
		if(self.size - self.top > 1):
			return False
		return True

	def peek(self):
		if(self.isEmpty()):
			print('Stack is empty :(')
		else:
			print(f"The peek element is : {self.stack[self.top]}")



def main():

	s = Stack(5)

	# s.peek()
	# s.pop()
	s.push(99)
	print(s.top)
	s.push(98)
	print(s.top)
	s.push(97)
	print(s.top)
	s.push(96)
	print(s.top)
	s.push(95)
	print(s.top)
	s.push(94)
	print(s.top)
	s.peek()
	s.pop()
	print(s.top)
	s.pop()
	print(s.top)
	s.pop()
	print(s.top)
	s.pop()
	print(s.top)
	s.pop()
	print(s.top)
	s.pop()
	print(s.top)



if __name__ == '__main__':
	main()
