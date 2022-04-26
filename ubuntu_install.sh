sudo apt update
sudo apt install -y wget git libyaml-cpp-dev libgsl0-dev libpopt-dev  build-essential graphviz

cd wombats_experiments/dfasat \
    && make gitversion.cpp && make \
    && cd .. \
    && pip install .
