FROM python:3

# vimとseleniumをインストール
RUN set -x && \
  apt-get update && \
  apt-get install -y vim
RUN  pip3 install pandas
RUN  pip3 install selenium
RUN  pip3 install slacker
RUN  pip3 install google-cloud-storage
RUN  pip3 install pandas-gbq
RUN  pip3 install random