from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np

def preprocess_image(img, target_size=(128, 128)):
    img = img.convert("RGB")
    img = img.resize(target_size)
    img_array = img_to_array(img)  # no division
    return np.expand_dims(img_array, axis=0)



def predict(model, image_array, class_names):
    pred = model.predict(image_array)
    predicted_index = int(np.argmax(pred[0]))  # ensures it's an int, not tuple or array
    confidence = np.max(pred[0])
    return predicted_index, confidence
    # return class_names[predicted_index] , confidence

