import numpy as np
import matplotlib as plt

class SupportVectorMachine:

	def __init__(self, visualization=True):
		self.visualization = visualization
		if visualization:
			self.fig = plt.figure()
			self.ax  = self.fig.add_subplot(1,1,1)


	def fit():
		pass

	def predict(self, features):

		# sign( x.w + b)
		classification = np.sign(np.dot(self.features, self.w) + self.b)
		return classification