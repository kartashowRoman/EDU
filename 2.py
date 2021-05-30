

class ReverseIterator(object):
	
	def __init__(self, array):
		self.array = array

	def __next__(self):
		try:	
			x = self.array[-1]
			del self.array[-1]
			return x
		except:
			
			raise ValueError('Empty iterator')
		
iterator = ReverseIterator([1, 2, 3])

for i in range(5):
	print(next(iterator))