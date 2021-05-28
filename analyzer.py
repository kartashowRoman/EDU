class UnigramMorphAnalyzer():



	def train(self, corpus_path):
		from collections import defaultdict
		
		with open(corpus_path, 'r') as file:
			train_data = file.read().split("\n")
			model = defaultdict(defaultdict)
			for i in train_data:
				try:
					word, pos = i.split(' ')
					
				except:
					continue

				model[word[-1]][pos] =1 		
		return model



a = UnigramMorphAnalyzer()


for i in a.train('get.txt'):
	print(i[0][1])
