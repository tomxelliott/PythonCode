from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)

# load 2003data.csv dataset
dataset = numpy.loadtxt("2005data.csv", delimiter=",")
# split into input (X) and output (Y) variables
# First 36 are input variables
# 37th is output variable
# 37 total variables
X = dataset[:,0:36]
Y = dataset[:,36]

# create model
# Rectifier (‘relu‘) activation function on the first two layers and the sigmoid ('sigmoid') function in the output layer
model = Sequential()
model.add(Dense(12, input_dim=36, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
# Specify loss function - in this case:
# use logarithmic loss, which for a binary classification problem is defined in Keras as “binary_crossentropy“.
# “adam” is an efficient gradient descent algorithm. Look at other options as well.
# metrics=['accuracy'] reports the classification accuracy of the model.
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
# we will run for a small number of iterations (150) and use a relatively small batch size of 10. 
# Again, these can be chosen experimentally by trial and error.
# can add , verbose=0 ,  parameter to to the fit() method to stop the bars when running model.
model.fit(X, Y, epochs=150, batch_size=10, initial_epoch=0)

# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
