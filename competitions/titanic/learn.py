import lightgbm
import numpy
import pandas
import pickle
import re

gender_submission_data_frame = pandas.read_csv('gender_submission.csv')
test_data_frame = pandas.read_csv('test.csv')
train_data_frame = pandas.read_csv('train.csv')
embarked_marks = set(test_data_frame['Embarked']) | set(test_data_frame['Embarked'])
embarked_marks = sorted(list(embarked_marks))
embarked_mark_to_number = {embarked_marks[number] : number for number in range(len(embarked_marks))}
sex_marks = set(test_data_frame['Sex']) | set(test_data_frame['Sex'])
sex_marks = sorted(list(sex_marks))
sex_mark_to_number = {sex_marks[number] : number for number in range(len(sex_marks))}
test_data_frame['Cabin'] = test_data_frame['Cabin'].map(lambda cabin : len(cabin.split()) if isinstance(cabin, str) else numpy.nan)
train_data_frame['Cabin'] = train_data_frame['Cabin'].map(lambda cabin : len(cabin.split()) if isinstance(cabin, str) else numpy.nan)
test_data_frame['Embarked'] = test_data_frame['Embarked'].map(lambda embarked_mark : embarked_mark_to_number[embarked_mark] if isinstance(embarked_mark, str) else numpy.nan)
train_data_frame['Embarked'] = train_data_frame['Embarked'].map(lambda embarked_mark : embarked_mark_to_number[embarked_mark] if isinstance(embarked_mark, str) else numpy.nan)
test_data_frame['Name'] = test_data_frame['Name'].map(lambda name : len(name.split()))
train_data_frame['Name'] = train_data_frame['Name'].map(lambda name : len(name.split()))
test_data_frame['Sex'] = test_data_frame['Sex'].map(lambda sex_mark : sex_mark_to_number[sex_mark] if isinstance(sex_mark, str) else numpy.nan)
train_data_frame['Sex'] = train_data_frame['Sex'].map(lambda sex_mark : sex_mark_to_number[sex_mark] if isinstance(sex_mark, str) else numpy.nan)
test_data_frame['Ticket'] = test_data_frame['Ticket'].map(lambda ticket : re.split('[^0-9]', ticket)[-1])
test_data_frame['Ticket'] = test_data_frame['Ticket'].map(lambda ticket : int(ticket) if re.match('^[0-9]+$', ticket) else numpy.nan)
train_data_frame['Ticket'] = train_data_frame['Ticket'].map(lambda ticket : re.split('[^0-9]', ticket)[-1])
train_data_frame['Ticket'] = train_data_frame['Ticket'].map(lambda ticket : int(ticket) if re.match('^[0-9]+$', ticket) else numpy.nan)
gender_submission_column_names = set(gender_submission_data_frame.columns)
test_data_column_names = set(test_data_frame.columns)
output_column_names = gender_submission_column_names - test_data_column_names
input_column_names = test_data_column_names
test_input_data_frame = test_data_frame[input_column_names]
test_output_data_frame = gender_submission_data_frame[output_column_names]
train_input_data_frame = train_data_frame[input_column_names]
train_output_data_frame = train_data_frame[output_column_names]
model = lightgbm.LGBMClassifier()
model.fit(train_input_data_frame, train_output_data_frame)
score = model.score(test_input_data_frame, test_output_data_frame)
print('score = {}'.format(score))
with open('model.pkl', 'wb') as model_file:
	pickle.dump(model, model_file)

