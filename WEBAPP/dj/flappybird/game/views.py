from django.shortcuts import render
import numpy as np
import re
import base64
from io import BytesIO
from PIL import Image

def home(request):
    
    return render(request,"home.html",None)


def about(request):

    return render(request,"about.html",None)

def hand_game(request):

    return render(request,"hand_game.html",None)

def nose_game(request):
    
    return render(request,"nose_game.html",None)


def image(request):
    
    if request.method == "POST": 

        image_b64 = request.values['image']
        image_data = re.sub('^data:image/.+;base64,','',image_b64) 
        decoded = base64.b64decode(image_data)

        image_PIL = Image.open(BytesIO(decoded))
        image_PIL.save("image.png")
        
        image_np = np.array(image_PIL,dtype=np.float32)
        print(image_np[None,...].shape)

        return "got image"
    
    return "waiting for image"


