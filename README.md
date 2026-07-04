# Workout Tracker API

This Flask API stores workout activity in a Supabase database.

Each workout has:

- `name`
- `duration_minutes`
- `type`

## How to Run the Backend

Create and activate a virtual environment:

py -m venv .venv
source .venv/Scripts/activate


### Install
py -m pip install -r requirements.txt

### To Run

flask run --debug

## Routes

- `"/"`
- `GET "/api/workouts"` 
- `POST "/api/workouts"`