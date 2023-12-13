from PIL import Image
import functools
import numpy
import pathlib
import random
import tensorflow

if __name__=='__main__':
	seed = 0
	random.seed(seed)
	numpy.random.seed(seed)
	tensorflow.random.set_seed(seed)
	image_width = 0x100
	image_height = 0x100
	image_size = (image_width, image_height)
	images = pathlib.Path.cwd()
	train_images = images / 'train'
	test_images = images / 'test'
	labels = {label.name for label in train_images.iterdir()} | {label.name for label in test_images.iterdir()}
	label2label_id = {label : label_id for label_id, label in enumerate(sorted(labels))}
	label2one_hot_vector = {label : [1 if label2label_id[label] == label_id else 0 for label_id in range(len(labels))] for label in labels}
	print(label2one_hot_vector)
	
	label2train_image_paths = {label : {train_image_path for train_image_path in (train_images / label).iterdir()} for label in labels}
	train_image_paths = functools.reduce(lambda left_train_image_paths, right_train_image_paths : left_train_image_paths | right_train_image_paths, label2train_image_paths.values(), set())
	train_image_path2train_image_path_id = {train_image_path : train_image_path_id for train_image_path_id, train_image_path in enumerate(sorted(train_image_paths))}
	train_image_path_ids = {train_image_path_id for train_image_path_id in train_image_path2train_image_path_id.values()}
	train_image_path2label = {train_image_path : next(label for label in labels if train_image_path in label2train_image_paths[label]) for train_image_path in train_image_paths}
	train_image_path_id2label_one_hot_vector = {train_image_path2train_image_path_id[train_image_path]: label2one_hot_vector[label] for train_image_path, label in train_image_path2label.items()}
	train_image_path_id2train_image = {train_image_path2train_image_path_id[train_image_path] : numpy.array(Image.open(train_image_path).convert('RGB').resize(image_size)) for train_image_path in train_image_paths}
	train_x = numpy.array([train_image_path_id2train_image[train_image_path_id] for train_image_path_id in sorted(train_image_path_ids)])
	train_y = numpy.array([train_image_path_id2label_one_hot_vector[train_image_path_id] for train_image_path_id in sorted(train_image_path_ids)])

	label2test_image_paths = {label : {test_image_path for test_image_path in (test_images / label).iterdir()} for label in labels}
	test_image_paths = functools.reduce(lambda left_test_image_paths, right_test_image_paths : left_test_image_paths | right_test_image_paths, label2test_image_paths.values(), set())
	test_image_path2test_image_path_id = {test_image_path : test_image_path_id for test_image_path_id, test_image_path in enumerate(sorted(test_image_paths))}
	test_image_path_ids = {test_image_path_id for test_image_path_id in test_image_path2test_image_path_id.values()}
	test_image_path2label = {test_image_path : next(label for label in labels if test_image_path in label2test_image_paths[label]) for test_image_path in test_image_paths}
	test_image_path_id2label_one_hot_vector = {test_image_path2test_image_path_id[test_image_path]: label2one_hot_vector[label] for test_image_path, label in test_image_path2label.items()}
	test_image_path_id2test_image = {test_image_path2test_image_path_id[test_image_path] : numpy.array(Image.open(test_image_path).convert('RGB').resize(image_size)) for test_image_path in test_image_paths}
	test_x = numpy.array([test_image_path_id2test_image[test_image_path_id] for test_image_path_id in sorted(test_image_path_ids)])
	test_y = numpy.array([test_image_path_id2label_one_hot_vector[test_image_path_id] for test_image_path_id in sorted(test_image_path_ids)])

	model = tensorflow.keras.models.Sequential()
	model.add(tensorflow.keras.layers.Rescaling(1 / 0xff, input_shape=train_x.shape[1:]))
	model.add(tensorflow.keras.layers.Conv2D(32, (3, 3), activation = 'relu'))
	model.add(tensorflow.keras.layers.MaxPooling2D(pool_size = (2, 2)))
	model.add(tensorflow.keras.layers.Dropout(0.1))
	model.add(tensorflow.keras.layers.Conv2D(64, (3, 3), activation = 'relu'))
	model.add(tensorflow.keras.layers.MaxPooling2D(pool_size = (2, 2)))
	model.add(tensorflow.keras.layers.Dropout(0.1))
	model.add(tensorflow.keras.layers.Flatten())
	model.add(tensorflow.keras.layers.Dense(0x100, activation = 'relu'))
	model.add(tensorflow.keras.layers.Dropout(0.1))
	model.add(tensorflow.keras.layers.Dense(len(labels), activation = 'softmax'))

	model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
	model.summary()
	batch_size = int(numpy.power(2, numpy.floor(numpy.log2(numpy.sqrt(len(train_image_paths))))))
	model.fit(train_x, train_y, batch_size = batch_size, epochs = 1)

	train_loss, train_accuracy = model.evaluate(train_x, train_y)
	print(f'train_loss = {train_loss}')
	print(f'train_accuracy = {train_accuracy}')
	test_loss, test_accuracy = model.evaluate(test_x, test_y)
	print(f'test_loss = {test_loss}')
	print(f'test_accuracy = {test_accuracy}')

	model.save('model')

