# AutoInspect ML Pipelines [MLOps BS Project]

## 1. Brief Overview :-
The objective of this project is to develop a defect detection system for surgical instruments using machine learning (ML) techniques. The project leverages a comprehensive ML workflow and MLOps pipeline to ensure efficient development, testing, deployment, and monitoring of the ML model. The project utilizes various tools and technologies such as GitHub, GitHub Actions, Jenkins, Docker, PythonAnywhere, Apache Airflow, and React Dashboard for seamless collaboration, testing, deployment, and monitoring.

## 2. Machine Learning Workflow :-
The ML workflow in this project follows a standard process for developing and deploying ML models. The key stages of the ML workflow include:
 
### 2.1 Data Collection :- 
The project starts with the collection of labeled data for training the defect detection model. Surgical instrument images with annotated defect labels are gathered from reliable sources, ensuring diverse and representative samples.

### 2.2 Data Preprocessing :- 
The collected data undergoes preprocessing to enhance the quality and compatibility of the dataset. This stage includes tasks such as data cleaning, image resizing, normalization, and augmentation techniques to improve the robustness of the model.

### 2.3 Model Training :- 
Using the preprocessed dataset, a machine learning model is trained to detect defects in surgical instruments. The chosen model architecture may involve deep learning techniques like convolutional neural networks (CNNs) for better feature extraction from images. The training process includes splitting the dataset into training and validation sets, hyperparameter tuning, and iterative model training.

### 2.4 Model Evaluation :- 
The trained model is evaluated using appropriate evaluation metrics such as accuracy, precision, recall, and F1-score. The evaluation helps assess the performance of the model and its ability to detect defects accurately.

### 2.5 Model Deployment :- 
The final trained model is prepared for deployment in a production environment. This involves converting the model into a deployable format, such as a Docker container, for easy deployment and scalability.

## 3. MLOps Pipeline :-
The MLOps pipeline implemented in this project incorporates several tools and processes to streamline the development, testing, deployment, and monitoring of the ML model. The key components of the MLOps pipeline are depicted as below :

![CI/CD Arhitecture](https://github.com/MuhammadSaqib001/AutoInspect-CICD-Pipelines/blob/main/cicd.jpg)

### 3.1 Collaboration & Version Control with GitHub :-
GitHub is used as the primary version control system, enabling collaboration and tracking changes made by project members. It ensures proper code management, code reviews, and easy integration with other tools in the pipeline. Merge requests and pull requests are utilized by different project members working on separate branches to propose changes to the codebase. These requests are submitted for review by other members, who provide feedback, suggest modifications, and discuss any concerns. Once the review process is completed and all feedback is addressed, the changes are merged into the main branch, ensuring a structured and organized development process.

Merge requests and pull requests in GitHub facilitate collaboration and code review, enabling team members to work on different branches while maintaining code quality and coherence. These processes ensure that proposed changes align with project standards and objectives. By leveraging merge requests and pull requests, the project fosters a collaborative environment that promotes effective code integration and enhances the overall development workflow.

### 3.2 Continuous Integration (CI) with GitHub Actions
GitHub Actions is utilized for continuous integration, allowing automatic testing of the codebase whenever changes are pushed to the repository. It ensures that the codebase remains stable and functional by running relevant tests, including unit tests, integration tests, and code quality checks.

### 3.3 Build Docker Image and Deployment on DockerHub using Jenkins :-
After setting up the GitHub repository, we configured Jenkins and created a new pipeline for this assignment. The pipeline is triggered when changes are made in the GitHub repo. The pipeline first checks out the code from the given repository, and after the build, a docker image is created and then that image is pushed to the Docker Hub. The screenshots of the process are given below: Jenkins, an automation server, is employed to automate the build and deployment process. It builds a Docker image of the ML model and pushes it to Docker Hub, making it easily accessible for deployment.

### 3.4 Deployment and Inference with PythonAnywhere :-
PythonAnywhere is utilized as the hosting platform for deploying the ML model. The deployed API downloads the Docker image from Docker Hub and performs inference on new surgical instrument images, detecting defects based on the trained model.

### 3.5 Batch Processing with Apache Airflow :-
Apache Airflow is integrated into the pipeline for performing batch processing tasks. It schedules and executes periodic data processing tasks, enabling data updates, retraining of the model, and uploading the inferences to Firestore, a cloud-based NoSQL database.

### 3.6 Monitoring and Visualization with React Dashboard :-
A React Dashboard is developed to monitor the performance of the ML model. It provides real-time visualizations, metrics, and analytics on model performance, data drift, and machine drift. The dashboard enables stakeholders to track the model's accuracy The monitoring component of the project plays a crucial role in assessing the performance of the ML model, detecting any deviations or anomalies, and ensuring ongoing data and model quality. Here's an
explanation of the monitoring aspect in your project:

## 4. Performance Monitoring :- 
The ML model's performance is continuously monitored to evaluate its effectiveness in detecting defects in surgical instruments. Key performance metrics such as accuracy, precision, recall, and F1-score are calculated and tracked over time. These metrics provide insights into the model's overall performance and its ability to correctly identify defects. 

### 4.1 Data Drift Monitoring :-
Data drift refers to the concept of changes in the input data distribution over time. Monitoring data drift helps identify situations where the model is being tested on data that significantly differs from the data it was trained on. To detect data drift, statistical measures and techniques can be employed to compare the current data distribution with the training data distribution. This allows you to identify if the model's performance is degrading due to changes in the data.

### 4.2 Model Drift Monitoring :- 
Model drift occurs when the model's performance deteriorates over time due to changes in the underlying patterns or relationships within the data. Monitoring model drift involves tracking performance metrics periodically and comparing them against predefined thresholds. If the performance falls below the thresholds, it indicates a need for retraining or updating the model.

### Anomaly Detection :- 
Anomaly detection techniques can be applied to monitor the behavior of the ML model and identify any unusual or unexpected patterns. This helps in identifying potential issues, such as sudden drops in performance or abnormal predictions, which may require further investigation.

### 4.3 Real-time Visualizations :- 
The React Dashboard mentioned in the project allows stakeholders to visualize and analyze the performance metrics, data drift, and model drift in real-time. It provides interactive charts, graphs, and visual representations of the monitored parameters, allowing for quick and intuitive analysis of the system's health and performance.

### 4.4 Alerting and Notification :- 
To ensure timely response to any issues or deviations, the monitoring system can be integrated with an alerting mechanism. When significant anomalies or performance drops are detected, alerts and notifications can be triggered, notifying the relevant stakeholders or team members. This enables proactive actions to address the issues and maintain the quality of the defect detection .
system.

## 5. Conclusion :-
In conclusion, this project successfully demonstrates a comprehensive ML workflow and MLOps pipeline for defect detection in surgical instruments. By leveraging various tools and technologies, including GitHub, GitHub Actions, Jenkins, Docker, PythonAnywhere, Apache Airflow, and a React Dashboard, the project ensures efficient collaboration, testing, deployment, and monitoring of the ML model.
