DATASET=$(shell pwd | awk -F / '{print $$NF}')
ZIPPED_IMAGES=$(DATASET).zip
IMAGES=train test

all: $(IMAGES)
	python train.py

$(IMAGES): $(ZIPPED_IMAGES)
	unzip $^

$(ZIPPED_IMAGES):
	kaggle datasets download samuelcortinhas/$(DATASET)

