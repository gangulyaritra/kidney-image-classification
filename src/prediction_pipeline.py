import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def generate_image_embeddings(self):
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        return np.expand_dims(test_image, axis=0)

    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model.h5"))
        test_image = self.generate_image_embeddings()
        result = np.argmax(model.predict(test_image), axis=1)
        prediction = "Tumor" if result[0] == 1 else "Normal"
        return [{"image": prediction}]
