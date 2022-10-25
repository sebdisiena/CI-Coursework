from ANN import NeuralNetwork
import numpy
import matplotlib.pyplot as plt

smallMnistTrain = "D:/Uni/Semester 1/EE40098 Computational Intelligence/Coursework A/exercise2/datasets/mnist_train_100.csv"
largeMnistTrain = "D:/Uni/Semester 1/EE40098 Computational Intelligence/Coursework A/exercise2/datasets/mnist_train.csv"
smallMnistTest = "D:/Uni/Semester 1/EE40098 Computational Intelligence/Coursework A/exercise2/datasets/mnist_test_10.csv"
largeMinstTest = "D:/Uni/Semester 1/EE40098 Computational Intelligence/Coursework A/exercise2/datasets/mnist_test.csv"

smallFashTrain = "D:/Uni/Semester 1/EE40098 Computational Intelligence/Coursework A/exercise2/datasets/fashion_mnist_train_1000.csv"
largeFashTrain = "D:/Uni/Semester 1/EE40098 Computational Intelligence/Coursework A/exercise2/datasets/fashion_mnist_train.csv"
smallFashTest = "D:/Uni/Semester 1/EE40098 Computational Intelligence/Coursework A/exercise2/datasets/fashion_mnist_test_10.csv"
largeFashTest = "D:/Uni/Semester 1/EE40098 Computational Intelligence/Coursework A/exercise2/datasets/fashion_mnist_test.csv"

def mnistTrain(trainDataSet):
    training_data_file = open(trainDataSet, 'r')
    training_data_list = training_data_file.readlines()
    training_data_file.close()
    
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

def mnistTest(testDataSet):
    # load the MNIST test samples CSV file into a list
    test_data_file = open(testDataSet,'r')
    test_data_list = test_data_file.readlines()
    test_data_file.close()

    scorecard = []

    # loop through all of the records in the test data set 
    for record in test_data_list:
        #split the record by the commas
        all_values = record.split(',')
        # the correct label is the first value
        correct_label = int(all_values[0])
        # scale and shift the inputs
        inputs = (numpy.asfarray(all_values[1:])/255.0*0.99) + 0.01
        # query the network
        outputs = n.query(inputs)
        #outputs = n.query(inputs)
        # the index of the highest value output corresponds to the label
        label = numpy.argmax(outputs)
        print(correct_label, "Correct Label", label,"Network Label")
        # append either a 1 or a 0 to the scorecard list
        if (label == correct_label):
            scorecard.append(1)
            #image_array = numpy.asfarray(outputs[1:]).reshape((28,28))
            #plt.imshow(image_array,cmap = 'Greys', interpolation = 'None')
            #plt.show()
        else: 
            scorecard.append(0)
            pass
    pass

    # calculate the performance score, the fraction of correct answers
    scorecard_array = numpy.asarray(scorecard)
    performance = (scorecard_array.sum()/scorecard_array.size)*100
    print("Performance = ", performance, '%')

def neuronNumberOptimisation():
    for i in range (50, 1000, 50):
        n = NeuralNetwork(inputNodes, (i), outputNodes, learningRate)
        mnistTrain(smallMnistTrain)
        mnistTest(smallMnistTest)
        print(i)
    pass

def learningRateOptimisation():
    pass

def iterationNumberOptimisation():
    pass

def optimisedSystem():
    pass

##### MAIN #################################################################################################

inputNodes = 784
hiddenNodes = 800
outputNodes = 10
learningRate = 0.1
n = NeuralNetwork(inputNodes,hiddenNodes,outputNodes,learningRate)
neuronNumberOptimisation()
