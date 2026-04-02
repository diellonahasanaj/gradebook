# Gradebook CLI - Homework

This is a lightweight command-line tool for managing student records, course enrollments, and grades.


## Setup
First, set up your virtual environment and activate it:
python -m venv venv
.\venv\Scripts\activate


## Usage
Everything runs through main.py. If you want to see how it works without manually entering a bunch of data, you can run the seed script first:
python -m scripts.seed


## Basic Commands
Add a student: python main.py add-student --name "Diellona Hasanaj"

Add a course: python main.py add-course --code CS50 --title "Intro to CS"

Enrollment: python main.py enroll --student-id 1 --course CS50

Add a grade: python main.py add-grade --student-id 1 --course CS50 --grade 95


## Checking Results
You can list out your data or calculate averages directly:
python main.py list students
python main.py gpa --student-id 1


## Technical Notes
Data: All information is stored as a JSON blob in data/gradebook.json. If things get messy, you can just delete that file to reset the state.

Logs: If a command fails silently, check logs/app.log. I’ve set it up to track validation errors (like trying to add a grade for a course a student isn't in).

Tests: I wrote basic unit tests for the service layer logic. Run them via:
python -m unittest discover -s tests


## Project Structure
models.py: Defines the Student, Course, and Grade objects.

storage.py: Handles the work of reading/writing to the JSON file.

service.py: Contains the actual business logic (GPA calculation, enrollment rules).

main.py: The CLI wrapper.