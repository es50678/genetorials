from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
from tensorflow.keras import models, layers

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

print(f'previous shape: {train_labels.shape}')
print(f'previous example: {train_labels[0]}')
train_labels = to_categorical(train_labels)
print(f'new shape: {train_labels.shape}')
# each value becomes an array with a corresponding "column" set to 1
# ie: 5 becomes [0, 0, 0, 0, 0, 1, 0, 0, 0]
print(f'new example: {train_labels[0]}')

test_labels = to_categorical(test_labels)

network.fit(train_images, train_labels, epochs=5, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels)
