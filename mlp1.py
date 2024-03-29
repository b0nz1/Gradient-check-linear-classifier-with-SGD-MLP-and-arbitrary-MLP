import numpy as np
import loglinear as ll
import math

STUDENT={'name': 'ZAIDMAN IGAL',
         'ID': '311758866'}

def classifier_output(x, params):
    # YOUR CODE HERE.
    W, b, U, b_tag = params
    layer = np.tanh(np.dot(x, W) + b)
    probs = ll.classifier_output(layer, [U,b_tag])
    
    return probs

def predict(x, params):
    """
    params: a list of the form [W, b, U, b_tag]
    """
    return np.argmax(classifier_output(x, params))

def loss_and_gradients(x, y, params):
    """
    params: a list of the form [W, b, U, b_tag]

    returns:
        loss,[gW, gb, gU, gb_tag]

    loss: scalar
    gW: matrix, gradients of W
    gb: vector, gradients of b
    gU: matrix, gradients of U
    gb_tag: vector, gradients of b_tag
    """
    # YOU CODE HERE
    W, b, U, b_tag = params
    
    y_vec = np.zeros(U.shape[1])
    y_vec[y] = 1
    y_tag = classifier_output(x, params)
    loss = -math.log(y_tag[y])

# layer
    layer_prm = np.tanh( x.dot(W) + b )
    gb_tag = y_tag - y_vec
    gU = np.array([layer_prm]).transpose().dot(np.array([gb_tag]))
    gb = gb_tag.dot(U.transpose()) * (1 - np.power(layer_prm, 2))
    gW = np.array([x]).transpose().dot(np.array([gb]))

    return loss, [gW, gb, gU, gb_tag]

def create_classifier(in_dim, hid_dim, out_dim):
    """
    returns the parameters for a multi-layer perceptron,
    with input dimension in_dim, hidden dimension hid_dim,
    and output dimension out_dim.

    return:
    a flat list of 4 elements, W, b, U, b_tag.
    """
    W = np.random.randn(in_dim, hid_dim) / np.sqrt(in_dim)
    b = np.zeros(hid_dim)

    U = np.random.randn(hid_dim, out_dim) / np.sqrt(hid_dim)
    b_tag = np.zeros(out_dim)

    return [W, b, U, b_tag]


