# FITAI 

## Overview

This project implements an AI-based exercise recommender system designed to suggest personalized exercise routines based on user profiles and preferences. 

## Live Site : 

Access the live exercise recommender system here: https://fitai-hrcp.onrender.com

## Purpose:

The system aims to help users achieve their fitness goals by providing tailored exercise recommendations that consider various factors like:

* User Attributes: Age, height, weight, gender, medical conditions, etc.
* Fitness Goals: Weight loss, muscle building, endurance training, etc.
* Exercise Preferences: Frequency, duration, preferred time of day, environment (gym, home, etc.), activity level, etc.
* Additional Information:Dietary preferences, sleep patterns, motivation level, stress level, exercise history, weather conditions, gym membership, support system, group class preferences, etc.

## Architecture:

The system utilizes a machine learning approach, specifically the Random Forest Classifier algorithm. This algorithm is trained on a dataset of exercise routines and user profiles to learn the relationships between user characteristics and effective exercises.

## Functionalities:

* Users provide their profile information through a user interface.
* The system analyzes the user profile and recommends a set of exercises tailored to their needs and preferences.
* The recommendations include a variety of exercises from 39 unique options, such as squats, lunges, push-ups, cardio exercises, and more.


## Analytic Process Design:

The key steps involved in the AI model development process:

1. Data Collection: Gathering exercise details and user profiles from relevant sources.
2. Data Preprocessing: Cleaning and formatting the data to ensure accuracy and consistency.
3. Feature Engineering: Identifying and extracting relevant features from the data for model training.
4. Model Training: Training the Random Forest Classifier model on the preprocessed data.
5. Evaluation: Assessing the model's performance using metrics like accuracy and precision.
6. Pipeline Creation: Building an automated workflow for running the AI model and generating recommendations.
7. Deployment: Integrating the model into a user-friendly interface for deployment (web application, mobile app, etc.)

## How to install this project 

1. Clone this project : git clone url
2. Install Dependencies : pip install -r requirements.txt
3. Run the porject : python app.py

## Developers 

1. Kinley Norbu Thinley 
2. Sujal Chuwan 
3. Tempel Gyeltshen 
4. Kuenzang Namgyel 