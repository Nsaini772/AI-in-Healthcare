# AI in Healthcare
# Genomic sequence classification with 1D CNN models(Alexnet and NiN)

This project is focused on classifying genomic sequences(DNA sequences) using convolutional neural networks (CNN's). The models implemented include AlexNet1D and NiN1D, both of which are tailored for sequence classification tasks. The data used in this project consists of DNA sequences encoded into one-hot encode. After training, the script will evaluate the model's performance on the test set, plotting accuracy graphs and confusion matrices.

You can change the file address from the main section of the code, depaning on the data file you want to run the model. 

# To run:
python project2.ipynb

# Features:
1. DNA sequences are one-hot encoded
2. Model training is done using AlexNet1D and NiN1D architecture.
3. Evaluation includes accuracy calculation and confusion matrix plotting.
4. Hyperparameter tuning using learning rate and weight decay option.
5. Visualizations for accuracies and confusion matrices across models.

# Install the required dependencies:
pip install torch numpy matplotlib scikit-learn seaborn

# Directory Structure
|--negative -> folder of 10 files containing negative datapoints
|--positive -> folder of 10 foles containing positive datapoints
|--1000.txt -> sample file containing 1000 data points
|--10000.txt -> sample file containing 10000 data points
|--Dataset.txt -> final dataset file
|--createDemoFile.py -> 
|--combineFile.py -> 
|--file1.txt -> combined file from 10 positive file
|--file2.txt -> combined file from 10 negative file
|--project2.ipynb -> this is the python code implemented model using AlexNet1D and NiN1D architecture.

# Model Architecture
-> AlexNet1D: A 1D convolutional neural network inspired by the AlexNet architecture. It consists of two convolutional layers followed by fully connected layers and dropout for regularization.
-> NiN1D: A 1D version of the Network in Network (NiN) model. It uses smaller convolutional layers and applies multiple convolution operations sequentially for feature extraction.

# Example Dataset
ATGCATGCATGCATGC 0 <--negative with 0
CGTACGTACGTACGTA 1 <--positive with 1
TTGCCAAGGTTCCGG 0
AAGTCCGGAATTGGTT 1
CGTACGTAGGTCGTA 0
...
...
GTACGTACGTAGGCTT 1


# Result and Visualizations
Accuracy Plot: Plots the training accuracy for each epoch.
Confusion matrix: Visualizes the confusion matrix for each model across the test dataset.

# Example output
Using device: cuda
Epoch 1: Loss = 0.6932, Accuracy = 56.25%
Epoch 2: Loss = 0.6689, Accuracy = 65.12%
...
Test Accuracy: 78.50%
