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

for input1 in numpy.arange(0,1):
    for input2 in numpy.arrange(0,1):
        inputs = [input1,input2]



# test the perceptron
n1 = [0.0,0.0]
n2 = [0.0,1.0]
n3 = [1.0,0.0]
n4 = [1.0,1.0]
w1 = [0.0,0.0]
w2 = [0.0,1.0]
w3 = [1.0,0.0]
w4 = [1.0,1.0]
b1 = -1
b2 = 0
b3 = 1

print("N1: ",n1)
print("N2: ",n2)
print("N3: ",n3)
print("N4: \n",n4)

print("W1: ",w1)
print("W1: ",w2)
print("W1: ",w3)
print("W1: \n",w4)

print("B1:    ",b1)
print("B2:    ",b2)
print("B3:    \n",b3)

print("N111 Result: ",perceptron(n1,w1,b1))
print("N211 Result: ",perceptron(n2,w1,b1))
print("N311 Result: ",perceptron(n3,w1,b1))
print("N411 Result: \n",perceptron(n4,w1,b1))

print("N112 Result: ",perceptron(n1,w1,b2))
print("N212 Result: ",perceptron(n2,w1,b2))
print("N312 Result: ",perceptron(n3,w1,b2))
print("N412 Result: \n",perceptron(n4,w1,b2))

print("N113 Result: ",perceptron(n1,w1,b3))
print("N213 Result: ",perceptron(n2,w1,b3))
print("N313 Result: ",perceptron(n3,w1,b3))
print("N413 Result: \n",perceptron(n4,w1,b3))

print("N121 Result: ",perceptron(n1,w2,b1))
print("N221 Result: ",perceptron(n2,w2,b1))
print("N321 Result: ",perceptron(n3,w2,b1))
print("N421 Result: \n",perceptron(n4,w2,b1))

print("N122 Result: ",perceptron(n1,w2,b2))
print("N222 Result: ",perceptron(n2,w2,b2))
print("N322 Result: ",perceptron(n3,w2,b2))
print("N422 Result: \n",perceptron(n4,w2,b2))

print("N123 Result: ",perceptron(n1,w2,b3))
print("N223 Result: ",perceptron(n2,w2,b3))
print("N323 Result: ",perceptron(n3,w2,b3))
print("N423 Result: \n",perceptron(n4,w2,b3))

print("N131 Result: ",perceptron(n1,w3,b1))
print("N231 Result: ",perceptron(n2,w3,b1))
print("N331 Result: ",perceptron(n3,w3,b1))
print("N431 Result: \n",perceptron(n4,w3,b1))

print("N132 Result: ",perceptron(n1,w3,b2))
print("N232 Result: ",perceptron(n2,w3,b2))
print("N332 Result: ",perceptron(n3,w3,b2))
print("N432 Result: \n",perceptron(n4,w3,b2))

print("N133 Result: ",perceptron(n1,w3,b3))
print("N233 Result: ",perceptron(n2,w3,b3))
print("N333 Result: ",perceptron(n3,w3,b3))
print("N433 Result: \n",perceptron(n4,w3,b3))

print("N141 Result: ",perceptron(n1,w4,b1))
print("N241 Result: ",perceptron(n2,w4,b1))
print("N341 Result: ",perceptron(n3,w4,b1))
print("N441 Result: \n",perceptron(n4,w4,b1))

print("N142 Result: ",perceptron(n1,w4,b2))
print("N242 Result: ",perceptron(n2,w4,b2))
print("N342 Result: ",perceptron(n3,w4,b2))
print("N442 Result: \n",perceptron(n4,w4,b2))

print("N143 Result: ",perceptron(n1,w4,b3))
print("N243 Result: ",perceptron(n2,w4,b3))
print("N343 Result: ",perceptron(n3,w4,b3))
print("N443 Result: \n",perceptron(n4,w4,b3))