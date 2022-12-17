COMPETITION=$(shell pwd | awk -F / '{print $$NF}')
CSVS=gender_submission.csv test.csv train.csv
UNZIPPED=.unzipped
ZIP=$(COMPETITION).zip

all: $(CSVS)
	python learn.py

clean:
	rm $(CSVS) $(ZIP)

rebuild: clean
	make

$(ZIP):
	kaggle competitions download -c $(COMPETITION)

$(UNZIPPED): $(ZIP)
	unzip $^
	touch $@

%.csv: $(UNZIPPED)
	:

