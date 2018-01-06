import os
import tensorflow as tf

# Turn off TensorFlow warning messages in program output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import pandas as pd
from keras.models import Sequential
from keras.layers import *



training_data_df = pd.read_csv("sales_data_training_scaled.csv")

X = training_data_df.drop('total_earnings', axis=1).values # X contain all input features of each game.
Y = training_data_df[['total_earnings']].values # y contain only expected earnings of each game.

# Define the model
model = Sequential()
model.add(Dense(50,input_dim=9,activation='relu'))
model.add(Dense(100,activation='relu'))
model.add(Dense(50,activation='relu'))

# The final output of our Neural Network should be a single number that represents the amount of money we predict a single game will earn.
#  So the last layer of our Neural Network needs to have exactly one output node.
#  So we'll say model.add Create a new dense layer. And have one node in it. Our predicted value for earnings should be a single linear value.
# So we won't use a ReLU activation function. Instead, for the last layer, we'll use a linear activation function.
model.add(Dense(1,activation='linear')) # last layer is the ouput layer so 1 node, predicted value  should be 'single linear'
model.compile(loss='mean_squared_error',optimizer='adam')