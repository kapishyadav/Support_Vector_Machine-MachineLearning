import numpy as np
import matplotlib as plt

class SupportVectorMachine:

	def __init__(self, visualization=True):
		self.visualization = visualization
		self.colors = {1:'r', -1: 'b'}
		if visualization:
			self.fig = plt.figure()
			self.ax  = self.fig.add_subplot(1,1,1)


	def fit(self, data):
		self.data = data

		opt_dict = {}

		transforms = [[1,1], [1,-1], [-1,-1], [-1,1]]
		all_data = []

		for yi in self.data:
			for featureset in self.data[yi]:
				for feature in featureset:
					all_data.append(feature)


		self.max_feature_value = max(all_data)
		self.min_feature_value = min(all_data)
		all_data = None #to release memory

		step_sizes = [self.max_feature_value*0.1, self.max_feature_value*0.01, self.max_feature_value*0.001]
		b_range_multiple = 5
		b_multiplie = 5
		latest_optimum = self.max_feature_value*10

		for step in step_sizes:

			w = np.array([latest_optimum, latest_optimum])
			optimized  = False
			while not optimized:
				pass








	def predict(self, features):

		# sign( x.w + b)
		classification = np.sign(np.dot(self.features, self.w) + self.b)
		return classification