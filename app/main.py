from fastapi import FastAPI
from utils import json_to_list
import os
from typing import Optional

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, 'students.json')

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Приветствуем"}

@app.get("/students")
def get_all_students(course: Optional[int] = None, student_id: Optional[int] = None, major: Optional[str] = None, enrollment_year: Optional[int] = None):
    students = json_to_list(path_to_json)
    if course is not None:
        return_list = []
        for student in students:
            if student["course"] == course:
                return_list.append(student)
        return return_list
    if student_id is not None:
        return_list = []
        for student in students:
            if student["student_id"] == student_id:
                return_list.append(student)
        return return_list
    if major is not None:
        return_list = []
        for student in students:
            if student["major"] == major:
                return_list.append(student)
        return return_list
    if enrollment_year is not None:
        return_list = []
        for student in students:
            if student["enrollment_year"] == enrollment_year:
                return_list.append(student)
        return return_list
    else:
        return students
"""Метод с параметрами запроса course(курс), student_id(id студента) и major(специальность/профиль)"""


# @app.get("/students/course/{course}")
# def get_students_by_course(course: int):
#     students = json_to_list(path_to_json)
#     return_list = []
#     for student in students:
#         if student["course"] == course:
#             return_list.append(student)
#     return return_list
"""Метод вывода студентов по курсу"""


# @app.get("/students/{student_id}")
# def get_student_by_id(student_id: int):
#     students = json_to_list(path_to_json)
#     return_list = []
#     for student in students:
#         if student["student_id"] == student_id:
#             return_list.append(student)
#     return return_list
"""Метод вывода студентов по id"""