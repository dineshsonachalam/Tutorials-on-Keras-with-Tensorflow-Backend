# 5_Save_Trained_Model.py
- So far, we've always retrained the neural network every time we've used it. 
- Can you think of an issue with this approach? Large neural networks can take hours or days to train. 
- Instead of retraining each time we run our program, we can train it once, and save the result to a file. 
- Then, whenever we want to use the neural network, we can just load it back up and use it. First let's look at how to save a model in Keris. 
- When you save the model, it saves both the structure of the neural network and the trained weights that determine how the neural network works. 
- The reason I used the h five file name extension is because the data will be stored in the h d f five format.
- H d f five is a binary file format designed for storing Python array data. The convention is to used h five as the file name extension but it's not required. 
***
# 6_Load_Saved_Model.py
- Here on line four, let's load their model from disk by calling load underscore model. Then we just pass in the file name of the model we want to load. In this case trained model dot h five.
- Since the file contains the structure and training parameters, this single line recreates our entire trained neural network. 
- We don't have to re-declare the structure of our neural network again. Now let's use the trained neural network to make a prediction. 
- We can use the model we loaded exactly like any other model. First on line six, we load the data that we want to use to make a prediction for. 
- Then on line seven, we make a prediction for the data by calling model dot predict and passing in that data. Then on line 10 we grab the prediction.
- And on lines 14 and 15 we scale the data from the zero to one range back to dollars.

***


