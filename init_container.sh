#!/bin/bash
# TODO uncomment
docker build .

docker run \
--name stapp \
--network host \
--mount type=bind,source=$PWD,target=/home/graph_editor \
-dit \
streamlit