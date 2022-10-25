# import NumPy library for matrix math
import numpy

# a single perceptron function
def perceptron(inputs_list,weights_list, bias):
    # convert the input list into a numpy array
    inputs = numpy.array(inputs_list)

    # convert the weight list into a numpy array
    weights = numpy.array(weights_list)

    # calculate the dot product
    summed = numpy.dot(inputs,weights)

    # add in the bias 
    summed = summed + bias

    # calculate the output
    output = 1 if summed > 0 else 0

    return output

# main code starts here

# test the perceptron
inputs = [1.0,0.0]
weights = [1.0,1.0]
bias = -1

print("Inputs: ",inputs)
print("Weights: ",weights)
print("Bias:    ",bias)
print("Result: ",perceptron(inputs,weights,bias))
