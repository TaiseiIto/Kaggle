DATASET=$(shell pwd | awk -F / '{print $$NF}')
MODEL=model.nnoir
MODEL_FIX_DIMENSION=model_fix_dimension.onnx
MODEL_ONNX=model.onnx
IMAGES=train test
ZIPPED_IMAGES=$(DATASET).zip

all: $(MODEL)
	python test.py

$(MODEL): $(MODEL_FIX_DIMENSION)
	onnx2nnoir -o $@ $<

$(MODEL_FIX_DIMENSION): $(MODEL_ONNX)
	onnxsim $< $@ --overwrite-input-shape 1,256,256,3

$(MODEL_ONNX): $(IMAGES)
	python train.py

$(IMAGES): $(ZIPPED_IMAGES)
	unzip $^

$(ZIPPED_IMAGES):
	kaggle datasets download samuelcortinhas/$(DATASET)

