import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load training data set from CSV file
training_data_df = pd.read_csv("sales_data_training.csv")

# Load testing data set from CSV file
test_data_df = pd.read_csv("sales_data_test.csv")

# Data needs to be scaled to a small range like 0 to 1 for the neural
# network to work well.
scaler = MinMaxScaler(feature_range=(0,1))

# Scale both the training inputs and outputs

# Fit transform means we want it to first fit the scaler to our data,
#  but figure out how much to scale down the numbers in each column and
# then we want it to actually transform or scale the data.
#  Now, on the next line we want to scale the test data the same way,

scaled_training = scaler.fit_transform(training_data_df)

# Calling transform instead of fit transform
#  means the scaler applies the same amount of scaling to the test data as the training data.
scaled_testing = scaler.transform(test_data_df)

# Print out the adjustment that the scaler applied to the total_earnings column of data
print("Note: total_earnings values were scaled by multiplying by {:.10f} and adding {:.6f}".format(scaler.scale_[8], scaler.min_[8]))

# Create new pandas DataFrame objects from the scaled data
scaled_training_df = pd.DataFrame(scaled_training, columns=training_data_df.columns.values)
scaled_testing_df = pd.DataFrame(scaled_testing, columns=test_data_df.columns.values)

# Save scaled data dataframes to new CSV files
scaled_training_df.to_csv("sales_data_training_scaled.csv", index=False)
scaled_testing_df.to_csv("sales_data_test_scaled.csv", index=False)

# To Note:
# Newly created csv file sales_data_training_scaled.csv &  sales_data_test_scaled.csv are scaled between 0 and 1.
# Here the highest value in the column will hold the value 1
# Here the lowest value in the column will be holding the value 0.
# The remaining columns will have values between 0.1 to 0.9