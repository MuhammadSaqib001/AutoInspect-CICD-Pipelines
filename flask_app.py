#!/usr/bin/env python
# coding: utf-8

# ..............................................................................FLASK App for AutoInspect..................................................................
# FLASK app with a restful API that can detects defects in surgical instruments as well as capable for camera calibrations
# It calls multiple models i.e., 3 in a sequence

# Step 1 :- The first model detects whether there is a surgical instrument or not . If there exists no surgical instrument in the picture , it terminates the execution returning a message and a specific HTTP response code (Object Detection)
# Step 2 :- The second in the pipeline classifies the instruments as whther faulty or non-faulty (DEFECT-NET v2)
# Step 3 :- The third model in the model localizes the instruments classified as faulty in the previous step along with indicating the type of fault (YOLOv5)



#Loading libraries necessary for the predictions
import os
from flask import Flask,request,jsonify,render_template
from flask_cors import CORS
from roboflow import Roboflow
import cv2
import base64
import math


# Configure upload folder for Flask application
 

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')
app.config['UPLOAD_FOLDER'] = './uploads/'
CORS(app)

@app.route('/')
def data():
    return render_template('index.html')

  
@app.route('/' ,methods=['POST'])
def upload_image():
    if request.method == 'POST':
        # Upload file flask
        uploaded_img = request.files['uploaded-file']
        uploaded_img=uploaded_img.read()
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', 'image.jpg')

        with open(file_path,'wb') as f:
            f.write(uploaded_img)
        image = cv2.imread(file_path)

        # Resizing all the test images to a specific dimension using cv2
        width = 720  # desired width
        height = 720  # desired height
        image = cv2.resize(image, (width, height))
        cv2.imwrite(file_path, image)


        step=2
        # PHASE-1 :- To see if there exists a surgical instrument or not
        if step==0:
            rf1 = Roboflow(api_key="MUHoUsFm0yl6S7thy4Fe")
            project1 = rf1.workspace().project("autoinspect-zcbxs")
            model1 = project1.version(2).model
            response1=model1.predict(file_path).json()

            surg=response1['predictions']['class']
            if surg=="Surgical":
                step=1


        #PHASE-2 :- To see if there exists a defect in the surgical instrument or not
        if step==1:
            rf2 = Roboflow(api_key="jg7DuFlunhwlrYBQaMkX")
            project2 = rf2.workspace().project("defect_detection-geufo")
            model2 = project2.version(7).model
            response2=model2.predict(file_path,confidence=30, overlap=30).json()
            all_defects=response2['predictions']
            if len(all_defects)>0:
                step=2

        #PHASE-3 :- To see the type of faults and their corresponding measurements
        if step==2:
            rf3 = Roboflow(api_key="MUHoUsFm0yl6S7thy4Fe")
            project3 = rf3.workspace().project("autoinspect-labeller")
            model3 = project3.version(1).model
            response=model3.predict(file_path,confidence=30, overlap=30)

            text_data = str(extract_detail_of_fault(str(response)))
            response.save("prediction.jpg")

            if len(text_data)==0:
                return jsonify({"message": "No Defect Detected in the Surgical Instrument"}),202

            # Encode image data
            with open("prediction.jpg", 'rb') as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

            # Create response object contaning the fault localized image as well as the dimension and their sizes
            response = {
                'text': text_data,
            }
            return jsonify(response),203

        # Extracting uploaded data file name
    return str("Sawi ha Bhai")
