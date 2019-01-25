from string import punctuation
from mrjob.job import MRJob

class MRWordCount(MRJob):

	def mapper(self, _, line):
		#saco puntuacion y pas a minusculas
		for punc in punctuation:
			line = line.replace(punc, ' ')
		line = line.lower()

		for w in line.split():
			#esta linea va a ir largando la palabra y el 1
			yield w,1

	def reducer(self, key, values):

		yield key, sum(values)


if __name__ == '__main__':
	MRWordCount.run()