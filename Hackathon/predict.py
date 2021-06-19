import numpy as np
import os
from tensorflow import keras
import tensorflow as tf
file_path = os.getenv('HOME') + '/beef/'
model_path = file_path + 'resnet50'
model = keras.models.load_model(model_path+'_aug_new_cam.h5')


def predict(img,model=model):
    img = img.reshape(1,256,256,3)
    img = tf.cast(img, tf.float32)/255.

    return np.array(model(img)*100,dtype=np.float32)
