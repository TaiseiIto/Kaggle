COMPETITION=$(shell pwd | awk -F / '{print $$NF}')
CSVS=gender_submission.csv test.csv train.csv
MODEL=model.pkl
UNZIPPED=.unzipped
ZIP=$(COMPETITION).zip

all: evaluate.py $(MODEL)
	python $<

$(MODEL): learn.py $(CSVS)
	python $<

clean:
	rm $(CSVS) $(MODEL) $(ZIP)

rebuild: clean
	make

$(ZIP):
	kaggle competitions download -c $(COMPETITION)

$(UNZIPPED): $(ZIP)
	unzip $^
	touch $@

%.csv: $(UNZIPPED)
	:

