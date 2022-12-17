COMPETITIONS=$(shell ls -l | grep ^d.*$$ | awk '{print $$NF}')

all:
	$(foreach COMPETITION, $(COMPETITIONS), make -C $(COMPETITION))

clean:
	$(foreach COMPETITION, $(COMPETITIONS), make clean -C $(COMPETITION))

rebuild:
	$(foreach COMPETITION, $(COMPETITIONS), make rebuild -C $(COMPETITION))

