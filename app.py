import pickle
import pandas as pd
from flask import Flask,render_template,request

app = Flask(__name__)
model = pickle.load(open("fitai_model.pkl","rb"))

cols = [
    'Age', 
    'Gender', 
    'Height', 
    'Weight', 
    'BMI', 
    'FitnessLevel', 
    'MedicalConditions', 
    'Injuries',
    'FitnessGoals', 
    'ExerciseFrequency', 
    'ExerciseDuration', 
    'PreferredTimeOfDay', 
    'PreferredEnvironment', 
    'ActivityLevel', 
    'DietaryPreferences', 
    'SleepPatterns', 
    'MotivationLevel', 
    'StressLevel', 
    'ExerciseHistory', 
    'WeatherConditions', 
    'GymMembership', 
    'SupportSystem', 
    'GroupClassesPreference'
]

def calculate_bmi(weight, height):
    # Convert height from cm to m
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return bmi

@app.route("/")
def landing_Page():
    return render_template("index.html")

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/predict",methods=["POST"])
def prediction():
    if request.method == "POST":
        Age = int(request.form['Age'])
        Gender = request.form['Gender'] #Checking the option spelling 
        Height = float(request.form['Height'])

        Weight = float(request.form['Weight'])
        BMI = calculate_bmi(Weight, Height)
        FitnessLevel = request.form['FitnessLevel'] #Checking the option spelling 
        
        MedicalConditions = request.form['MedicalConditions'] #Checking the option spelling 
        Injuries = request.form['Injuries'] #Checking the option spelling 
        FitnessGoals = request.form['FitnessGoals'] #Checking the option spelling 
        
        ExerciseFrequency = float(request.form['ExerciseFrequency'])
        ExerciseDuration = request.form['ExerciseDuration'] #Checking the option spelling 
        PreferredTimeOfDay = float(request.form['PreferredTimeOfDay'])
        
        PreferredEnvironment = request.form['PreferredEnvironment'] #Checking the option spelling 
        ActivityLevel = request.form['ActivityLevel'] #Checking the option spelling 
        DietaryPreferences = request.form['DietaryPreferences'] #Checking the option spelling 
        
        SleepPatterns = float(request.form['SleepPatterns']) #Checking the option spelling 
        MotivationLevel = request.form['MotivationLevel'] #Checking the option spelling 
        StressLevel = request.form['StressLevel'] #Checking the option spelling 
        
        ExerciseHistory = request.form['ExerciseHistory'] #Checking the option spelling  
        WeatherConditions = request.form['WeatherConditions'] #Checking the option spelling 
        GymMembership = request.form['GymMembership']
        
        SupportSystem = request.form['SupportSystem']
        GroupClassesPreference = request.form['GroupClassesPreference']

         
        x_sample = [[Age,Gender,Height,Weight,BMI,FitnessLevel,MedicalConditions,Injuries,FitnessGoals,ExerciseFrequency,ExerciseDuration,PreferredTimeOfDay,PreferredEnvironment,ActivityLevel,DietaryPreferences,SleepPatterns,MotivationLevel,StressLevel,ExerciseHistory,WeatherConditions,GymMembership,SupportSystem,GroupClassesPreference]]
        X = pd.DataFrame(x_sample,columns=cols)
        result = model.predict(X)
        print(result)

    return render_template("output.html") 

if __name__ == "__main__":
    app.run(debug=True)