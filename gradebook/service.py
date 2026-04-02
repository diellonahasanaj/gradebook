from .storage import load_data, save_data


def add_student(name):
    data = load_data()
    new_id = len(data["students"]) + 1
    student = {"id": new_id, "name": name}
    data["students"].append(student)
    save_data(data)
    return new_id


def add_course(code, title):
    data = load_data()
    data["courses"].append({"code": code, "title": title})
    save_data(data)


def enroll(student_id, course_code):
    data = load_data()
    enrollment = {
        "student_id": student_id,
        "course_code": course_code,
        "grades": []
    }
    data["enrollments"].append(enrollment)
    save_data(data)


def add_grade(student_id, course_code, grade):
    data = load_data()
    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_code"] == course_code:
            e["grades"].append(grade)
            save_data(data)
            return
    raise ValueError("Enrollment not found")


def list_students():
    return load_data()["students"]


def list_courses():
    return load_data()["courses"]


def list_enrollments():
    return load_data()["enrollments"]


def compute_average(student_id, course_code):
    data = load_data()
    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_code"] == course_code:
            grades = e["grades"]
            return sum(grades) / len(grades) if grades else 0
    raise ValueError("Enrollment not found")


def compute_gpa(student_id):
    data = load_data()
    avgs = []

    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["grades"]:
            avg = sum(e["grades"]) / len(e["grades"])
            avgs.append(avg)

    return sum(avgs) / len(avgs) if avgs else 0