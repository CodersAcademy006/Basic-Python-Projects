import numpy as np
import matplotlib.pyplot as plt

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function for backpropagation
def sigmoid_derivative(x):
    return x * (1 - x)

# XOR inputs and corresponding outputs
inputs = np.array([[0, 0],
                   [0, 1],
                   [1, 0],
                   [1, 1]])

outputs = np.array([[0], [1], [1], [0]])

# Set a seed for reproducibility
np.random.seed(42)

# Random weights for input -> hidden layer (2 neurons in hidden layer)
input_weights = np.random.uniform(size=(2, 2))
hidden_weights = np.random.uniform(size=(2, 1))

# Bias terms
input_bias = np.random.uniform(size=(1, 2))
hidden_bias = np.random.uniform(size=(1, 1))

# Learning rate
learning_rate = 0.1

# Training parameters
epochs = 10000  # Number of iterations for training
losses = []  # To track loss over time

# Training the neural network
for epoch in range(epochs):
    # Feedforward step
    hidden_layer_input = np.dot(inputs, input_weights) + input_bias
    hidden_layer_output = sigmoid(hidden_layer_input)

    final_input = np.dot(hidden_layer_output, hidden_weights) + hidden_bias
    final_output = sigmoid(final_input)

    # Calculate the error
    error = outputs - final_output
    losses.append(np.mean(np.abs(error)))  # Track the mean absolute error

    # Backpropagation step
    d_final_output = error * sigmoid_derivative(final_output)
    error_hidden_layer = d_final_output.dot(hidden_weights.T)
    d_hidden_output = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    hidden_weights += hidden_layer_output.T.dot(d_final_output) * learning_rate
    hidden_bias += np.sum(d_final_output, axis=0, keepdims=True) * learning_rate
    input_weights += inputs.T.dot(d_hidden_output) * learning_rate
    input_bias += np.sum(d_hidden_output, axis=0, keepdims=True) * learning_rate

# Testing the network
def predict(x):
    hidden_layer_input = np.dot(x, input_weights) + input_bias
    hidden_layer_output = sigmoid(hidden_layer_input)
    final_input = np.dot(hidden_layer_output, hidden_weights) + hidden_bias
    final_output = sigmoid(final_input)
    return final_output

# Plotting the loss vs epochs graph
plt.figure(figsize=(10, 6))
plt.plot(losses, label='Loss (Error)')
plt.title('Loss (Error) vs Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()

# Visualize the decision boundary
def plot_decision_boundary():
    x_min, x_max = -0.5, 1.5
    y_min, y_max = -0.5, 1.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    grid = np.c_[xx.ravel(), yy.ravel()]
    predictions = predict(grid)
    Z = np.round(predictions).reshape(xx.shape)

    plt.figure(figsize=(10, 6))
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.6)
    plt.scatter(inputs[:, 0], inputs[:, 1], c=outputs.ravel(), s=100, cmap=plt.cm.Spectral, edgecolors='k')
    plt.title('Decision Boundary for XOR Problem')
    plt.xlabel('Input 1')
    plt.ylabel('Input 2')
    plt.show()

# Show the decision boundary
plot_decision_boundary()

# Print final results after training
for input_data, target in zip(inputs, outputs):
    prediction = predict(input_data)
    print(f"Input: {input_data}, Predicted Output: {np.round(prediction)}, True Output: {target}")


# Test Cases
# Input: [0 0], Predicted Output: [0.], True Output: [0]
# Input: [0 1], Predicted Output: [1.], True Output: [1]
# Input: [1 0], Predicted Output: [1.], True Output: [1]
# Input: [1 1], Predicted Output: [0.], True Output: [0]