FROM 10.202.107.19/sfai/tf35:mod-v2

MAINTAINER jcwang
ENV LANG US.UTF-8
RUN apt-get update
RUN pip install --upgrade pip
RUN apt-get install -y vim
RUN apt-get install -y gedit

RUN pip install jieba
RUN pip install gensim
RUN pip install pyyaml
RUN pip install nltk
RUN pip install sklearn
RUN pip install scipy

ADD . /ner
WORKDIR /ner
