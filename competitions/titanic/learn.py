import pandas

if __name__ == '__main__':
	print('Hello, World!')
	gender_submission_data_frame = pandas.read_csv('gender_submission.csv')
	test_data_frame = pandas.read_csv('test.csv')
	train_data_frame = pandas.read_csv('train.csv')
	print('gender_submission_data_frame')
	print(gender_submission_data_frame)
	print('test_data_frame')
	print(test_data_frame)
	print('train_data_frame')
	print(train_data_frame)
	gender_submission_column_names = set(gender_submission_data_frame.columns)
	test_data_column_names = set(test_data_frame.columns)
	print("gender_submission_column_names = {}".format(gender_submission_column_names))
	print("test_data_column_names = {}".format(test_data_column_names))
	output_column_names = gender_submission_column_names - test_data_column_names
	input_column_names = test_data_column_names
	print("output_colunm_names = {}".format(output_column_names));
	print("input_colunm_names = {}".format(input_column_names));

