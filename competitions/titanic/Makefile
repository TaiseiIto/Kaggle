TARGETS=gender_submission.csv test.csv train.csv
ZIP=titanic.zip

all: $(TARGETS)

clean: clean-csv
	rm $(ZIP)

clean-csv:
	for i in $$(ls | grep ^.*\.csv$$); do rm $$i; done

rebuild: clean
	make

$(ZIP):
	kaggle competitions download -c titanic

%.csv: $(ZIP)
	unzip -o $^

