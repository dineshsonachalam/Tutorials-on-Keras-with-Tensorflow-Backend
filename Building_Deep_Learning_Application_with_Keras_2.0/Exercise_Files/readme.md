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
# 7_Image_Recognition.py
- For ResNet 50 images we feed into the network need to be 224 pixels by 224 pixels. 
- So we need to resize the image before we can use it. Let's close the image and go back to our code.
- We can resize the image by adding a target size parameter. So we'll say target size equals and then pass in a tuple of 224 by 224. Keras will scale the image down to that size. 
- You might be thinking that 224 by 224 pixels is a low resolution image, but using low resolution images is common even in the latest image recognition models.
- Keeping the size of images as small as possible helps improve the processing speed by limiting the number of nodes you need in the neural network.
- All right, on line 12 we need to convert the image data into an array of plain numbers that we can feed into the neural network. 
- There's a built in helper function to do this called image.img to array. So we'll just call image.img to array and then we just pass in the name of our image data, which is img. 
- This will turn our image into a three dimensional array. The first two dimensions are the height and width of the image which will be 224 by 224. 
- The third dimension is color.
- We can do that on line 15 by calling NumPy's expand dims function. 
- So we call mp.expand dims and pass in the data and say that we want to expand on axis zero, which is the first axis. 
- Most images you have in your computer represent the red, green, and blue values of each pixel as one byte. 
- That means each value can range from zero to 255. 
- But neural networks work best with small numbers. So we need to normalize the data before we feed it to the neural network.
- This model has a built in normalization function called preprocess input that will do that for us. We just need to call it and pass in our data. So here on line 18 we'll call ResNet 50.preprocessed input and pass in X. 
- Now we are ready to run the normalized data through the neural network and make a prediction. 
- Let's go to line 21 and then we'll call model.predict and we'll pass in X the image data.
- This will return a predictions object. The predictions object is a 1,000 element array of floating point numbers. 
- Each element in the array tells us how likely our picture contains each of 1,000 objects the model is trained to recognize. 
- To make things easier, the ResNet 50 model provides a decode predictions function that will just tell us the names of the most likely matches, instead of making us check all 1,000 possible entries. On line 24, let's call that function. So we'll call ResNet 50.decode predictions, and we just pass in the predictions object.

- By default, it will give us the top five most likely matches, but if we add in top equals nine, we can get the top nine matches instead.
- Now here on line 28 we just loop through the predictions and print out each result. Okay, before we run the code, there's a couple of things we need to mention. 
- The first time you run this code, Keras will connect to the Internet and download the latest version of the ResNet 50 model. This means you'll need Internet access to run it, and around 100 megabytes of data will be downloaded.

***

# Export Keras logs in TensorFlow format:
TensorFlow comes with a great web-based tool called TensorBoard that lets us visualize our model's structure and monitor its training. To use TensorBoard we need our keras model to write log files in the format that TensorBoard can read. TensorBoard uses the information in these log files to generate its visualizations, let's add TensorBoard logging to our keras model. 
