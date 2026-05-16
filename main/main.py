import tensorflow as tf
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#The dataset
import kagglehub as kagg

# Download latest version
path = kagg.dataset_download("alirezakay/stranger-things-faces-dataset-grayscale")

print("Path to dataset files:", path)