from ANN import NeuralNetwork
import numpy
import matplotlib.pyplot as plt

# load the MNIST test samples CSV file into a list
test_data_file = open("mnist_test_10.csv",'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# scorecard list for how well the network performs, initally empty
scorecard = []

inputNodes = 784
hiddenNodes = 100
outputNodes = 10
learningRate = 0.3
    
n = NeuralNetwork(inputNodes,hiddenNodes,outputNodes,learningRate)

# loop through all of the records in the test data set 
for record in test_data_list:
    #split the record by the commas
    all_values = record.split(',')
    # the correct label is the first value
    correct_label = int(all_values[0])
    print(correct_label, "Correct Label")
    # scale and shift the inputs
    inputs = (numpy.asfarray(all_values[1:])/255.0*0.99) + 0.01
    # query the network
    outputs = n.query(inputs)
    #outputs = n.query(inputs)
    # the index of the highest value output corresponds to the label
    label = numpy.argmax(outputs)
    print(label,"Network Label")
    # append either a 1 or a 0 to the scorecard list
    if (label == correct_label):
        scorecard.append(1)
        image_array = numpy.asfarray(outputs[1:]).reshape((28,28))
        plt.imshow(image_array,cmap = 'Greys', interpolation = 'None')
        plt.show()
    else: 
        scorecard.append(0)
        pass
    pass

# calculate the performance score, the fraction of correct answers
scorecard_array = numpy.asarray(scorecard)
print("Performance = ", (scorecard_array.sum()/scorecard_array.size)*100, '%')