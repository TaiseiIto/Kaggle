COMPETITIONS=$(shell ls -l | grep ^d.*$$ | awk '{print $$NF}')

define run
	make -C $(1)

endef

define clean
	make clean -C $(1)

endef

define rebuild
	make rebuild -C $(1)

endef

all:
	$(foreach COMPETITION, $(COMPETITIONS), $(call run, $(COMPETITION)))

clean:
	$(foreach COMPETITION, $(COMPETITIONS), $(call clean, $(COMPETITION)))

rebuild:
	$(foreach COMPETITION, $(COMPETITIONS), $(call rebuild, $(COMPETITION)))

