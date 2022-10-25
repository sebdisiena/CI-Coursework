# N = NeuralNetwork(self, input_nodes, hidden_nodes, output_nodes, learning_rate)
from ANN import NeuralNetwork
import itertools

def TwoInputNeuralNetworkLoop(totalIterations):
    inputNodes = 2
    hiddenNodes = 4
    outputNodes = 1
    learningRate = 1
    
    N = NeuralNetwork(inputNodes,hiddenNodes,outputNodes,learningRate)

    inputs = [[0.0,0.0],
              [0.0,1.0],
              [1.0,0.0],
              [1.0,1.0]]

    logicGate = input("Enter Logic Gate: ")
    if logicGate == "AND":
        target = [0.0,0.0,0.0,1.0]
    elif logicGate == "OR":
        target = [0.0,1.0,1.0,1.0]
    elif logicGate == "XOR":
        target = [0.0,1.0,1.0,0.0]
    elif logicGate == "NOR":
        target = [1.0,0.0,0.0,0.0]
    else: print("Incorrect Input")

    for i in range(totalIterations):
        for j in range(len(inputs)):
            N.train(inputs[j],target[j])

        output = N.query(inputs)
    
    print("Iterations Complete.")
    print(output)
    return output
    

def FourInputNeuralNetworkLoop(totalIterations):
    inputNodes = 4
    hiddenNodes = 4
    outputNodes = 1
    learningRate = 1
    
    N = NeuralNetwork(inputNodes,hiddenNodes,outputNodes,learningRate)

    inputs = list(itertools.product([0,1],repeat = 4))
    print(inputs)

    logicGate = input("Enter Logic Gate: ")
    if logicGate == "AND":
        target = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    elif logicGate == "OR":
        target = [0.0,1.0,1.0,1.0]
    elif logicGate == "XOR":
        target = [0.0,1.0,1.0,0.0]
    elif logicGate == "NOR":
        target = [1.0,0.0,0.0,0.0]
    else: print("Incorrect Input")

    for i in range(totalIterations):
        for j in range(len(inputs)):
            N.train(inputs[j],target[j])

        output = N.query(inputs)
    
    print("Iterations Complete.")
    print(output)
    return output

numberInputs = input("2 or 4 inputs?")
if numberInputs == "2":
    TwoInputNeuralNetworkLoop(5000)
elif numberInputs == "4":
    FourInputNeuralNetworkLoop(5000)
else: print("Incorrect Selection")
