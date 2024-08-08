import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import numpy as np

class YourModel:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        cnn = tf.keras.models.Sequential()
        cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
        cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
        cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
        cnn.add(tf.keras.layers.Flatten())
        cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))
        cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
        cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return cnn

    def train(self, train_data_dir, val_data_dir, target_size=(64, 64), batch_size=32, epochs=50):
        data_gen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, validation_split=0.2)
        
        train_data_gen = data_gen.flow_from_directory(train_data_dir, target_size=target_size, batch_size=batch_size, class_mode='binary', subset='training', shuffle=True)
        val_data_gen = data_gen.flow_from_directory(val_data_dir, target_size=target_size, batch_size=batch_size, class_mode='binary', subset='validation', shuffle=True)
        
        self.model.fit(x=train_data_gen, validation_data=val_data_gen, epochs=epochs)

    def predict(self, image_path, target_size=(64, 64)):
        test_image = load_img(image_path, target_size=target_size)
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = self.model.predict(test_image)
        
        return 'Negative' if result[0][0] == 1 else 'Positive'
