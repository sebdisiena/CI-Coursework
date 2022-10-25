# provide: a truth table, a network structure diagram, the weights and biases, and a graphical state space 
# representation for perceptrons or MLPs that perform the following operations: AND, NAND, OR & XOR

import numpy
import matplotlib.pyplot as plt
from itertools import product

################# PERCEPTRON ############################################################
def perceptron(inputsList,weightsList, bias):
    # convert the input list into a numpy array
    inputs = numpy.array(inputsList)

    # convert the weight list into a numpy array
    weights = numpy.array(weightsList)

    # calculate the dot product
    summed = numpy.dot(inputs,weights)

    # add in the bias 
    summed = summed + bias

    # calculate the output
    output = 1 if summed > 0 else 0

    return output

######## INTERCEPT CALCULATION ##########################################################
def interceptCalc(weightsList, bias):

    xIntercept = -(bias / weightsList[0])
    yIntercept = -(bias / weightsList[1])

    return [xIntercept, 0], [0, yIntercept]

############## LOGIC GATE OPERATIONS ####################################################
def orOperation(inputsList):
    output = perceptron(inputsList, [2.0, 2.0], -1)
    interceptPlot = interceptCalc([2.0, 2.0], -1)
    return inputsList, output, interceptPlot

def andOperation(inputsList):
    output = perceptron(inputsList, [1.0, 1.0], -1)
    interceptPlot = interceptCalc([1.0, 1.0], -1)
    return inputsList, output, interceptPlot

def nandOperation(inputsList):
    output = perceptron(inputsList, [-1.0, -1.0], 1)
    interceptPlot = interceptCalc([-1.0, -1.0], 1)
    return inputsList, output, interceptPlot

def xorOperation(inputsList):
    output = andOperation([orOperation(inputsList), nandOperation(inputsList)])
    interceptPlotOr = interceptCalc([2.0, 2.0], -1)
    interceptPlotAnd = interceptCalc([1.0, 1.0], -1)
    return inputsList, output, interceptPlotOr, interceptPlotAnd

######## LOGIC GATE SIMULATION ##########################################################
def logicGateSimulation(inputLogicGate):
    inputs = [0,1]
    fig = plt.xkcd()
    plt.xlim(-1, 2)
    plt.ylim(-1, 2)
    plt.xlabel("Input 1")
    plt.ylabel("Input 2")
    plt.title("State Space Representation of " + logicGate + " Perceptron")

    for i1 in product(inputs, repeat = 2):
        if logicGate == "AND":
            [inputs, result, intercept] = andOperation(i1)
            print("AND Truth Table: ", inputs, " | ", result)
        elif logicGate == "OR":
            [inputs, result, intercept] = orOperation(i1)
            print("OR Truth Table: ", inputs, " | ", result)
        elif logicGate == "NAND":
            [inputs, result, intercept] = nandOperation(i1)
            print("NAND Truth Table: ", inputs, " | ", result)
        elif logicGate == "XOR":
            [inputs, result, interceptOr, interceptAnd] = xorOperation(i1)
            print("XOR Truth Table: ", inputs, " | ", result)
        
        if result == 1:
            plt.scatter(i1[0],i1[1],s=50,color="green",zorder=3)
        else: 
            plt.scatter(i1[0],i1[1],s=50,color="red",zorder=3)
    
    if logicGate == "XOR":
        plt.axline(interceptOr[0], interceptOr[1])
        plt.axline(interceptAnd[0], interceptAnd[1])
    else:
        plt.axline(intercept[0], intercept[1])
    plt.grid(True, linewidth=1, linestyle=':')
    plt.tight_layout()
    plt.show()

########### MAIN ########################################################################
logicGate = input("Select Logic Gate: ")
logicGateSimulation(logicGate)