#Route for AutoInspect Detection & Classification API endpoint()
# @app.route('/okay' ,methods=['POST','GET'])
def AutoInspect_Detection():

    basepath = os.path.dirname(__file__)
    file_path = os.path.join(basepath, 'uploads', 'image.jpg')

    # Receiving the image from the client request
    image = request.files.get('image')
    image=image.read()

    with open(file_path,'wb') as f:
        f.write(image)

    file_path='/home/saqib0494/AutoInspect/uploads/image.jpg'
    image = cv2.imread(file_path)

    # Resizing all the test images to a specific dimension using cv2
    width = 720  # desired width
    height = 720  # desired height
    image = cv2.resize(image, (width, height))
    cv2.imwrite(file_path, image)


    step=2
    # PHASE-1 :- To see if there exists a surgical instrument or not
    if step==0:
        rf1 = Roboflow(api_key="MUHoUsFm0yl6S7thy4Fe")
        project1 = rf1.workspace().project("autoinspect-zcbxs")
        model1 = project1.version(2).model
        response1=model1.predict(file_path).json()

        surg=response1['predictions']['class']
        if surg=="Surgical":
            step=1


    #PHASE-2 :- To see if there exists a defect in the surgical instrument or not
    if step==1:
        rf2 = Roboflow(api_key="jg7DuFlunhwlrYBQaMkX")
        project2 = rf2.workspace().project("defect_detection-geufo")
        model2 = project2.version(7).model
        response2=model2.predict(file_path,confidence=30, overlap=30).json()
        all_defects=response2['predictions']
        if len(all_defects)>0:
            step=2

    #PHASE-3 :- To see the type of faults and their corresponding measurements
    if step==2:
        rf3 = Roboflow(api_key="MUHoUsFm0yl6S7thy4Fe")
        project3 = rf3.workspace().project("autoinspect-labeller")
        model3 = project3.version(1).model
        response=model3.predict(file_path,confidence=30, overlap=30)

        text_data = str(extract_detail_of_fault(str(response)))
        response.save("prediction.jpg")

        if len(text_data)==0:
            return jsonify({"message": "No Defect Detected in the Surgical Instrument"}),202

        # Encode image data
        with open("/home/saqib0494/prediction.jpg", 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        # Create response object contaning the fault localized image as well as the dimension and their sizes
        response = {
            'text': text_data,
            'image': encoded_string
        }
        return jsonify(response),203


#Route for AutoInspect Camera Calibration API endpoint ()
@app.route('/calibration/' ,methods=['POST','GET'])
def AutoInspect_Calibration():
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(basepath, 'uploads', 'calibration.jpeg')

    # Receiving the image from the client request
    image = request.files.get('image')
    image=image.read()

    with open(file_path,'wb') as f:
        f.write(image)

    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    # Apply Otsu's thresholding to create a binary image
    ret, img_thresh = cv2.threshold(img, 150, 170, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Find contours in the binary image
    contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return_radius=999999
    # Iterate through each contour and fit a circle
    for contour in contours:
        _ = cv2.contourArea(contour)
        (x,y), radius = cv2.minEnclosingCircle(contour)
        if radius> 80 and radius<110:
            img = cv2.circle(img, (int(x),int(y)), int(radius), (0,255,0), 2)

            if radius<return_radius:
                return_radius=radius
    return str(2*return_radius),203


#Function Description :-
#Supporting function that extracts all the necessary details like height , width , class of the prediction and confidence score from the json response containing details of the faults detected
def extract_detail_of_fault(text_data):
    start = 0
    occurrences = []
    while True:
        width_index = text_data.find("width", start)
        if width_index == -1:
            # Substring not found
            break
        comma_index_w = text_data.find(',', width_index)


        height_index = text_data.find("height", comma_index_w)
        comma_index_h = text_data.find(",", height_index)

        confidence_index = text_data.find("confidence", comma_index_h)
        comma_index_co = text_data.find(",", confidence_index)

        class_index = text_data.find("class", comma_index_co)
        comma_index_c = text_data.find(",", class_index)

        substring_w = float(text_data[width_index+8:comma_index_w])
        substring_h = float(text_data[height_index+8:comma_index_h])
        substring_co= float(text_data[confidence_index+13:comma_index_co])
        substring_c= text_data[class_index+9:comma_index_c-1]

        length=math.sqrt(substring_w*substring_w+substring_h*substring_h)

        occurrences.append(substring_c)
        occurrences.append(substring_co)
        occurrences.append(length)
        # Move start index to the next character after the last occurrence
        start = comma_index_c
    return occurrences

# @app.route('/uploader/' ,methods=['POST','GET'])
# def default():
#   return render_template('index.html')

# @app.route('/inference/' ,methods=['POST','GET'])
# def inference():
#     uploaded_img = request.files['uploaded-file']
#     # # Extracting uploaded data file name
#     basepath = os.path.dirname(__file__)
#     file_path = os.path.join(basepath, 'uploads', 'image.jpg')
#     uploaded_img.save(file_path)

#     file_path='/home/saqib0494/AutoInspect/uploads/image.jpg'
#     rf = Roboflow(api_key="jg7DuFlunhwlrYBQaMkX")
#     project = rf.workspace().project("defect_detection-geufo")
#     model = project.version(7).model
#     response=model.predict(file_path,confidence=40, overlap=30).json()
#     all_defects=response['predictions']
#     count=0
#     for x in range(len(all_defects)):
#         if all_defects[x]['class']=='Defects':
#             count+=1
#     return str(count)

if __name__ == "__main__":
    app.run()


# In[ ]:




