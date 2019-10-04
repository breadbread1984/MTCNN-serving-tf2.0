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
        loaded_pnet = tf.saved_model.load('./mtcnn/pnet/1');
        loaded_rnet = tf.saved_model.load('./mtcnn/rnet/1');
        loaded_onet = tf.saved_model.load('./mtcnn/onet/1');
        infer_pnet = loaded_pnet.signatures['serving_default'];
        infer_rnet = loaded_rnet.signatures['serving_default'];
        infer_onet = loaded_onet.signatures['serving_default'];
        print('pnet\'s output tensor name is ', infer_pnet.structured_outputs);
        print('rnet\'s output tensor name is ', infer_rnet.structured_outputs);
        print('onet\'s output tensor name is ', infer_onet.structured_outputs);

if __name__ == "__main__":

        assert tf.executing_eagerly();
        main();

