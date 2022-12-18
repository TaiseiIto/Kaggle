import lightgbm
import numpy
import pandas

if __name__ == '__main__':
	print('Hello, World!')
	gender_submission_data_frame = pandas.read_csv('gender_submission.csv')
	test_data_frame = pandas.read_csv('test.csv')
	test_data_frame['Cabin'] = test_data_frame['Cabin'].map(lambda cabin : len(cabin.split()) if isinstance(cabin, str) else numpy.nan)
	test_data_frame = test_data_frame.drop('Name', axis = 1)
	train_data_frame = pandas.read_csv('train.csv')
	train_data_frame['Cabin'] = train_data_frame['Cabin'].map(lambda cabin : len(cabin.split()) if isinstance(cabin, str) else numpy.nan)
	train_data_frame = train_data_frame.drop('Name', axis = 1)
	print('gender_submission_data_frame')
	print(gender_submission_data_frame)
	print('test_data_frame')
	print(test_data_frame)
	print('train_data_frame')
	print(train_data_frame)
	gender_submission_column_names = set(gender_submission_data_frame.columns)
	test_data_column_names = set(test_data_frame.columns)
	print('gender_submission_column_names = {}'.format(gender_submission_column_names))
	print('test_data_column_names = {}'.format(test_data_column_names))
	output_column_names = gender_submission_column_names - test_data_column_names
	input_column_names = test_data_column_names
	print('output_colunm_names = {}'.format(output_column_names))
	print('input_colunm_names = {}'.format(input_column_names))
	test_input_data_frame = test_data_frame[input_column_names]
	test_output_data_frame = gender_submission_data_frame[output_column_names]
	train_input_data_frame = train_data_frame[input_column_names]
	train_output_data_frame = train_data_frame[output_column_names]
	print('test_input_data_frame')
	print(test_input_data_frame)
	print('test_output_data_frame')
	print(test_output_data_frame)
	print('train_input_data_frame')
	print(train_input_data_frame)
	print('train_output_data_frame')
	print(train_output_data_frame)
	train_data_set = lightgbm.Dataset(train_input_data_frame, train_output_data_frame)
	train_params = {'objective' : 'binary'}
	model = lightgbm.train(train_params, train_data_set)

