import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from mushroom_data import mushroom_names, dict_hongos

app = Flask(__name__)

# Testing
test_images = 'C:/Users/Jekthor/Pictures/Imagenes prueba'
img1 = f'{test_images}/amanita_muscaria.jpg'
img2 = f'{test_images}/boletus_edulis.jpg'
img3 = f'{test_images}/gyromitra_esculenta.jpg'

# Cargar el modelo
model = load_model('models/mushroom_classifier.h5')


# Función para predecir la clase y obtener las dos predicciones principales con sus probabilidades
def predict_image(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(150, 150))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    predictions = model.predict(img_array)[0]
    top_indices = np.argsort(predictions)[-2:][::-1]  # Obtener los índices de las dos predicciones más altas

    top_classes = [mushroom_names[idx] for idx in top_indices]
    top_probabilities = [predictions[idx] for idx in top_indices]

    return top_classes, top_probabilities


# Ejemplo de predicción
img1_classes, img1_probabilities = predict_image(img1)
img2_classes, img2_probabilities = predict_image(img2)
img3_classes, img3_probabilities = predict_image(img3)

# Mostrar resultados
print(f'Predicción para {img1}:')
for i in range(len(img1_classes)):
    print(f'  Clase: {img1_classes[i]}, Probabilidad: {img1_probabilities[i]:.2f}')

print()

print(f'Predicción para {img2}:')
for i in range(len(img2_classes)):
    print(f'  Clase: {img2_classes[i]}, Probabilidad: {img2_probabilities[i]:.2f}')

print()

print(f'Predicción para {img3}:')
for i in range(len(img3_classes)):
    print(f'  Clase: {img3_classes[i]}, Probabilidad: {img3_probabilities[i]:.2f}')




@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    image_path = "./static/uploads/"
    img_folder = os.listdir(image_path)

    if len(img_folder) > 0:
        for img in img_folder:
            os.remove(os.path.join(image_path, img))

    image_obj = request.files['imageFile']

    if image_obj:
        save_path = os.path.join(image_path, image_obj.filename)
        image_obj.save(save_path)

        prediction = predict_image(save_path)
        print(prediction)
        fst_prob = "%.2f" % (prediction[1][0] * 100)
        fst_label = prediction[0][0]
        snd_prob = "%.2f" % (prediction[1][1] * 100)
        snd_label = prediction[0][1]
        pred_details = f'Con una seguridad del {fst_prob}%, la seta es una clase {fst_label}.'

        # img_array = preprocess_image(save_path, target_size=(224, 224))
        #
        # predictions = model.predict(img_array)
        # fst_prob = np.max(predictions) * 100
        # fst_label = np.argmax(predictions)
        #
        # pred_details = f'Con una seguridad del {fst_prob}%, la seta es una clase {fst_label}.'
        #
        print("image_path:", image_path)
        print("image_folder:", img_folder)
        return render_template(
            "index.html",
            prob1=fst_prob,
            prob2=snd_prob,
            data1=dict_hongos[fst_label],
            data2=dict_hongos[snd_label],
            pred=pred_details,
            pathfile=save_path
        )
        # return render_template("index.html", prob1=fst_prob, data1=fst_label, pred=pred_details, pathfile=image_path)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
