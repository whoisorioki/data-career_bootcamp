import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Initialize the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), padding='same', input_shape=(64, 64, 3), activation='relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# To increase Efficiency, add another Convolutional layer
classifier.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full Connection
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dropout(0.5))

# Output layer
classifier.add(Dense(units=80, activation='softmax'))

# Compiling the CNN
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        '/home/whoisorioki/Desktop/GitHub/data-career_bootcamp/Week 8/animal dataset/train',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

test_set = test_datagen.flow_from_directory(
        '/home/whoisorioki/Desktop/GitHub/data-career_bootcamp/Week 8/animal dataset/test',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

# classifier.fit(
#         training_set,
#         steps_per_epoch=len(training_set),
#         epochs=30,
#         validation_data=test_set,
#         validation_steps=len(test_set))

# classifier.save('animal_detection_model.h5')

test_image = image.load_img(
    '/home/whoisorioki/Desktop/GitHub/data-career_bootcamp/Week 8/animal dataset/test/Butterfly/8419a712a72b381f.jpg',
    target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
model = load_model('/home/whoisorioki/Desktop/GitHub/data-career_bootcamp/Week 8/model.h5')
result = model.predict(test_image)
result = np.argmax(result)
class_indices = training_set.class_indices

print(result)

for k, v in class_indices.items():
    if v == result:
        predicted_class = k

print('Predicted class:', predicted_class)

