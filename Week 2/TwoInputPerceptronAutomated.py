# import NumPy library for matrix math
import numpy
import matplotlib.pyplot as plt
from itertools import permutations
from itertools import product

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

# input A
inputs = [0,1]
weights = [1.0,1.0]
bias = -1

for i1 in product(inputs, repeat = 2):

    result = perceptron(i1,weights,bias)
    print("For Input: ", i1, "Result: ", perceptron(i1,weights,bias))
    inter_x = -(bias/weights[0]) 
    inter_y = -(bias/weights[1]) 
    intercept = [inter_x,0],[0,inter_y]

    func = lambda x: -(weights[0] / weights[1])*x - (bias / weights[1])
    intercept = [(0, func(0)), (1, func(1))]
    # make a new plot (XKCD syle)
    fig = plt.xkcd()

    # add points as scatters - scatter(x,y,size,color)
    # zorder determines the drawing order, set to 3 to make the grid lines appear behind the scatter points
    # if statement to set plot points to a particular color depending on the output of perceptron function
    if result == 1:
        plt.scatter(i1[0],i1[1],s=50,color="green",zorder=3)
    else: plt.scatter(i1[0],i1[1],s=50,color="red",zorder=3)

    
    plt.axline(intercept[0],intercept[1],color="blue")

# set the axis limits
plt.xlim(-2,2)
plt.ylim(-2,2)

# label the plot
plt.xlabel("Input 1")
plt.ylabel("Input 2")
plt.title("State Space of Input Vector")

# turn on grid lines
plt.grid(True,linewidth=1,linestyle=':')

# autosize (stops the labels getting cut off)
plt.tight_layout()

# show the plot
plt.show()