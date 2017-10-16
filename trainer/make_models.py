from __future__ import print_function
"""
This code will take input csv and convert it to a vector
for input in a net. Then the correctly shaped net will train
on input output pairs generated in batches, randomly
finally, the network is verified on some witheld data.

Make sure that the path for train_model point to whitespace delimited files that you want
"""

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop
from keras import losses, layers

import pandas
import numpy as np
import argparse
import pickle

from tensorflow.python.lib.io import file_io

def train_model(X, y):
	""" 
	Train model on X and y, return model
	"""
	#create test data to check for overfitting
	X_test = X[:200]
	X = X[200:]	
	y_test = y[:200]
	y = y[200:]
	
	# num inputs is the number of columns in the csv excluding the last one
	num_inputs = X.shape[1]
	print('X shape: ', X.shape)
	print('y shape: ', y.shape)

	# create and compile the model
	model = Sequential()

	model.add(Dense(500, input_dim=num_inputs))
	model.add(Activation('relu'))
	model.add(Dropout(0.4))

	model.add(Dense(300))
	model.add(Activation('relu'))
	model.add(Dropout(0.4))

	model.add(Dense(10, name='learned_features'))
	model.add(Activation('relu'))

	model.add(Dense(2))
	model.add(Activation('softmax'))

	rms = RMSprop()
	loss = losses.categorical_crossentropy 
	model.compile(loss=loss, optimizer=rms, metrics=['accuracy'])

	# train the model
	model.fit(X, y, epochs=50, batch_size=100)

	# test the model for overfitting using withheld test data
	scores = model.evaluate(X_test, y_test)
	print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

	return model


def train_model_cloud(train_file, **args):
	# Here put all the main training code in this function
	print(train_file)
	file_stream = file_io.FileIO(train_file, mode='r')
	X, y = pickle.load(file_stream)
	model = train_model(X, y)
	return model

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	# Input Arguments
	parser.add_argument(
			'--train-file',
			help='GCS or local paths to training data',
			required=True
			)

	parser.add_argument(
			'--job-dir',
			help='GCS location to write checkpoints and export models',
			required=True
			)
	args = parser.parse_args()
	arguments = args.__dict__
	job_dir = arguments.pop('job_dir')

	model = train_model_cloud(**arguments)
	model.save('trained_model1.h5')
