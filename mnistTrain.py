import numpy
from ANN import NeuralNetwork
# load the MNIST 100 training samples CSV file into a list
training_data_file = open("mnist_train_100.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

inputNodes = 784
hiddenNodes = 100
outputNodes = 10
learningRate = 0.3
    
n = NeuralNetwork(inputNodes,hiddenNodes,outputNodes,learningRate)
# train the neural network on each training sample
for record in training_data_list:
    # split the record by the commas
    all_values = record.split(',')
    # scale and shift the inputs from 0..255 to 0.01..1
    inputs = (numpy.asfarray(all_values[1:])/255.0*0.99) + 0.01
    # create the target output values (all 0.01, except the desired label which is 0.99)
    targets = numpy.zeros(outputNodes) + 0.01
    # all_values[0] is the target label for this record
    targets[int(all_values[0])] = 0.99
    # train the network
    n.train(inputs,targets)
pass