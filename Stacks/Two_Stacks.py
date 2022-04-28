class TwoStack:
	def __init__(self, size):
		self.stack = [0]*size
		self.top1 = -1
		self.top2 = size
		self.size = size
		
	def push1(self, val):
		if(self.top2 - self.top1 > 1):
			self.top1 += 1
			self.stack[self.top1] = val
			
	def push2(self, val):
		if(self.top2 - self.top1 > 1):
			self.top2 -= 1
			self.stack[self.top2] = val
			
	def pop1(self):
		if(self.top1 >= 0):
			ans = self.stack[self.top1]
			self.top1 -= 1
			return ans
		else:
			return -1
		
	def pop2(self):
		if(self.top2 < self.size):
			ans = self.stack[self.top2]
			self.top2 += 1
			return ans
		else:
			return -1
