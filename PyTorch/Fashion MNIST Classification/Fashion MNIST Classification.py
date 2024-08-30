#%%
# Import necessary libraries
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt

# Load the Fashion MNIST dataset
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()

# Normalize pixel values to be between 0 and 1
train_images = train_images / 255.0
test_images = test_images / 255.0

# Print dataset shape
print("Training data shape:", train_images.shape)
print("Test data shape:", test_images.shape)

# Define the CNN model
model = models.Sequential([
    # Convolutional layer
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    
    # Another convolutional layer
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    # Another convolutional layer
    layers.Conv2D(64, (3, 3), activation='relu'),
    
    # Flatten the results to feed into a dense layer
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    
    # Output layer
    layers.Dense(10)
])

# Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Print model summary
model.summary()

# Reshape data for the model
train_images = train_images[..., np.newaxis]
test_images = test_images[..., np.newaxis]

# Train the model
history = model.fit(train_images, train_labels, epochs=5, validation_split=0.1, batch_size=64)

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f'\nTest accuracy: {test_acc:.4f}')

# Plot training & validation accuracy values
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Test case: Predict on a single image
def predict_image(image):
    image = np.expand_dims(image, axis=0)
    predictions = model.predict(image)
    predicted_label = np.argmax(predictions)
    return predicted_label

# Test on a single image from the test set
sample_image = test_images[0]
sample_label = test_labels[0]
predicted_label = predict_image(sample_image)
print(f'Actual label: {sample_label}, Predicted label: {predicted_label}')
#%%
