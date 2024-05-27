import pandas as pd
from flask import Flask,render_template,request
from joblib import load

app = Flask(__name__)
model = load("fitai_model.pkl")

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

exercises = [
    "Air Squats",
    "Arm Circles",
    "Assisted Pistol Squats",
    "Bird Dogs",
    "Bodyweight Squats",
    "Brisk Walking",
    "Bulgarian Split Squats",
    "Burpees",
    "Chair Squats",
    "Cycling",
    "Dips",
    "Dumbbell Rows",
    "Elevated Pike Pushups",
    "Glute Bridges",
    "HIIT",
    "Incline Push-Ups",
    "Jogging",
    "Jumping Jacks",
    "Lunges",
    "Marching on the Spot",
    "Modified Plank",
    "Modified Wall Push-Ups",
    "Pilates",
    "Plank",
    "Push-Ups",
    "Reverse Lunges",
    "Running",
    "Seated Leg Lifts",
    "Seated Rowing",
    "Side Leg Lifts",
    "Sliding Leg Curl",
    "Step-ups",
    "Supermans",
    "Swimming",
    "Tricep Dips on Chair",
    "Walking Lunges",
    "Wall Push-Ups",
    "Water Bottle Bicep Curls",
    "Yoga"
]

def calculate_bmi(weight, height):
    # Convert height from cm to m
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return bmi

def Get_exercise(arr):
    output = arr.tolist()[0]
    exercises_indices = [i for i, x in enumerate(output) if x == 1]
    filtered_exercises = [exercises[i] for i in exercises_indices]
    print(filtered_exercises)

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
        Gender = request.form['Gender'] 
        Height = int(request.form['Height'])

        Weight = int(request.form['Weight'])
        BMI = calculate_bmi(Weight, Height)
        FitnessLevel = request.form['FitnessLevel'] 
        
        MedicalConditions = request.form['MedicalConditions'] 
        Injuries = request.form['Injuries'] 
        FitnessGoals = request.form['FitnessGoals'] 
        
        ExerciseFrequency = int(request.form['ExerciseFrequency'])
        ExerciseDuration = int(request.form['ExerciseDuration']) 
        PreferredTimeOfDay = request.form['PreferredTimeOfDay']
        
        PreferredEnvironment = request.form['PreferredEnvironment'] 
        ActivityLevel = request.form['ActivityLevel'] 
        DietaryPreferences = request.form['DietaryPreferences'] 
        
        SleepPatterns = float(request.form['SleepPatterns']) 
        MotivationLevel = request.form['MotivationLevel'] 
        StressLevel = request.form['StressLevel'] 
        
        ExerciseHistory = request.form['ExerciseHistory'] 
        WeatherConditions = request.form['WeatherConditions']  
        GymMembership = request.form['GymMembership']
        
        SupportSystem = request.form['SupportSystem']
        GroupClassesPreference = request.form['GroupClassesPreference']
         
        x_sample = [[Age,Gender,Height,Weight,BMI,FitnessLevel,MedicalConditions,Injuries,FitnessGoals,ExerciseFrequency,ExerciseDuration,PreferredTimeOfDay,PreferredEnvironment,ActivityLevel,DietaryPreferences,SleepPatterns,MotivationLevel,StressLevel,ExerciseHistory,WeatherConditions,GymMembership,SupportSystem,GroupClassesPreference]]
        X = pd.DataFrame(x_sample,columns=cols)
        result = model.predict(X)

        Get_exercise(result)

    return render_template("output.html") 

if __name__ == "__main__":
    app.run(debug=True)