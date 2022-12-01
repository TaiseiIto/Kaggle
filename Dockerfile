FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
# gcc, ld, make, etc.
RUN apt install build-essential -y
# git
RUN apt install git -y
RUN apt install git-email -y
RUN git config --global pull.rebase false
RUN mkdir /root/.ssh
# tmux
RUN apt install tmux -y
# tzdata
RUN apt install tzdata -y
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
# unzip
RUN apt install unzip -y
# editor
RUN apt install vim -y
# wget
RUN apt install wget -y
# clone the repository
WORKDIR /root
RUN git clone https://github.com/TaiseiIto/Kaggle.git
WORKDIR /root/Kaggle
# python
# RUN ./python/setup.sh

# ash setting
RUN cat ash/.profile >> /root/.bashrc

# tmux setting
RUN cp tmux/.tmux.conf ..

# vim setting
RUN cat vim/.vimrc >> ../.vimrc

