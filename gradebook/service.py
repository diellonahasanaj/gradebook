import logging
from .storage import load_data, save_data


def _student_exists(data, student_id):
    return any(student["id"] == student_id for student in data["students"])


def _course_exists(data, course_code):
    return any(course["code"] == course_code for course in data["courses"])


def add_student(name):
    if not name or not name.strip():
        logging.error("Student name cannot be empty")
        raise ValueError("Name cannot be empty")

    data = load_data()
    new_id = len(data["students"]) + 1
    student = {"id": new_id, "name": name.strip()}
    data["students"].append(student)
    save_data(data)
    logging.info(f"Added student: id={new_id}, name={name.strip()}")
    return new_id


def add_course(code, title):
    if not code or not code.strip():
        logging.error("Course code cannot be empty")
        raise ValueError("Course code cannot be empty")

    if not title or not title.strip():
        logging.error("Course title cannot be empty")
        raise ValueError("Course title cannot be empty")

    data = load_data()

    if _course_exists(data, code.strip()):
        logging.error(f"Course already exists: {code.strip()}")
        raise ValueError("Course already exists")

    course = {
        "code": code.strip(),
        "title": title.strip()
    }

    data["courses"].append(course)
    save_data(data)
    logging.info(f"Added course: code={code.strip()}, title={title.strip()}")


def enroll(student_id, course_code):
    data = load_data()
    course_code = course_code.strip()

    if not _student_exists(data, student_id):
        logging.error(f"Student not found: id={student_id}")
        raise ValueError("Student not found")

    if not _course_exists(data, course_code):
        logging.error(f"Course not found: code={course_code}")
        raise ValueError("Course not found")

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            logging.error(f"Duplicate enrollment: student_id={student_id}, course_code={course_code}")
            raise ValueError("Student is already enrolled in this course")

    enrollment = {
        "student_id": student_id,
        "course_code": course_code,
        "grades": []
    }

    data["enrollments"].append(enrollment)
    save_data(data)
    logging.info(f"Enrolled student {student_id} in course {course_code}")


def add_grade(student_id, course_code, grade):
    if not (0 <= grade <= 100):
        logging.error(f"Invalid grade: {grade}")
        raise ValueError("Grade must be between 0 and 100")

    data = load_data()
    course_code = course_code.strip()

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            enrollment["grades"].append(grade)
            save_data(data)
            logging.info(f"Added grade {grade} for student {student_id} in {course_code}")
            return

    logging.error(f"Enrollment not found for student {student_id} in {course_code}")
    raise ValueError("Enrollment not found")


def list_students():
    data = load_data()
    return data["students"]


def list_courses():
    data = load_data()
    return data["courses"]


def list_enrollments():
    data = load_data()
    return data["enrollments"]


def compute_average(student_id, course_code):
    data = load_data()
    course_code = course_code.strip()

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            grades = enrollment["grades"]
            average = sum(grades) / len(grades) if grades else 0
            logging.info(f"Computed average for student {student_id} in {course_code}: {average}")
            return average

    logging.error(f"Enrollment not found for average: student {student_id}, course {course_code}")
    raise ValueError("Enrollment not found")


def compute_gpa(student_id):
    data = load_data()
    averages = []

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["grades"]:
            avg = sum(enrollment["grades"]) / len(enrollment["grades"])
            averages.append(avg)

    gpa = sum(averages) / len(averages) if averages else 0
    logging.info(f"Computed GPA for student {student_id}: {gpa}")
    return gpa