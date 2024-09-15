from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from datetime import date, datetime
from typing import Optional
import re

from app.models.Major import Major


class Student(BaseModel):
    student_id: int
    phone_number: str = Field(default=..., description="Номер телефона с '+'")
    first_name: str = Field(default=..., min_length=1, max_length=50, description="Имя студента")
    last_name: str = Field(default=..., min_length=1, max_length=50, description="Фамилия студента")
    date_of_birth: date = Field(default=..., description="Дата рождения студента")
    email: EmailStr = Field(default=..., description="Электронный адрес студента")
    address: str = Field(default=..., min_length=10, max_length=100, description="Адрес студента")
    enrollment_year: int = Field(default=...,ge=2002, description="Год поступления студента")
    major: Major = Field(default=..., description="Специальность")
    course: int = Field(default=..., ge=1, le=5, description="Курс (от 1 до 5)")
    special_notes: Optional[str] = Field(default=None, max_length=500, description="Доп заметки")


@field_validator("phone_number")
@classmethod
def validator_phone(cls, values: str) -> str:
    if not re.match(r'^\+\d{1,15}$', values):
        raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 символов')
    return values

@field_validator("date_of_birth")
@classmethod
def validator_date_of_birth(cls, values: date):
    if values and values >=datetime.now().date():
        raise ValueError('Дата рождения не может быть больше сегодяшнего дня')
    return values

class UpdateFilterStudent(BaseModel):
    student_id: int

class StudentUpdate(BaseModel):
    course: int = Field(..., ge=1, le=5, description="Курс должен быть в диапазоне от 1 до 5")
    major: Optional[Major] = Field(..., description="Профиль студента")



# def test_valid_student(data: dict) -> None:
#     try:
#         student = Student(**data)
#         print(student)
#     except ValidationError as e:
#         print(f"Ошибка валидации: {e}")
#
#
# student_data = {
#     "student_id": 1,
#     "phone_number": "+1234567890",
#     "first_name": "Иван",
#     "last_name": "Иванов",
#     "date_of_birth": date(2000, 1, 1),
#     "email": "ivan.ivanov@example.com",
#     "address": "Москва, ул. Пушкина, д. Колотушкина",
#     "enrollment_year": 2002,
#     "major": "Информатика",
#     "course": 8,
#     "special_notes": "Увлекается программированием"
# }
#
# test_valid_student(student_data)
"""Тест модели"""