
def integers():
	i = 0
	while True:
		yield i
		i += 1

def squares():
	i = 0
	while True:
		yield i ** 2
		i += 1

def take(generator):
	# res = []
	# for i in range(5):
	# 	res.append(next(generator))
	return [next(generator) for i in range(5)]
	# return res
i1 = squares()


for i in range(10):
	print(next(i1))

for i in range(10):
	print(next(i1))

print(take(i1))