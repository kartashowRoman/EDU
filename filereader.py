class FileReader():
	
	def __init__(self, path = ''):
		self.path = path

	def read(self):
		try:
			with open(self.path, 'r') as file:
				text = file.read()
		except:
			return ''

		return text

	def write(self, some_text = ''):
		with open(self.path, 'w') as file:
			file.write(some_text)
	
	def count(self):
		from nltk.tokenize import word_tokenize

		text = self.read()
		text_tokenized = word_tokenize(text)
		self.word_count = len(text_tokenized)

		with open(self.path, 'r') as file:
			self.line_count = len(file.readlines())

	def __str__(self):
		import pathlib
		pwd = str(pathlib.Path().absolute())
		pwd += '/'+self.path
		return pwd

	def __add__(self, another_file):
		text1 = self.read()
		text2 = another_file.read()
		name1 = self.path.replace('.txt', '')
		name2 = another_file.path
		with open(name1+name2, 'w') as file:
			file.write(text1+text2)
		return FileReader(name1+name2)



a = FileReader('text1.txt')
b = FileReader('text2.txt')
a.write('hi')
b.write('yo')
c = a + b
print(c)
