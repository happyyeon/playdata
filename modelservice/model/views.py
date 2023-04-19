from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import base64
import tensorflow as tf
from io import BytesIO
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img


model = tf.keras.models.load_model("./model/cats_dogs_basic_cnn_3.h5")




# Create your views here.
@api_view(["POST"])
def predict(request):
    base64_string = request.data.get('image')
    img = Image.open(BytesIO(base64.b64decode(base64_string)))
    print (type(img))
    img.save("3.png")
    dog_image =img_to_array(load_img("./{}".format("3.png"), target_size=(150,150))).astype('float32')
    img_to_array(load_img("{}".format("3.png"), target_size=(150,150))).astype('float32')
    dog_image = dog_image.reshape(1, 150, 150, 3)
    dog_image /= 255
    rt = model.predict(dog_image)


    if rt < 0.5 :
        rt_dict = {
                'result' : '고양이 사진을 보내셨네요...'
             }
    else:
        rt_dict = {
                'result' : '강아지 사진을 보내셨네요...'
             }
   
    return Response(rt_dict)