from ANN import NeuralNetwork
import itertools

def mnistNeuralNetworkLoop(totalIterations, target, inputs):
    inputNodes = 784
    hiddenNodes = 100
    outputNodes = 10
    learningRate = 0.3
    
    n = NeuralNetwork(inputNodes,hiddenNodes,outputNodes,learningRate)

    for i in range(totalIterations):
        for j in range(len(inputs)):
            n.train(inputs[j],target[j])

        output = n.query(inputs)
    
    print("Iterations Complete.")
    print(output)
    return output