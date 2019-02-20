import os
from PIL import Image
import tensorflow as tf
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

IMAGE_SIZE = 500
NUM_CLASSES = 1 # table, table_with_edges

def get_batch(data, size):
	re = []
	taken_indices = []	
	while True:
		i = random.randint(0, len(data)-1)
		if i in taken_indices:
			continue
		taken_indices.append(i)				
		re.append(data[i])	
		if len(re) >= size:						
			break			
	x = np.array([item[0] for item in re])		
	y = np.array([item[1] for item in re])
	return np.array(x), np.array(y)

def fetch_dataset():
	flags = tf.app.flags
	FLAGS = flags.FLAGS	
	flags.DEFINE_string('data_dir', "../data/tables", """Path to the data samples directory""")	

	# SCALE = 0.25
	# SCALED_IMAGE_SIZE = SCALE * ORIGINAL_IMAGE_SIZE	

	data_dir = FLAGS.data_dir
	NUM_SAMPLES = len(os.listdir(data_dir)) - 2 # subtract two for the properties files

	image_paths = ["{}/{}.png".format(data_dir, i) for i in range(0, NUM_SAMPLES)]
	dataset_path = "{}/props.csv".format(data_dir)
	dataset = pd.read_csv(dataset_path)
	labels = dataset.iloc[:, -1]		
	images = []
	for path in image_paths:
		image = Image.open(path)
		image_array = np.array(image)[:, :, 0:3]		
		images.append(image_array)		
	images = np.array(images)	
	dataset = []
	for i in range(0, len(images)):
		dataset.append([images[i], labels[i]])	
	return dataset