from flask import *  
import response
import cv2
import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'static/uploads' 
app = Flask(__name__)  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')  
def upload():  
    return render_template("index.html")  
 
@app.route('/upload_image', methods = ['POST'])  
def upload_image():  
    if request.method == 'POST': 
        f = request.files['image']  
        f.filename='input.jpg'
#         filename = secure_filename(f.filename)
        fn=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
        f.save(fn)
#         cv2.imwrite(fil, f)
        gn=response.get_response(fn)
    return render_template("result.html", display_detection = gn, fname = fn)  

if __name__ == '__main__':  
    app.run(debug = True) 