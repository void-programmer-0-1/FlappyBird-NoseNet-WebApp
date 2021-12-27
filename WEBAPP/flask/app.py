from flask import Flask,request,render_template
import base64
import numpy as np
from io import BytesIO
from PIL import Image
import re

app = Flask(__name__)

@app.route("/")
def homepage():

    return render_template("home.html")

@app.route("/nose-game")
def nosegame():

    return render_template("nose_game.html")

@app.route("/hand-game")
def handgame():

    return render_template("hand_game.html")

@app.route("/about")
def about():

    return render_template("about.html")    

@app.route("/image",methods=["POST"])
def image():
    
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

if __name__ == "__main__":
    app.run(debug=True)