import pandas

gender_submission_data_frame = pandas.read_csv('gender_submission.csv')
test_data_frame = pandas.read_csv('test.csv')
gender_submission_column_names = set(gender_submission_data_frame.columns)
test_data_column_names = set(test_data_frame.columns)
output_column_names = gender_submission_column_names - test_data_column_names
input_column_names = test_data_column_names
test_input_data_frame = test_data_frame[input_column_names]
test_output_data_frame = gender_submission_data_frame[output_column_names]
print(test_input_data_frame)
print(test_output_data_frame)

