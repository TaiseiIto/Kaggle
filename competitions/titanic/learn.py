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

