'''Create a data structure twoStacks that represent two stacks. 
Implementation of twoStacks should use only one array, i.e., 
both stacks should use the same array for storing elements. 

Following functions must be supported by twoStacks.

push1(int x) –> pushes x to first stack 
push2(int x) –> pushes x to second stack
pop1() –> pops an element from first stack and return the popped element 
pop2() –> pops an element from second stack and return the popped element
Implementation of twoStack should be space efficient.'''


import math 

class twoStacks: 

	def __init__(self, n):	 # constructor 
		self.size = n 
		self.arr = [None] * n 
		self.top1 = math.floor(n/2) + 1
		self.top2 = math.floor(n/2) 

	# Method to push an element x to stack1 

	def push1(self, x): 

		# There is at least one empty space for new element 
		if self.top1 > 0: 
			self.top1 = self.top1 - 1
			self.arr[self.top1] = x 
		else: 
			print("Stack Overflow by element : ", x) 

	# Method to push an element x to stack2 

	def push2(self, x): 

		# There is at least one empty space for new element 
		if self.top2 < self.size - 1: 
			self.top2 = self.top2 + 1
			self.arr[self.top2] = x 
		else: 
			print("Stack Overflow by element : ", x) 

	# Method to pop an element from first stack 

	def pop1(self): 
		if self.top1 <= self.size/2: 
			x = self.arr[self.top1] 
			self.top1 = self.top1 + 1
			return x 
		else: 
			print("Stack Underflow") 
			exit(1) 

	# Method to pop an element from second stack 

	def pop2(self): 
		if self.top2 >= math.floor(self.size/2) + 1: 
			x = self.arr[self.top2] 
			self.top2 = self.top2 - 1
			return x 
		else: 
			print("Stack Underflow") 
			exit(1) 


# Driver program to test twoStacks class 
if __name__ == '__main__': 
	ts = twoStacks(5) 
	ts.push1(5) 
	ts.push2(10) 
	ts.push2(15) 
	ts.push1(11) 
	ts.push2(7) 
	
	print("Popped element from stack1 is : " + str(ts.pop1())) 
	ts.push2(40) 
	print("Popped element from stack2 is : " + str(ts.pop2())) 


