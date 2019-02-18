import numpy as np
import pandas as pd
import tensorflow as tf
import tables_images as tables

from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten

training_size = 0.7

data = tables.fetch_dataset()[0:50]
train_size_limit = round(training_size * len(data))
train_data = data[: train_size_limit]
test_data = data[ train_size_limit:]

shape = [tables.IMAGE_SIZE, tables.IMAGE_SIZE, 3]

model = Sequential()
model.add(Conv2D(64, kernel_size=5, activation='relu', input_shape=shape))
model.add(Conv2D(32, kernel_size=5, activation='relu'))
model.add(Flatten())
model.add(Dense(1, activation='softmax'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
train_x, train_y = tables.get_batch(train_data, len(train_data))
test_x, test_y = tables.get_batch(test_data, len(test_data))

model.fit(train_x, train_y, epochs=3, batch_size=10)
scores = model.evaluate(test_x, test_y, verbose=0)
print(scores)

## Save Model
model_json = model.to_json()
with open('../models/tables.json', 'w') as file:
	file.write(model_json)
model.save_weights('../models/tables.h5')
print("Saved to disk")
