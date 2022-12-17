TARGET=gender_submission.csv test.csv train.csv
ZIP=titanic.zip

all: $(TARGET)

clean:
	rm $(TARGET) $(ZIP)

rebuild: clean
	make

$(TARGET): $(ZIP)
	unzip $^

$(ZIP):
	kaggle competitions download -c titanic

