# Keras
![](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/Building_Deep_Learning_Application_with_Keras_2.0/Pictures/1.png)
- Keras is designed to make it as easy as possible to build deep learning systems with as little complexity as possible. With Keras, you can build a deep neural network with only with only a few lines of code.

- Keras doesn't do all of the work itself. It's really a front-end layer written in Python that runs on top of other popular deep learning toolkits like TensorFlow and Theano. At abstracts away a lot of the complexity of using those tools while still giving you many of the benefits. 

- When you tell Keras to build a deep neural network, behind the scenes it builds out the neural network using either TensorFlow or Theano. 

- In this repository, we'll be using TensorFlow as the back-end. When you use Keras with TensorFlow, it builds a TensorFlow model and runs the training process for you.

- That means that your model is compatible with most tools and utilities that work with TensorFlow. You can even upload your Keras model to Google's Cloud Machine learning system. One of the core principles of Keras is that best practices are built in. When building a deep learning system, there are many different parameters you have to configure.

- Keras always tries to provide good defaults for parameters. The default setting used in Keras are based on what has worked well for researchers in the past.

- So more often than not, using the default settings in Keras will get you close to your goal. Even better, Keras comes with several pre-trained deep learning models for image recognition. You can use the pre-trained models to recognize common types of objects and images, or you can adapt these models to create a custom image recognition system with your own data.

***
![](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/Building_Deep_Learning_Application_with_Keras_2.0/Pictures/2.png)


***
![](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/Building_Deep_Learning_Application_with_Keras_2.0/Pictures/3.png)


***

![](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/Building_Deep_Learning_Application_with_Keras_2.0/Pictures/4.png)


***

![](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/Building_Deep_Learning_Application_with_Keras_2.0/Pictures/5.png)

***

![](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/Building_Deep_Learning_Application_with_Keras_2.0/Pictures/6.png)

***

![](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/Building_Deep_Learning_Application_with_Keras_2.0/Pictures/7.png)


***

# A simple Neural network:
![Neural Network](https://www.pyimagesearch.com/wp-content/uploads/2016/08/simple_neural_network_header.jpg)

***

# Train-Test-Evaluation flow with Keras:

### 1. Create a neural network model:
```sh
model = keras.models.Sequential()
# model object represents -> neural network we are building
# Once we have model object we add layers to neural network
model.add(keras.layers.Dense())
# Final step of defining a model is to compile.
# Keras uses tensorflow model for backend compilation.
model.compile(loss='mean_squared_error',optimizer='adam')
# To compile we need to tell keras two important things:
# 1st -> Tell how we want to measure the accuracy of each prediction during training phase [Loss Function]
# 2nd -> Keras Optimizer Algorithm
```
### 2. Training Phase:
- To train the model, we call model.fit and pass in the training data and the expected output for the training data. 
- Keras will run the training process and print out the progress to the console. 
- When training completes, it will report the final accuracy that was achieved with the training data. Once the model is trained, we're ready for the testing phase.

```sh
#  To train the model, we call model.fit and pass in the training data and the expected output for the training data
model.fit(training_data,expected_output)
```

### 3. Testing Phase:
```sh
error_rate = model.evaluate(testing_data,expected_output)
# When we are happy with accuracy we can save model to a file.
# To do that we call model.save
model.save("trained_model.h5")
# This model contains everything we need to use our model in another program.
```

### 4. Evaluation Phase:
We'll load our previously trained model by calling the load model function and passing in a file name. And then, to use the model to make new predictions, we just call the predict function and pass in the new data we want predictions for.
```sh
model = keras.models.load_model('trained_model.h5')
predictions = model.predict(new_data)
```

