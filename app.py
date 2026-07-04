import os
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

app = Flask(__name__)
CORS(app)

supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)

@app.get("/")
def home():
    return {"message": "Workout Tracker API is running!"}

@app.get("/api/workouts")
def get_workouts():
    response = supabase.table("w4d3_workout_tracker").select("*").execute()
    return {
        "workouts": response.data,
        "count": len(response.data)
        
        }

@app.post("/api/workouts")
def create_workout():
    data = request.get_json()

    if not data:
        return {"error": "Request body must be JSON"}, 400
    
    if "name" not in data or "duration_minutes" not in data or "type" not in data:
        return {"error": "name, duration_minutes, and type are required"}, 400
    
    new_workout = {
        "name": data.get("name"),
        "duration_minutes": data.get("duration_minutes"),
        "type": data.get("type")
    }

    response = supabase.table("w4d3_workout_tracker").insert(new_workout).execute()
    return {
        "message": "New workout added",
        "workout": response.data
    }, 201
    