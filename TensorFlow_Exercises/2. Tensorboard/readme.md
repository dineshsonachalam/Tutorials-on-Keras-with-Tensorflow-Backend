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
