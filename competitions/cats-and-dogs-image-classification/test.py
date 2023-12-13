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
	test_images = images / 'test'
	labels = {label.name for label in test_images.iterdir()}
	label2label_id = {label : label_id for label_id, label in enumerate(sorted(labels))}
	label2one_hot_vector = {label : [1 if label2label_id[label] == label_id else 0 for label_id in range(len(labels))] for label in labels}
	print(label2one_hot_vector)
	
	label2test_image_paths = {label : {test_image_path for test_image_path in (test_images / label).iterdir()} for label in labels}
	test_image_paths = functools.reduce(lambda left_test_image_paths, right_test_image_paths : left_test_image_paths | right_test_image_paths, label2test_image_paths.values(), set())
	test_image_path2test_image_path_id = {test_image_path : test_image_path_id for test_image_path_id, test_image_path in enumerate(sorted(test_image_paths))}
	test_image_path_ids = {test_image_path_id for test_image_path_id in test_image_path2test_image_path_id.values()}
	test_image_path2label = {test_image_path : next(label for label in labels if test_image_path in label2test_image_paths[label]) for test_image_path in test_image_paths}
	test_image_path_id2label_one_hot_vector = {test_image_path2test_image_path_id[test_image_path]: label2one_hot_vector[label] for test_image_path, label in test_image_path2label.items()}
	test_image_path_id2test_image = {test_image_path2test_image_path_id[test_image_path] : numpy.array(Image.open(test_image_path).convert('RGB').resize(image_size)) for test_image_path in test_image_paths}
	test_x = numpy.array([test_image_path_id2test_image[test_image_path_id] for test_image_path_id in sorted(test_image_path_ids)])
	test_y = numpy.array([test_image_path_id2label_one_hot_vector[test_image_path_id] for test_image_path_id in sorted(test_image_path_ids)])

	model = tensorflow.keras.models.load_model('model')
	model.summary()

	test_loss, test_accuracy = model.evaluate(test_x, test_y)
	print(f'test_loss = {test_loss}')
	print(f'test_accuracy = {test_accuracy}')

