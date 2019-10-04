#!/usr/bin/python3

from os.path import join;
import tensorflow as tf;

def main():

        tf.keras.backend.set_learning_phase(0);
        pnet = tf.keras.models.load_model(join('models', 'pnet.h5'));
        rnet = tf.keras.models.load_model(join('models', 'rnet.h5'));
        onet = tf.keras.models.load_model(join('models', 'onet.h5'));
        tf.saved_model.save(pnet, './mtcnn/pnet/1');
        tf.saved_model.save(rnet, './mtcnn/rnet/1');
        tf.saved_model.save(onet, './mtcnn/onet/1');

if __name__ == "__main__":

        assert tf.executing_eagerly();
        main();

