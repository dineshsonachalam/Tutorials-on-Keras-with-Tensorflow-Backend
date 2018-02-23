# Introduction to Long Short Term Memory(LSTM):

Sequence Prediction Problems involves:

- Predicting sales for finding patterns in the stock market data.
- Understanding movie plots to recognize way of speech.
- Language translation to predict your next word on your iphone's keyboard.

LSTM provides the most effective solution for sequence prediction problems.

### 1. A look into RNN(Recurrent Neural Networks):

A stock market value depends on stock values from previous days.

##### Problem with conventional Feed-forward Neural Network:

- Here all test cases are considered to be independent.
- That is when fitting a model for a particular day, there is no consideration for stock prices on previous day.

This problem can be solved by using Recurrent Neural Network(RNN).

Here in RNN , the networks are considering the trend of stock prices, before predicting the stock prices for today.

A typical RNN looks like this.

![https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/12/05231650/rnn-neuron-196x300.png]()

Here every prediction at time t(h_t) is dependent on all previous prediction and the information learned from them.

![https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/12/06022525/bptt-768x313.png]()

RNNs can solve our purpose of sequence handling to a great extent but not entirely. RNNs are great when it comes to short contexts.

But in order to be able to build a story and remember it, we need our models to be able to understand and remember the context behind the sequences, just like a human brain. This is not possible with a simple RNN.

### 2. Limitations of RNN:

Lets take a problem:

> The color of the sky is ___________   

RNN is quite effective in predicting because it need not remember what was said before or what was its meaning.

The prediction would be,

> The color of the sky is blue

However RNN fails to understand context behind an input. Something that we said long before, cannot be recalled when making prediction in the present.

> I spent 20 years working for the under-privileged kids in Spain. I then moved to Africa.
>
> ......             
>
> I can speak fluent in __________________________               

Here, we can understand that since the author has worked in Spain for 20 years, it is very likely that he may possess a good command over Spanish. But, to make a proper prediction, the RNN needs to remember this context. The relevant information may be separated from the point where it is needed, by a huge load of irrelevant data. This is where a Recurrent Neural Network fails!   



A similar case is observed in Recurrent Neural Networks. RNN remembers things for just small durations of time, i.e. if we need the information after a small time it may be reproducible, but once a lot of words are fed in, this information gets lost somewhere. This issue can be resolved by applying a slightly tweaked version of RNNs – the Long Short-Term Memory Networks.          

### 3. Improvement over RNN: LSTM (Long Short-Term Memory) Networks:

When we arrange our calendar for the day, we prioritize our appointments right? If in case we need to make some space for anything important we know which meeting could be canceled to accommodate a possible meeting.



Turns out that an RNN doesn’t do so. In order to add a new information, it transforms the existing information completely by applying a function. Because of this, the entire information is modified, on the whole, i. e. there is no consideration for *‘important’ *information and *‘not so important’* information.



LSTMs on the other hand, make small modifications to the information by multiplications and additions. With LSTMs, the information flows through a mechanism known as cell states. This way, LSTMs can selectively remember or forget things. The information at a particular cell state has three different dependencies.



Lets take an example of predicting the stock prices for a particular stock. The stock prices for today will depend upon:

1. The trend that the stock has been following in the previous days, maybe a downtrend or an uptrend.
2. The price of the stock on the previous day, because many traders compare the stock’s previous day price before buying it.
3. The factors that can affect the price of the stock for today. This can be a new company policy that is being criticized widely, or a drop in the company’s profit, or maybe an unexpected change in the senior leadership of the company.  



These dependencies can be generalized to any problem as:

1. The previous cell state *(i.e. the information that was present in the memory after the previous time step)*
2. The previous hidden state *(i.e. this is the same as the output of the previous cell)*
3. The input at the current time step *(i.e. the new information that is being fed in at that moment)*

### 4. Architecture of LSTM:

The functioning of LSTM can be visualized by understanding the functioning of a news channel’s team covering a murder story. Now, a news story is built around facts, evidence and statements of many people. Whenever a new event occurs you take either of the three steps.

Let’s say, we were assuming that the murder was done by ‘poisoning’ the victim, but the autopsy report that just came in said that the cause of death was ‘an impact on the head’. Being a part of this news team what do you do? You immediately **forget **the previous cause of death and all stories that were woven around this fact.

What, if an entirely new suspect is introduced into the picture. A person who had grudges with the victim and could be the murderer? You **input **this information into your news feed, right?

Now all these broken pieces of information cannot be served on mainstream media. So, after a certain time interval, you need to summarize this information and **output **the relevant things to your audience. Maybe in the form of “*XYZ turns out to be the prime suspect.*”.

Now let’s get into the details of the architecture of LSTM network:

![https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/12/10131302/13-768x295.png]()

Now, this is nowhere close to the simplified version which we saw before, but let me walk you through it. A typical LSTM network is comprised of different memory blocks called **cells**(the rectangles that we see in the image)**. ** There are two states that are being transferred to the next cell; the **cell state** and the hidden state**. The memory blocks are responsible for remembering things and manipulations to this memory is done through three major mechanisms, called **gates. Each of them is being discussed below.

##### 4.1 Forget Gate

Taking the example of a text prediction problem. Let’s assume an LSTM is fed in, the following sentence:

> Bob is a nice person. Dan on other hand is evil.

As soon as the first full stop after “*person” *is encountered, the forget gate realizes that there may be a change of context in the next sentence. As a result of this, the *subject *of the sentence is *forgotten *and the place for the subject is vacated. And when we start speaking about “*Dan” *this position of the subject is allocated to “*Dan”*. This process of forgetting the subject is brought about by the forget gate.



A forget gate is responsible for removing information from the cell state. The information that is no longer required for the LSTM to understand things or the information that is of less importance is removed via multiplication of a filter. This is required for optimizing the performance of the LSTM network.



##### 4.2 Input Gate

Okay, let’s take another example where the LSTM is analyzing a sentence:

> Bob knows swimming. He told me over the phone that he had served navy for 4 long years.

Now the important information here is that “Bob” knows swimming and that he has served the Navy for four years. This can be added to the cell state, however, the fact that he told all this over the phone is a less important fact and can be ignored. This process of adding some new information can be done via the **input** gate.

![https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/12/10131330/16.png]()

The input gate is responsible for the addition of information to the cell state. This addition of information is basically three-step process as seen from the diagram above.

1. Regulating what values need to be added to the cell state by involving a sigmoid function. This is basically very similar to the forget gate and acts as a filter for all the information from h_t-1 and x_t.
2. Creating a vector containing all possible values that can be added (as perceived from h_t-1 and x_t) to the cell state. This is done using the **tanh **function, which outputs values from -1 to +1.  
3. Multiplying the value of the regulatory filter (the sigmoid gate) to the created vector (the tanh function) and then adding this useful information to the cell state via addition operation.

##### 4.3 Output Gate

Not all information that runs along the cell state, is fit for being output at a certain time. We’ll visualize this with an example:

![https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/12/10015531/b2_19-768x109.png]()

In this phrase, there could be a number of options for the empty space. But we know that the current input of *‘brave’,* is an adjective that is used to describe a noun. Thus, whatever word follows, has a strong tendency of being a noun. And thus, Bob could be an apt output.

This job of selecting useful information from the current cell state and showing it out as an output is done via the output gate.

​                                                              



[Useful link to understand what is RNN?](https://ayearofai.com/rohan-lenny-3-recurrent-neural-networks-10300100899b)





