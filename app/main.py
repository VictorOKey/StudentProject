from http.client import HTTPException

from fastapi import FastAPI
from app.models.student import Student, UpdateFilterStudent, StudentUpdate
from utils import json_to_list, add_student, update_student, delete_student
import os
from typing import Optional, List, Dict
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, 'students.json')

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Приветствуем"}

@app.get("/student", response_model= Student)
def get_student_by_id(student_id: Optional[int] = None):
    students = json_to_list(path_to_json)
    if student_id is not None:
        for student in students:
            if student["student_id"] == student_id:
                return student

"""Метод вывода списка студентов с простой фильтрацией необязательных полей:"""
@app.get("/students")
def get_students_by_param(course: Optional[int] = None, major: Optional[str] = None, first_name: Optional[str] = None, last_name: Optional[str] = None):
    students = json_to_list(path_to_json)
    filtered_student = []
    if course and major and first_name and last_name is not None:
        for student in students:
            if student["course"] == course and student["major"] == major and student["first_name"] == first_name and student["last_name"] == last_name:
                filtered_student.append(student)
        return filtered_student
        """Фильтрация по всем полям"""

    if course and major and first_name is not None:
        for student in students:
            if student["course"] == course and student["major"] == major and student["first_name"] == first_name:
                filtered_student.append(student)
        return filtered_student
        """Курс, Профиль, Имя"""

    if course and major and last_name is not None:
        for student in students:
            if student["course"] == course and student["major"] == major and student["last_name"] == last_name:
                filtered_student.append(student)
        return filtered_student
        """Курс, Профиль, Фамилия"""

    if course and first_name and last_name is not None:
        for student in students:
            if student["course"] == course and student["first_name"] == first_name and student["last_name"] == last_name:
                filtered_student.append(student)
        return filtered_student
        """Курс, Имя, Фамилия"""

    if major and first_name and last_name is not None:
        for student in students:
            if student["major"] == major and student["first_name"] == first_name and student["last_name"] == last_name:
                filtered_student.append(student)
        return filtered_student
        """Профиль, Имя, Фамилия"""

    if course and major is not None:
        for student in students:
            if student["course"] == course and student["major"] == major:
                filtered_student.append(student)
        return filtered_student
        """Курс, Профиль"""

    if course and first_name is not None:
        for student in students:
            if student["course"] == course and student["first_name"] == first_name:
                filtered_student.append(student)
        return filtered_student
        """Курс, Имя"""

    if course and last_name is not None:
        for student in students:
            if student["course"] == course and student["last_name"] == last_name:
                filtered_student.append(student)
        return filtered_student
        """Курс, Фамилия"""

    if major and first_name is not None:
        for student in students:
            if student["major"] == major and student["first_name"] == first_name:
                filtered_student.append(student)
        return filtered_student
        """Профиль, Имя"""

    if major and last_name is not None:
        for student in students:
            if student["major"] == major and student["last_name"] == last_name:
                filtered_student.append(student)
        return filtered_student
        """Профиль, Фамилия"""

    if major:
        for student in students:
            if student["major"] == major:
                filtered_student.append(student)
        return filtered_student

    if course:
        for student in students:
            if student["course"] == course:
                filtered_student.append(student)
        return filtered_student

    if first_name:
        for student in students:
            if student["first_name"] == first_name:
                filtered_student.append(student)
        return filtered_student

    if last_name:
        for student in students:
            if student["last_name"] == last_name:
                filtered_student.append(student)
        return filtered_student
    else: return(students)

@app.post("/add_student")
def add_student__(student:Student):
    student_dict = student.dict()
    check = add_student(student_dict)
    if check:
        return {"message": "Успешно добавлен!"}
    else:
        return {"message": "Ошибка при добавлении!"}


@app.put("/update_student")
def update_student(filter_student: UpdateFilterStudent, new_data: StudentUpdate):
    check = update_student(filter_student.dict(), new_data.dict())
    if check:
        return {"message": "Успешно обновлён!"}
    else:
        raise HTTPException(status=400, detail="Ошибка при обновлении!")





# @app.get("/students")
# def get_all_students(course: Optional[int] = None, student_id: Optional[int] = None, major: Optional[str] = None, enrollment_year: Optional[int] = None):
#     students = json_to_list(path_to_json)
#     if course is not None:
#         return_list = []
#         for student in students:
#             if student["course"] == course:
#                 return_list.append(student)
#         return return_list
#     if student_id is not None:
#         return_list = []
#         for student in students:
#             if student["student_id"] == student_id:
#                 return_list.append(student)
#         return return_list
#     if major is not None:
#         return_list = []
#         for student in students:
#             if student["major"] == major:
#                 return_list.append(student)
#         return return_list
#     if enrollment_year is not None:
#         return_list = []
#         for student in students:
#             if student["enrollment_year"] == enrollment_year:
#                 return_list.append(student)
#         return return_list
#     else:
#         return students
"""Метод с параметрами запроса course(курс), student_id(id студента), major(специальность/профиль), enrollment_year(год поступления)"""
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