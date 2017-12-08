import numpy as np
from keras.datasets import cifar10
from matplotlib import pyplot as plt
from scipy.misc import toimage
from PIL import Image
import PIL
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


(x_train, y_train), (x_test, y_test) = cifar10.load_data()

model = Sequential()

def architecture_cnn( model ):

	model.add( Conv2D( 16, (2 , 2), input_shape = ( 32, 32, 3 ),
				kernel_initializer = 'glorot_uniform',
				strides = ( 1, 1 ),
				padding = 'same',
				activation = 'relu' ) )

	# hidden layers
	model.add( Activation( 'relu' ) )

	model.add( Dropout( 0.4 ) )

	model.add( MaxPooling2D( pool_size = ( 2, 2 ) ) )

	model.add( Conv2D( 18, ( 2, 2 ), strides = ( 2, 2 ), activation = 'relu', padding = 'same' ) )

	model.add( Flatten() )

	model.add( Dense( 12, activation = 'relu' ) )

	model.add( BatchNormalization() )

	model.add( Activation( 'relu' ) )

	model.add( Dropout( 0.5 ) )

	# classification layer
	model.add( Dense( 10, activation = 'softmax' ) )

	# backpropagation
	lrate  = 0.2
	sgd    = SGD( lr = lrate, 
					momentum = 0.7, 
					decay = 0.0005, 
					nesterov = True, 
					clipnorm = 1., 
					clipvalue = 0.5 )

	model.compile( loss = 'sparse_categorical_crossentropy', 
					optimizer = 'sgd', 
					metrics = ['accuracy'] )

	return model

def resize_image( img ):

	wsize = 32
	hsize = 32

	img = img.resize((wsize, hsize), PIL.Image.ANTIALIAS)
	
	return img

def predicting_label( img ):

	modelS = architecture_cnn( model )
	modelS.load_weights( 'bias/recg.h5', by_name = False )

	label = ''

	x_pred = np.zeros( shape = ( 1, 32, 32, 3 ), dtype = np.uint8 )

	imgResize = resize_image( img )
	x_pred[0] = np.asarray( imgResize )

	x_pred = x_pred.astype( 'float32' )
	x_pred = x_pred / 255.0

	predictions = model.predict( x_pred )

	classes = [ 'airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck' ]
	for i in range( x_pred.shape[0] ):
		b = list( predictions[i] )
		first_max = sorted( predictions[i] )[-1]

	label = classes[b.index( first_max )]

	return label
