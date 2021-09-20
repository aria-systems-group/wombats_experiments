FROM ubuntu:18.04

RUN apt update

# Install Tools and C++ Libraries
RUN apt install -y wget git libyaml-cpp-dev libgsl0-dev libpopt-dev  build-essential

# Install Anaconda
RUN wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh \
    && bash Anaconda3-2019.10-Linux-x86_64.sh -b \
    && rm Anaconda3-2019.10-Linux-x86_64.sh

# path setteing
ENV PATH $PATH:/root/anaconda3/bin

# Somehow it fails when pulling dfasat/pypckage/src submodule
# so I added "|| true" to ignore the error
RUN cd \
    && git clone --recurse-submodules https://github.com/aria-systems-group/wombats_experiments || true

RUN cd \
    && cd wombats_experiments/dfasat \
    && make gitversion.cpp && make \
    && cd .. \
    && conda env create -f environment.yml \
    && conda init bash

# RUN conda activate wombats \
#     jupyter notebook



