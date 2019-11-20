from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
from keras import backend as K

model = load_model('D:\\Users\\chiawei\\konduit\\Github\\Keras_mnist_python\\mnist.h5')

img = load_img(imagePath, False,'grayscale',target_size=(28,28))

x = img_to_array(img)
x = x.astype('float32')
x /= 255
x = np.expand_dims(x, axis=0)

output = model.predict(x)

print(output)

output = str(output)

output_class = model.predict_classes(x)

print(output_class)

output_class = str(output_class)

K.clear_session()
