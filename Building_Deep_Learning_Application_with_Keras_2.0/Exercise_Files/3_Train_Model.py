import pandas as pd
from keras.models import Sequential
from keras.layers import *

training_data_df = pd.read_csv("sales_data_training_scaled.csv")

X = training_data_df.drop('total_earnings', axis=1).values
Y = training_data_df[['total_earnings']].values

# Define the model
model = Sequential()
model.add(Dense(50, input_dim=9, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
# model.fit(training_data-->x,expected_output-->Y)
#  A single training pass across the entire training data set is called an epoch. Let's start with 50 passes or 50 epochs.
model.fit(X,Y,epochs=50,shuffle=True,verbose=2)

# Neural networks typically train best when the data is shuffled.
# So we'll pass in shuffle equals true. And then we're going to pass in one more parameter, verbose equals two.
# This just tells Keras to print more detailed information during training so we can watch what's going on.


# If we do too few passes, the neural network won't make accurate predictions,
# but if we do too many it will waste time, and it might also cause over fitting problems.
# The best way to tune this is to try training the neural network
# and stop doing additional training passes when the network stops getting more accurate.


# Load the separate test data set
test_data_df = pd.read_csv("sales_data_test_scaled.csv")

X_test = test_data_df.drop('total_earnings', axis=1).values # Input features
Y_test = test_data_df[['total_earnings']].values # Expected Output

# Testing phase : model.evaluate(testing_data,expected_output)

# I'm also going to pass in verbose equals zero,
# just so it doesn't print out extra log information that we don't need.
# The result from this call will be the error rate for the test data as measured by our cost function,
# and we'll store that in test error rate.

test_error_rate = model.evaluate(X_test,Y_test,verbose=0)
print("The mean squared error (MSE) for the test data set is: {}".format(test_error_rate))

# I'm also going to pass in verbose equals zero, just so it doesn't print out extra log information that we don't need.
# The result from this call will be the error rate for the test data as measured by our cost function, and we'll store that in test error rate.