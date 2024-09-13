from fastapi import FastAPI
from utils import json_to_list
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, 'students.json')

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Приветствуем"}

@app.get("/students")
def get_all_students():
    return json_to_list(path_to_json)

@app.get("/students/course/{course}")
def get_students_by_course(course: int):
    students = json_to_list(path_to_json)
    return_list = []
    for student in students:
        if student["course"] == course:
            return_list.append(student)
    return return_list

@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    students = json_to_list(path_to_json)
    return_list = []
    for student in students:
        if student["student_id"] == student_id:
            return_list.append(student)
    return return_list