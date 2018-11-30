# Emerging Technologies Assignment 2018 - neural network

A repo to hold Jupyter notebooks and a script file for Emerging technologies assignment.

Files in this project : <br>

**1. numpy random notebook** <br>
A jupyter notebook explaining the concepts behind and the use of the numpy random package, including plots of the various distributions.

**2. Iris dataset notebook** <br>
A jupyter notebook explaining the famous iris data set including the difficulty in writing an algorithm to separate the three classes of iris based on the variables in the dataset.

**3. MNIST dataset notebook** <br>
A jupyter notebook explaining how to read the MNIST dataset efficiently into memory in Python.

**4. Digit recognition script** <br>
A Python script that takes an image file containing a handwritten digit and identifies the digit using a supervised learning algorithm and the MNIST dataset.

**5. Digit recognition notebook** <br>
A jupyter notebook explaining how the above Python script works and discussing its performance.

**image files must be in black and white and must be 28 x 28.**
------
------
**Required to run this project.** 

* A folder added to the root directory of the project called data. 
* Inside the data folder the following 4 files : <br>
&nbsp;&nbsp;&nbsp;&nbsp;1. train-images-idx3-ubyte.gz:  training set images (9912422 bytes) <br>
&nbsp;&nbsp;&nbsp;&nbsp;2. train-labels-idx1-ubyte.gz:  training set labels (28881 bytes) <br>
&nbsp;&nbsp;&nbsp;&nbsp;3. t10k-images-idx3-ubyte.gz:   test set images (1648877 bytes) <br>
&nbsp;&nbsp;&nbsp;&nbsp;4. t10k-labels-idx1-ubyte.gz:   test set labels (4542 bytes)<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; These files can be downloaded from here : http://yann.lecun.com/exdb/mnist/ <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; No need to unzip them, the code can handle that.

* Working on this project I used Anaconda to simplify package management. download here : https://www.anaconda.com/download/
* With Anaconda installed you will need to open a cmd prompt with admin rights. (Search cmd on your machine, right click, open as admin.)
* The following commands will need to be run to add all the packages used : <br>
&nbsp;&nbsp;&nbsp;&nbsp;1. pip install jupyter <br>
&nbsp;&nbsp;&nbsp;&nbsp;2. conda install tensorflow <br>
&nbsp;&nbsp;&nbsp;&nbsp;3. conda install keras <br>
&nbsp;&nbsp;&nbsp;&nbsp;4. conda install -c anaconda scikit-learn <br>
&nbsp;&nbsp;&nbsp;&nbsp;5. conda update matplotlib <br>

------

To run the script:

* move to folder with script
* open command prompt 
* enter python digitrec.py


------
Author: Thomas Duffy.
