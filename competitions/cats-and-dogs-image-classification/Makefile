DATASET=$(shell pwd | awk -F / '{print $$NF}')
MODEL=model
IMAGES=train test
ZIPPED_IMAGES=$(DATASET).zip

all: $(MODEL)
	python test.py

$(MODEL): $(IMAGES)
	python train.py

$(IMAGES): $(ZIPPED_IMAGES)
	unzip $^

$(ZIPPED_IMAGES):
	kaggle datasets download samuelcortinhas/$(DATASET)

