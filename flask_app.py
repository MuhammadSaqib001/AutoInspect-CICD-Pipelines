#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
from flask import Flask,request,render_template
from flask_cors import CORS
from roboflow import Roboflow
import requests
import time

# In[4]:


app = Flask(__name__)
CORS(app)

@app.route('/livestream/' ,methods=['POST','GET'])
def uploadFile():
    # # Upload file flask
    # uploaded_img = request.files['uploaded-file']
    # # Extracting uploaded data file name
    # # Upload file to database (defined uploaded folder in static path)
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(basepath, 'uploads', 'image.jpg')
    # uploaded_img.save(file_path)
    url_image='https://www.discoversoon.com/wp-content/uploads/2018/10/Surgical-Instruments-Manufacturer-and-Supplier-in-Pakistan.jpg'
    r = requests.get(url_image) # create HTTP response object

    with open(file_path,'wb') as f:
        f.write(r.content)

    file_path='/home/saqib0494/AutoInspect/uploads/image.jpg'
    rf = Roboflow(api_key="jg7DuFlunhwlrYBQaMkX")
    project = rf.workspace().project("defect_detection-geufo")
    model = project.version(7).model


    response=model.predict(file_path,confidence=40, overlap=30).json()
    all_defects=response['predictions']
    count=0
    for x in range(len(all_defects)):
        if all_defects[x]['class']=='Defects':
            count+=1
    return str(count)


@app.route('/service/' ,methods=['POST','GET'])
def default():
   return render_template('index.html')


@app.route('/inference/' ,methods=['POST','GET'])
def inference():
    file_path='/home/saqib0494/AutoInspect/uploads/image.jpg'
    rf = Roboflow(api_key="jg7DuFlunhwlrYBQaMkX")
    project = rf.workspace().project("defect_detection-geufo")
    model = project.version(7).model
    response=model.predict(file_path,confidence=40, overlap=30).json()
    all_defects=response['predictions']
    count=0
    for x in range(len(all_defects)):
        if all_defects[x]['class']=='Defects':
            count+=1
    return str(count)

if __name__ == "__main__":
    app.run()


# In[ ]:



