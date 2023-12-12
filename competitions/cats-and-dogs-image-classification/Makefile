DATASET=$(shell pwd | awk -F / '{print $$NF}')
ZIP=$(DATASET).zip
UNZIPPED=$(DATASET)

all:
	python train.py

$(ZIP):
	kaggle datasets download samuelcortinhas/$(DATASET)

$(UNZIPPED): $(ZIP)
	unzip $^

