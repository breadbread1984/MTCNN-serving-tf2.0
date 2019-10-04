#!/bin/bash

cp -rv ./mtcnn /tmp
nohup tensorflow_model_server --rest_api_port=8503 --model_name=pnet --model_base_path="/tmp/mtcnn/pnet" >pnet_server.log 3>&1 &
nohup tensorflow_model_server --rest_api_port=8504 --model_name=rnet --model_base_path="/tmp/mtcnn/rnet" >rnet_server.log 3>&1 &
nohup tensorflow_model_server --rest_api_port=8505 --model_name=onet --model_base_path="/tmp/mtcnn/onet" >onet_server.log 3>&1 &

