ZIP=titanic.zip

all: $(ZIP)
	unzip $^

clean:
	rm *.csv $(ZIP)

rebuild: clean
	make

$(ZIP):
	kaggle competitions download -c titanic

