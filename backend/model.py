import os
import glob
import keras
from keras.models import Sequential
from keras.callbacks import EarlyStopping
from keras.layers import Dense,Dropout

from params import MODEL_PATH

########################################################################################

def initialize_model(X_train, y_train):
    """
    Initialize a TensorFlow Keras model with a defined architecture and
    an early stopping condition.
    """
    # Model architecture
    model=Sequential()
    model.add(Dense(128, activation='relu', input_shape=(len(X_train[0]),)))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(y_train[0]), activation='softmax'))

    # Compile model
    adam = keras.optimizers.Adam(0.001)
    model.compile(optimizer=adam,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Early stopping condition
    early_stopping = EarlyStopping(monitor='accuracy', patience=10, restore_best_weights=True)

    return model, early_stopping

########################################################################################

def train_model(model, X_train, y_train, early_stopping):
    """
    Train a TensorFlow Keras model.
    """
    history = model.fit(X_train, y_train,
                        epochs=200,
                        batch_size=10,
                        callbacks=[early_stopping],
                        verbose=-1)

    return history

########################################################################################

def save_model(model, history):
    """
    Save a TensorFlow Keras model with continuous versioning.
    """
    for version in range(1, 99):
        file = f'kaybot_model_{str(version)}.h5'
        file_path = os.path.join(MODEL_PATH, file)

        if not os.path.exists(file_path):
            model.save(file_path, history)

            print(f'✅ Model saved as "{file}"')
            return None

    print(f'❌ Failed to save Model saved')
    return None

########################################################################################

def load_local_model():
    """
    Load the latest locally saved TensorFlow Keras model.
    """
    local_model_paths = glob.glob(f"{MODEL_PATH}/*")

    model_path_on_disk = sorted(local_model_paths)[-1]
    model = keras.models.load_model(model_path_on_disk)

    return model

########################################################################################
