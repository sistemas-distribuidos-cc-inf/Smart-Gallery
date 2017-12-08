import numpy as np
from keras.datasets import cifar10
from matplotlib import pyplot as plt
from scipy.misc import toimage
from PIL import Image
import keras
from keras.callbacks import History
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.pooling import AveragePooling2D
from keras.layers import Activation, Dense, Flatten
from keras.layers import Dropout
from keras.layers.normalization import BatchNormalization
from keras.optimizers import SGD
import os

# load dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
epochs = 10

model = Sequential()

def design_model( model ):
	# input layer
	model.add( Conv2D( 16, (2 , 2), input_shape = ( 32, 32, 3 ),
			kernel_initializer = 'glorot_uniform',
			strides = ( 1, 1 ),
			padding = 'same',
			activation = 'linear' ) )

	# hidden layers

	model.add( Activation( 'linear' ) )

	model.add( Dropout( 0.4 ) )

	model.add( MaxPooling2D( pool_size = ( 2, 2 ) ) )

	model.add( Conv2D( 18, ( 2, 2 ), strides = ( 2, 2 ), activation = 'linear', padding = 'same' ) )

	model.add( Flatten() )

	model.add( Dense( 12, activation = 'linear' ) )

	model.add( BatchNormalization() )

	model.add( Activation( 'linear' ) )

	model.add( Dropout( 0.5 ) )

	# classification layer
	model.add( Dense( 10, activation = 'softmax' ) )

	return model

def compile_model( model ):
	# backpropagation
	lrate  = 0.2
	       = SGD( lr = lrate, 
					momentum = 0.7, 
					decay = 0.0005, 
					nesterov = True, 
					clipnorm = 1., 
					clipvalue = 0.5 )

	model.compile( loss = 'sparse_categorical_crossentropy', 
				optimizer = sgd, 
				metrics = ['accuracy'] )

	# fit model
	history = model.fit(  x_train, y_train, 
					validation_data = ( x_test, y_test ), 
					epochs = epochs, 
					batch_size = 32 )
	return model

def main():

	modelS = design_model( model )
	modelS = compile_model( model )
	modelS.save_weights('bias/recg.h5')

	scores = modelS.evaluate( x_test, y_test, verbose = 0 )

	print( '\n' )
	print( 'Accuracy: %.2f%%' % ( scores[1] * 100 ) )
	print( 'Loss: %.2f%%' % ( scores[0] * 100 ) )
	print( '\n' )


if __name__ == "__main__":
    main()
