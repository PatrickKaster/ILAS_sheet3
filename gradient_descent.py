#!/usr/bin/env python3
from optparse import OptionParser
import random
import itertools

parser = OptionParser()
parser.add_option("-e", "--eta", dest="eta_value", help="size of steps", metavar="VALUE", type="float")

(options,args) = parser.parse_args()

class Example:
    def __init__(self,values,outcome):
        self.values = values
        self.outcome = outcome

    def __str__(self):
        return str(self.values) + " : " + str(self.outcome)

def perceptron_output(weights,values):
    """
    computes the output of one perceptron
    """
    if len(weights) != len(values):
        # hier soll eigentlich eine exception geworfen werden
        return 0
    acc = 0
    for i in range(len(weights)):
        acc += weights[i]*values[i]
    return 1 if( acc > 0 ) else -1

def get_small_random_value():
    """
    function returns a value x in [0,0.1)

    I would consider this as a small random number as demanded in the algorithm if one consideres the
    """
    return random.uniform(0,0.1)


def gradient_descent(eta,examples):
    # initialize weights with small random integers
    weight = [get_small_random_value() for i in range(len(examples[0].values))]
    #while condition is not met
    while True:
        # initialize delta of weights 
        weight_delta = [0 for i in range(len(examples[0].values))]
        for example in examples:
            output = perceptron_output(weight,example.values)
            for weight_idx in range(len(weight)):
                weight_delta[weight_idx] += eta*(example.outcome - output)*example.values[weight_idx]

        for weight_idx in range(len(weight)):
            weight[weight_idx] += weight_delta[weight_idx]

        # termination criterion: terminate if there is a weight_delta which is greater than eta
        terminate = True
        for d in weight_delta:
            if d > eta:
                terminate = False
        if terminate:
            break
    return weight

def f(x,y,z):
    return x and ( y or z )

# generate all possible examples for the given function
examples = []
for x in itertools.product('01',repeat=3):
    arguments = [int(i) for i in x]
    examples.append(Example(arguments, f(*arguments)))

# run gradient descent on the given examples
weights = gradient_descent(0.1,examples)
for w in weights:
    print(w)
