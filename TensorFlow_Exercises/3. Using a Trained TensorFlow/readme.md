# export_model_cloud.py
1. At the end of the training loop we want to export the train model, but because we want to use the model in the cloud, we can't use the normal tf.train.saver function to save the model. Instead, we're going to use TensorFlow's saved model builder that let's us customize how the model is exported. 

2. First, let's go all the way down to line 149.

3. Now, let's create a new saved model builder object. The full name is tf.saved_model.builder.SavedModelBuilder. The only parameter we have to pass in is the name of the folder we want to save the model file to. I'm going to use exported model.
 
4. Now we're ready to define the inputs and outputs of the model that we want Google to use when it runs the model in the cloud. 

5. First, we have a Python dictionary with a key called inputs.

6. In this dictionary, we'll list each tensor that needs to be filled in when their model is run. Our model takes in one tensor with nine values as input, so that means our model will have one input. We'll just call it input. For the value of the input key, we'll pass in the tensor we want data fed into. In this case, it will be X, but to make this work we also need to wrap that tensor in the call to a function called tf.saved_model.utils.build_tensor_info, like this, and then pass in X.

7. We create the signature def by calling this tf.saved_model.signature_def_utils.build_signature_def then we'll pass in the inputs and outputs we just defined. So the inputs will be the inputs dictionary and the outputs will be the outputs dictionary. Then we have to name the method we are defining, but we won't make up a name, we'll always use the special predefined function name called tf.saved_model.signature_constants.PREDICT_METHOD_NAME.

8. That's the name Google will always look for in order to execute our model. Great, we've defined the inputs, the outputs, and the signature def. Now we're ready to configure the model builder to tell it exactly how we want this model exported. Let's go down to line 164 and then we can call the model_builder.add_meta_graph_and_variables function. That names a mouthful, but meta graph is the structure of our computational graph and the variables are the values we set on each node in the graph. So this is telling TensorFlow that we want to export everything.

9. We can see here in PyCharm a new exported model folder and inside is a file called saved_model.pb. This file contains the structure of our model in Google's special proto buff format. There's also a variables subfolder that contains a checkpoint of all the variables in our graph. This model is now ready to be uploaded to the Google cloud.
