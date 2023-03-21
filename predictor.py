#!/usr/bin/env python
# coding: utf-8

# In[7]:

from roboflow import Roboflow

def prediction(file_path):
    # model = torch.hub.load('/home/saqib0494/AutoInspect/yolov5',  'custom', path='/home/saqib0494/AutoInspect/best.pt', force_reload=True)  # yolov5n - yolov5x6 or custom
    # pic=imread(file_path)
    # results = model(pic)  # inference
    # response=results.pandas().xyxy[0].to_json(orient="records")  # JSON img1 predictions
    # if len(response)==2:
    #     return "Non-Faulty"
    # return "Faulty"
    rf = Roboflow(api_key="jg7DuFlunhwlrYBQaMkX")
    project = rf.workspace().project("defect_detection-geufo")
    model = project.version(7).model
    return model.predict(file_path, confidence=25, overlap=30).json()