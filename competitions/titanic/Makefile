TARGETS=gender_submission.csv test.csv train.csv
UNZIPPED=.unzipped
ZIP=titanic.zip

all: $(TARGETS)

clean:
	rm $(TARGETS) $(ZIP)

rebuild: clean
	make

$(ZIP):
	kaggle competitions download -c titanic

$(UNZIPPED): $(ZIP)
	unzip $^
	touch $@

%.csv: $(UNZIPPED)
	:

