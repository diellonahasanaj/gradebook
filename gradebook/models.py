from dataclasses import dataclass, field
from typing import List

def validate_name(value: str):
    if not value or not value.strip():
        raise ValueError("Value cannot be empty")
    
def validate_grade(grade: float):
    if not (0 <= grade <= 100):
        raise ValueError("Grade must be between 0 and 100")
    
@dataclass
class Student:
    id: int
    name: str
     
    def __post_init__(self):
        validate_name(self.name)

@dataclass
class Course:
    code: str
    title: str

    def __post_init__(self):
        validate_name(self.code)
        validate_name(self.title)

@dataclass
class Enrollment:
    student_id: int
    course_code: str
    grades: List[float] = field(default_factory=list)

    def add_grade(self, grade: float):
        validate_grade(grade)
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0
