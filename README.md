# MTCNN-serving-tf2.0
This project implements the serving code of MTCNN facial detection.

## prerequisite tools
install prerequisite tools with the following cmds

```bash
echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | sudo tee /etc/apt/sources.list.d/tensorflow-serving.list && \
	curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | sudo apt-key add -

sudo apt update
sudo apt install python3-opencv tensorflow-model-server
pip3 install numpy tf-nightly-2.0-preview requests
```

## convert the model from hdf5 to saved model

With hdf5 model placed in the current directory, convert it with the following command.

```python
python3 convert_model.py
```

Then you can find mtcnn directory presenting at current directory.

## start serving

After saved model was successfully generated under current directory, start serving the model with following command

```bash
bash start_serving.sh
```

## predict with model server

detect faces with model server by executing

```bash
python3 Detector.py
```

## predict offline

detect faces with local tensorflow by executing

```bash
python3 OfflineDetector.py
```
