# AutoInspect CI/CD Pipeline
## 1. Introduction

AutoInspect is a an automated inspection technique to make sure that surgical equipment are free of any visually examinable manufacturing fault . Our product is capable of classifying / grading a surgical instrument as faulty or non-faulty along with dataset generation for the model training & validation . It would also indicate the type of fault the subject has i.e., breakage ,cracks , pores , corrosion, tucks and scratches . Web-Interface through which the factory's higher authorities will be able to monitor the quality remotely and see quality stats on a daily basis plus the test rig as a prototype for automated image acquisition .

## 2. Scope :-

1. Dataset generation for model training & validation
2. Classifying / grading a surgical instrument as faulty or non-faulty
3. Indicating the type of fault the subject has i.e., breakage ,cracks , pores ,
corrosion, tucks and scratches
4. Web-Interface through which factory's higher authorities will be able to monitor
the quality remotely and see quality stats on daily basis
5. Test rig as a prototype for Automated Image Acquisition

## 3. End Product :- 

A Machine Vision System along with web interfaces for cloud integrationcapable of fault detection in surgical instruments consisting of a vision unit as a test rig for automated image acquisition , computational unit providing environment for the ML models & image processing algorithms to run .

## 4. Methodology

To solve the problem of automated inspection of surgical equipment we have opted the following ways :-

- [DataSet Generation for the Surgical Instruments] - Generated Data of the defected surgical instruments 
- [Pre_Processing & Augmentation] - Used image processing tecniques to prepare our dataset for defect detection
- [Image_Processing Solutions] - Used  reference based and contour based image processing tecniques for defect detection
- [YOLOv5s] - a fine tunned YOLOv5s model for defect detection
- [ImageNet Architectures] - Different pre-trained models for defect detection
- [Defect-Net] - A custom CNN model from scratch

## 5. Technology Stack

1. Tensorflow and Keras (for training deep learning models)
2. NumPy , Pandas and OpenCV (for image processing)
3. Flask (for api development in order to host ML Models on Python Anywhere)
4. React and Django (for web-interfaces)
5. Flutter (for app development ios and android both) 

## 6. Contributors

- Muhammad Taimoor (i190552@nu.edu.pk) Final Year CS Sudent at FAST NUCES , Islamabad
- Muhammad Saqib (i190494@nu.edu.pk) Final Year CS Sudent at FAST NUCES , Islamabad

## 8. Installation

1. Open the requirements.txt file and see the libraries necessary for running these files .
2. Install those libraraies and restart the python ide you are using .
3. Now Clone the repository to run or collab/ run locally on Jupyter Notebook .
4. Alternatobley , running files on online IDEs like Google Colab and Kaggle would be fine too .

![CI/CD Arhitecture](https://github.com/MuhammadSaqib001/AutoInspect-CICD-Pipelines/cicd.jpg)

