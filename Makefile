# OS specific symbols
ifeq ($(OS), Windows_NT)
BLANK =
DELIMITER = \$(BLANK)
SCRIPT_PREFIX = 
SCRIPT_SUFFIX = .bat
else
DELIMITER = /
SCRIPT_PREFIX = ./
SCRIPT_SUFFIX = .sh
endif

# docker
DOCKER = docker
DOCKER_IMAGE = kaggle
DOCKER_IMAGE_TAG = latest
DOCKER_CONTAINER = kaggle
DOCKER_CONTAINER_SHELL = /bin/sh

# Clean docker environment
clean-devenv:
	$(SCRIPT_PREFIX)script$(DELIMITER)clean-devenv$(SCRIPT_SUFFIX) $(DOCKER) $(DOCKER_IMAGE) $(DOCKER_CONTAINER)

# Build docker environment
devenv:
	$(SCRIPT_PREFIX)script$(DELIMITER)devenv$(SCRIPT_SUFFIX) $(DOCKER) $(DOCKER_IMAGE) $(DOCKER_IMAGE_TAG) $(DOCKER_CONTAINER)

# Only the developer can execute it.
# usage : $ make gitconfig KEY=<GitHub private key path> GPG=<.gnupg path>
gitconfig:
	$(DOCKER) cp $(KEY) $(DOCKER_CONTAINER):/root/Kaggle/ssh/github && \
	$(DOCKER) cp $(GPG) $(DOCKER_CONTAINER):/root/.gnupg && \
	$(DOCKER) start $(DOCKER_CONTAINER) && \
	$(DOCKER) exec -it $(DOCKER_CONTAINER) /root/Kaggle/git/gitconfig.sh && \
	$(DOCKER) stop $(DOCKER_CONTAINER)

# Rebuild docker environment
rebuild-devenv: clean-devenv
	make devenv

update-repository:
	git pull origin main

