# Vehicle Model Classification using Convolutional Neural Networks

This repository contains the code and resources for a vehicle classification project. The goal of the project is to accurately predict the make and model of vehicles from unstructured e-commerce images. By utilizing convolutional neural networks (CNNs), we preprocess the data, generate augmented training samples, and train a fine-grained classification model.

<p align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/Python-3.10%20-%23006400.svg?&style=for-the-badge&logo=Python&logoColor=green" /></a>
    <a href="https://www.tensorflow.org/">
        <img src="https://img.shields.io/badge/Tensorflow%20-%23FF8300.svg?&style=for-the-badge&logo=Tensorflow&logoColor=white" /></a>
    <a href="https://www.tensorflow.org/">
        <img src="https://img.shields.io/badge/Pytorch%20-%23EE4C2C.svg?&style=for-the-badge&logo=Pytorch&logoColor=white" /></a>
    <a href="https://www.docker.com/">
        <img src="https://img.shields.io/badge/Docker%20-%23003F8C.svg?&style=for-the-badge&logo=Docker&logoColor=white" /></a>
    <a href="https://choosealicense.com/licenses/mit/">
        <img src="https://img.shields.io/badge/License-MIT%20-%23212121.svg?&style=for-the-badge&logoColor=green" /></a>
    <a href="https://www.linkedin.com/in/enzo-matias-gonzalez/">
        <img src="https://img.shields.io/badge/LinkedIn%20-%230270AD.svg?&style=for-the-badge&logo=Linkedin&logoColor=white" /></a>
    
</p>

## Key Features

- Preprocessing: The dataset of unstructured e-commerce images is preprocessed to ensure consistent inputs for the classification model. This includes resizing, normalizing, and removing irrelevant information such as croping backgrounds.
- Data Augmentation: To increase the size and variability of the training dataset, data augmentation techniques are employed. This involves applying transformations like rotation, flipping, and scaling to create additional samples for better generalization.
- ResNet CNN Architecture: The model architecture is based on the ResNet CNN, which has proven to be effective in various image classification tasks. The convolutional layers of the ResNet are pretrained on a large-scale dataset and finetuned to suit the vehicle make and model classification task.
- Finetuning the Fully Connected Layers: The fully connected layers of the ResNet are adjusted and finetuned to specialize in the fine-grained classification of vehicle makes and models. This customization allows the model to extract discriminative features and achieve high accuracy.
- Training and Evaluation: The model is trained using the augmented dataset and optimized using stochastic gradient descent (SGD). The training process involves feeding the images through the network, updating the model's weights, and minimizing the classification loss. The model's performance is evaluated using a separate test set, with accuracy as the primary evaluation metric.
