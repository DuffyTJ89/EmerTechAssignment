#adapted from in class notebook

print ('*** Python Neural Network Started ***')
print ('> Is the mnist dataset present in a folder titled "data" in the same directory as this script? Y/N')

datasetPresent = input("> ")

#if yes 
if datasetPresent == "y" or datasetPresent == "Y":
    #add gzip for unzipping the files
    import gzip
    with gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb') as f:
        file_content = f.read()

    # Import keras.
    import keras as kr

    # Start a neural network, building it by layers.
    model = kr.models.Sequential()

    # Add a hidden layer with 1000 neurons and an input layer with 784.
    model.add(kr.layers.Dense(units=600, activation='linear', input_dim=784))
    model.add(kr.layers.Dense(units=400, activation='relu'))
    # Add a three neuron output layer.
    model.add(kr.layers.Dense(units=10, activation='softmax'))

    # Build the graph.
    model.compile(loss='categorical_crossentropy', optimizer='Adamax', metrics=['accuracy'])

    with gzip.open('data/train-images-idx3-ubyte.gz', 'rb') as f:
        train_img = f.read()

    with gzip.open('data/train-labels-idx1-ubyte.gz', 'rb') as f:
        train_lbl = f.read()


    import numpy as np
        
    train_img = ~np.array(list(train_img[16:])).reshape(60000, 28, 28).astype(np.uint8) / 255.0
    train_lbl =  np.array(list(train_lbl[ 8:])).astype(np.uint8)

    inputs = train_img.reshape(60000, 784)

    # For encoding categorical variables.
    import sklearn.preprocessing as pre

    encoder = pre.LabelBinarizer()
    encoder.fit(train_lbl)
    outputs = encoder.transform(train_lbl)

    model.fit(inputs, outputs, epochs=25, batch_size=100)


#if no
elif datasetPresent == "n" or datasetPresent == "N": 
    print('> You cannot run this script without the dataset')

#catch the rest
else :
    print ('> Invailid response')

print ('*** Python Neural Network Finished ***')