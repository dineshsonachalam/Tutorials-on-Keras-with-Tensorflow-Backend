# Tensorflow Basics Tutorial
![](https://lh3.googleusercontent.com/hIViPosdbSGUpLmPnP2WqL9EmvoVOXW7dy6nztmY5NZ9_u5lumMz4sQjjsBZ2QxjyZZCIPgucD2rhdL5uR7K0vLi09CEJYY=s688)

# What is Tensorflow?
- A software framework for building and deploying machine learning models.
- Tensorflow gives you the basic building blocks that you need to design,train and deploy machine learning models.
- Its typically used to build deep neural networks.
- Deep neural networks built with Tensorflow used in many different areas

   1. **Image recognition** - Where you recognize what object appear in a picture.
   2. **Speech recognition** - Where you turn speech into text.
   3. In particular course, well use Tensorflow to solve typical business problem of estimating sales.

- Tensorflow is a low level toolkit. It takes few lines of code to build machine learning model in Tensorflow. Because of this there are wrappers for tensorflow that simplify common operations. The most popular wrapper with tensorflow is keras.

- **keras** - High-level tensorflow wrapper for building neural networks with only a few lines of code. 



# Basic Questions:
1. What is a tensorflow session?

    An object that runs on the computation graph and tracks the state of each node in the graph.
2. The Google Cloud SDK is a set of command-line utilities that can be used to interactive with the Google Cloud service from your local computer.

    True

3. Before training a neural network, it's often necessary to scale the data so all the values are between 0 and 1.

   True


***
# Why it is called Tensorflow?

Any data to be processed by Tensorflow has to be stored in a multidimensional array(Also called 'Tensors')
- Similar to a flow chart in Tensorflow data flow from 1 operation to that of the another operation. So it is called tensorflow.


***
#  Supervised Learning:
The branch of Machine Learning where the computer learns how to perform a function by looking at labelled training data.

![](https://wiki.seg.org/images/1/10/Machine_learning_workflow_.png)

Step 1: Choose a Machine Learning Model.For example we can take **Neural Networks**

Step 2: Training Phase:

`Testing data ---> Supervised Learning Model ---> Correct Output`

Step 3: Testing Phase:

`Testing data ---> Supervised Learning Model ---> Predicted output`

Step 4: Evaluation Phase:

`New data ---> Trained Supervised Learning Model ---> Predicted Answer`


***

# Train,Test / Evaluation in TensorFlow:

First we code our machine learning algorithm. We'll do that by building a computational graph of operations that TensorFlow can run. Here's how we'll implement a neural network.

Step 1: Build a Model (as a Graph) 
![](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/Pictures/tensorflow_computation_model.png)

- First we'll define each layer of the neural network and connect them together so that data flows from the first layer through to the last layer.
- We'll add the placeholder node that represents the data that will be fed in as input to the neural network. 
- And another placeholder node that represents the output, or values predicted by the neural network. 
- Next, we need a way to measure the accuracy of the neural network's predictions. 
- We'll define the **function that measures the accuracy of each prediction during the training process**. This is called a **loss function**. 
- The loss function gets added to the graph as its own operation. Then we have to create an optimizer function that tells TensorFlow how we want to train the model.
- When we run this function, it will perform one training step on our model. 
- TensorFlow provides many pre-built optimizer functions so usually we just have to tell it which one to use and we don't need to implement custom code. 
- We'll call this node the training operation. The training operation will train the neural network by looking at the results of the loss function and using that to adjust the weights of each layer in the neural network until they produce the desired output.
- Because this is a computational graph, there's no single start or end. We can start processing at any node in the graph.

### For example:
- If we want to run one step of training, we can run the training operation. 
- And if we want to make a prediction for new data, we can run the output operation.
- When you run an operation, TensorFlow will push any needed data through the network according to the pathways you defined to make everything work. 
- Now that the machine learning algorithm is fully defined as a computational graph, we can move on to the training phase. 
 But before we can execute any of the operations in our graph, we have to create a Tensorflow session.

### Tensorflow Session:
A session is an object intenser flow that runs operations on the graph and tracks the state of each node in the graph.
- Once the session object is created, we can ask it to run any operation in the graph. 
- To train the model, we'll call the training operation over and over. 
- Each time the training operation runs, we'll pass a new training data that will be used for that training pass. And then we'll check the current accuracy by calling the loss function.

### TensorBoard:
- TensorBoard is a web based application that lets us visually monitor the system in real time. 
- We can use the graphs in -TensorBoard to monitor how the accuracy is improving as the training process continues to run. - Now that the model is trained, we can move on to the testing phase. 
- We pass in test data, and then measure the accuracy by calling the loss function. 
- The data will flow through the neural network and into the loss function.
- The loss function will tell us how close the values predicted by the neural network were to the real testing data.

Once we are happy with the accuracy of the predictions, we can save this model to a file. When we save a trained model, we're actually writing out a copy of this graph, and the state of all nodes in the graph. When we load the model later, we're just restoring the graph to it's previous state. Now that we have a trained model, we'll load it up to restore the graph. To use the model to make new predictions, we'll feed in data to the input node and call the output operation.


***
# Addition in Tensorfow:

[ [ x & y Input_data ----> Addition Operation ] [Session] ]

- Lets build a computational graph that add two numbers together. Graph has one operation called 'addition'.
- Simply adds together the tensors(Multi-Dimensional array) passed into it.
- Once the graph is defined. We create new TensorFlow Session. Then we'll feed in values for X and Y, and we'll ask the session object to execute the addition node. The result we get after executing addition node is the answer.

[Addition_TensorFlow_model.py](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/TensorFlow_Exercises/1.%20Training%20a%20model%20in%20Tensor%20Flow/1_Addition_Basic_TensorFlow_Model)


***


# Options for Loading data

### 1. Preload data into the memory:
- Is quick and easy.
- Works as long as the entire data set fits into RAM.
- Uses normal Python code with Nothing TensorFlow specific.
- Can use helpful Python libraries like Pandas

### 2. Feed data Step-by-Step:
- TensorFlow calls the custom data loader function each time it needs more data.
- This makes it possible to work with larger datasets.
- Normal Python Code is used.

### 3. Setup a data pipeline:
- Scales to infinitely large datasets.
- Require writing TensorFlow-specific code.
- Support parallel processing.

![](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/Pictures/data_pipeline_example.png)

### Recommended:
1. Use the simplest solution(Preloading) if possible.
2. Build a data pipeline if your dataset becomes too large.
3. Only add more complexity when you need it.
***
# Start Tensorboard server (< 1 min)
Open a terminal window in your root project directory. Run:

```
tensorboard --logdir="C:\Users\Dinesh\Desktop\Ex_Files_TensorFlow\Ex_Files_TensorFlow\Exercise Files\04\logs"
```
Go to the URL it provides OR on windows:
```
http://localhost:6006/
```

# Installation:
- Install [Anaconda](https://www.anaconda.com/download/) Python 3.6 version.
- Download and install [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) Community edition.

- Install tensorflow on windows

Take the following steps to install TensorFlow in an Anaconda environment:



1. Create a conda environment named tensorflow by invoking the following command:

`C:> conda create -n tensorflow python=3.5 `

2. Activate the conda environment by issuing the following command:

`C:> activate tensorflow`
 `(tensorflow)C:>  # Your prompt should change `

3. Issue the appropriate command to install TensorFlow inside your conda environment. To install the CPU-only version of TensorFlow, enter the following command:

`(tensorflow)C:> pip install --ignore-installed --upgrade tensorflow `

- To install the GPU version of TensorFlow, enter the following command (on a single line):

`(tensorflow)C:> pip install --ignore-installed --upgrade tensorflow-gpu `




# To Do:

1. - [ ]   [Learn TensorFlow and deep learning, without a Ph.D.]()https://cloud.google.com/blog/big-data/2017/01/learn-tensorflow-and-deep-learning-without-a-phd
2. - [ ]  [Stanford tensorflow Tutorials](https://github.com/chiphuyen/stanford-tensorflow-tutorials)
3. - [ ]  [MIT Self Driving Cars](https://selfdrivingcars.mit.edu/resources/)
4. - [ ] [Pathyway to Deep Learning](http://adventuresinmachinelearning.com/neural-networks-tutorial/)









