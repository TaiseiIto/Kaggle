COMPETITION=$(shell pwd | awk -F / '{print $$NF}')
TARGETS=gender_submission.csv test.csv train.csv
UNZIPPED=.unzipped
ZIP=$(COMPETITION).zip

all: $(TARGETS)

clean:
	rm $(TARGETS) $(ZIP)

rebuild: clean
	make

$(ZIP):
	kaggle competitions download -c $(COMPETITION)

$(UNZIPPED): $(ZIP)
	unzip $^
	touch $@

%.csv: $(UNZIPPED)
	:

