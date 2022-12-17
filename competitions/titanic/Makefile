TARGETS=gender_submission.csv test.csv train.csv
ZIP=titanic.zip

all: $(TARGETS)

clean: clean-csv
	rm $(ZIP)

clean-csv:
	rm *.csv

rebuild: clean
	make

$(ZIP):
	kaggle competitions download -c titanic

%.csv: $(ZIP) clean-csv
	unzip $<

