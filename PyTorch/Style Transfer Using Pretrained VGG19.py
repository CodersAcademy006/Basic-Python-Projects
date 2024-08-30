#%%
# import numpy, tensorflow and matplotlib
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import math
import time

# import VGG 19 model and keras Model API
from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model

# Image Credits: Tensorflow Doc
content_path = tf.keras.utils.get_file(
    'content.jpg',
    'https://storage.googleapis.com/download.tensorflow.org/example_images/YellowLabradorLooking_new.jpg')
style_path = tf.keras.utils.get_file(
    'style.jpg',
    'https://storage.googleapis.com/download.tensorflow.org/example_images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg')

# Code to load and process image with resizing
def load_and_process_image(image_path, target_size=(256, 256)):
    img = load_img(image_path, target_size=target_size)
    img = img_to_array(img)
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    return img

def deprocess(img):
    img[:, :, 0] += 103.939
    img[:, :, 1] += 116.779
    img[:, :, 2] += 123.68
    img = img[:, :, ::-1]
    img = np.clip(img, 0, 255).astype('uint8')
    return img

def display_image(image):
    if len(image.shape) == 4:
        img = np.squeeze(image, axis=0)
    img = deprocess(img)
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img)
    return

# Load and display content and style images
content_img = load_and_process_image(content_path)
style_img = load_and_process_image(style_path)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
display_image(content_img)
plt.title('Content Image')

plt.subplot(1, 2, 2)
display_image(style_img)
plt.title('Style Image')
plt.show()

# Load the VGG19 model and set it to non-trainable
model = VGG19(include_top=False, weights='imagenet')
model.trainable = False

# Print details of different layers
model.summary()

# Define content and style models
content_layer = 'block5_conv2'
content_model = Model(inputs=model.input, outputs=model.get_layer(content_layer).output)

style_layers = ['block1_conv1', 'block3_conv1']  # Fewer style layers
style_models = [Model(inputs=model.input, outputs=model.get_layer(layer).output) for layer in style_layers]

# Content loss
def content_loss(content, generated):
    a_C = content_model(content)
    a_G = content_model(generated)
    loss = tf.reduce_mean(tf.square(a_C - a_G))
    return loss

# Gram matrix
def gram_matrix(A):
    channels = int(A.shape[-1])
    a = tf.reshape(A, [-1, channels])
    n = tf.shape(a)[0]
    gram = tf.matmul(a, a, transpose_a=True)
    return gram / tf.cast(n, tf.float32)

# Style loss
def style_cost(style, generated):
    J_style = 0
    weight_of_layer = 1. / len(style_models)

    for style_model in style_models:
        a_S = style_model(style)
        a_G = style_model(generated)
        GS = gram_matrix(a_S)
        GG = gram_matrix(a_G)
        style_loss = tf.reduce_mean(tf.square(GS - GG))
        J_style += style_loss * weight_of_layer

    return J_style

# Training function
generated_images = []

def training_loop(content_path, style_path, iterations=30, a=10, b=1000):
    content = load_and_process_image(content_path)
    style = load_and_process_image(style_path)
    generated = tf.Variable(content, dtype=tf.float32)
    
    # Set a smaller, more appropriate learning rate
    opt = tf.keras.optimizers.Adam(learning_rate=0.02)
    
    best_cost = math.inf
    best_image = None

    for i in range(iterations):
        start_time_cpu = time.process_time()
        start_time_wall = time.time()

        with tf.GradientTape() as tape:
            J_content = content_loss(content, generated)
            J_style = style_cost(style, generated)
            J_total = a * J_content + b * J_style

        grads = tape.gradient(J_total, generated)
        opt.apply_gradients([(grads, generated)])

        end_time_cpu = time.process_time()
        end_time_wall = time.time()

        cpu_time = end_time_cpu - start_time_cpu
        wall_time = end_time_wall - start_time_wall

        if J_total < best_cost:
            best_cost = J_total
            best_image = generated.numpy()

        print(f"Iteration {i}: Total Loss {J_total:.4e}, CPU Time: {cpu_time:.6f}s, Wall Time: {wall_time:.6f}s")

        generated_images.append(generated.numpy())

    return best_image

# Train the model and get best image
final_img = training_loop(content_path, style_path, iterations=30)

# Display last 10 intermediate results
plt.figure(figsize=(12, 12))
for i in range(min(10, len(generated_images))):
    plt.subplot(4, 3, i + 1)
    display_image(generated_images[i])
plt.show()

# Display best result
plt.figure(figsize=(10, 10))
display_image(final_img)
plt.title('Final Style Transfer Result')
plt.show()
#%%
#