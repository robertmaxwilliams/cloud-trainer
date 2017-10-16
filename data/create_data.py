import pandas
import numpy as np
import pickle


def pickle_data(filename):
	""" 
	Pickle training data found at filename, as list of two numpy array
	"""
	# import the csv as numpy array
	data = pandas.read_csv(filename, delim_whitespace=True, lineterminator='\n').values
	# shuffle the values in place, since data is clumped by class
	np.random.shuffle(data)
	
	# get all but last column for 'X', input data
	X = data[:, :-1] 
	X = X.astype(float)

	# get only the last row for 'y', targets and convert to 2-wide onehot
	y = data[:, -1]
	y = y.astype(int)	
	y_onehot = np.zeros((y.shape[0], 2))
	y_onehot[np.arange(y.shape[0]), y] = 1.
	y = y_onehot
	
	simple_filename = filename.split('/')[-1]
	with open(simple_filename+'.pickle', 'w') as outfile:
		pickle.dump([X, y], outfile)

pickle_data('../raw_data/cons_feature')
pickle_data('../raw_data/rbp_feature')
