# Start Tensorboard server (< 1 min)
Open a terminal window in your root project directory. Run:

```
tensorboard --logdir=tensorboard --logdir="C:\Users\Dinesh\Desktop\Tensorflow-Basics\TensorFlow_Exercises\2. Tensorboard\logs"
```
Go to the URL it provides OR on windows:
```
http://localhost:6006/
```
***

# Graphical Representation in TensorBoard:
![](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/Pictures/Graph_Representation_Tensorflow.png)

***

# Visualizing training in TensorBoard
1. Open Visualize_training.py
2. Let's say that we want to retrain this neural network several times, with a different number of nodes in the first layer each time. 
3. Our goal is to find out which neural network design gives us the best prediction accuracy. 
4. The problem is that each time we run the training process, additional log files will be created with the same name as the old log files. 
5. The new log files will mix with the old log files and create overlapping graphs in TensorBoard. 
6. We won't have any way to tell which training run was which. We can fix this by using a different run name for each training run.
7.Here's how it works. First, if you already have a logs folder here in PyCharm, let's right click and delete the folder before we get started. Right click, delete, and click delete. 
8.Okay, let's go up to line 37. Let's create the variable called RUN_NAME. This will just be a string where we can give a name to the current training run. Let's start with "run 1 with 50 nodes". Now let's go back down to line 104.
9.Currently every log file is named exactly the same way. 
10. Let's change how we are creating the log file names, so that we can separate them per run. All we have to do is put each run in a different subfolder.
11. Then we are going back to line 37, after log/run 1 with 50 nodes been created. This time we are going run with 20 nodes in the layer1.
12. Then start TensorBoard server.
13. In TensorBoard we can view find out which neural network design gives us the best prediction accuracy that is run 1 with 50 nodes or run2 with 20 nodes.
14. As we trace the line here, we can see that run 1 had a lower cost[less error] the entire time than run 2. So it looks like having 50 nodes in the first layer is working better than having 20 nodes. These graphs also update automatically every minute as you train.
![](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/Pictures/cost_comparison_50_nodes_vs_20_nodes.png)

***

# Adding Histogram in TensorBoard
1. Open custom_visualization.py
2. In line 94, add `tf.summary.histogram('predicted_value',prediction)` to add custom histogram visualization for predictions.
3. Then run this python file and a log value is created.
4. Start TensorBoard Server by openning a terminal window in your root project directory. Run:

```
tensorboard --logdir=tensorboard --logdir="C:\Users\Dinesh\Desktop\Tensorflow-Basics\TensorFlow_Exercises\2. Tensorboard\logs"
```
Here,
At the top of TensorBoard click Histograms to see our new histogram. And then expand the logging subsection. Now to look at one of these charts in more detail let's click the Expand button. This chart shows us the range of predictions our neural network made each step during training. Back here at step zero, we can see the predictions made were very low and all grouped together. But as we move forward in time, we can see that the learn to make predictions with a wider range of values.

Because our data was scaled to the zero to one range, we'd expect the predictions right out of the neural network to roughly cover that same zero to one range.
![](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/Pictures/histogram_1.png)
![](https://github.com/dineshsonachalam/Tensorflow-Basics/blob/master/Pictures/histogram_2.png)
