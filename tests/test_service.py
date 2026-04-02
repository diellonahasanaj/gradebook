import unittest
import os
from gradebook import service


class TestService(unittest.TestCase):

    def setUp(self):
        # Reset data before each test
        if os.path.exists("data/gradebook.json"):
            os.remove("data/gradebook.json")

    def test_add_student(self):
        sid = service.add_student("TestStudent")
        self.assertTrue(sid > 0)

    def test_add_course_and_enroll(self):
        sid = service.add_student("Student1")
        service.add_course("TEST101", "Test Course")

        service.enroll(sid, "TEST101")

        enrollments = service.list_enrollments()
        self.assertTrue(
            any(e["student_id"] == sid and e["course_code"] == "TEST101"
                for e in enrollments)
        )

    def test_add_grade_and_average(self):
        sid = service.add_student("Student2")
        service.add_course("TEST102", "Another Course")
        service.enroll(sid, "TEST102")

        service.add_grade(sid, "TEST102", 100)
        service.add_grade(sid, "TEST102", 80)

        avg = service.compute_average(sid, "TEST102")
        self.assertEqual(avg, 90)

    def test_invalid_grade(self):
        sid = service.add_student("Student3")
        service.add_course("TEST103", "Course")
        service.enroll(sid, "TEST103")

        with self.assertRaises(ValueError):
            service.add_grade(sid, "TEST103", 150)

    def test_duplicate_enrollment(self):
        sid = service.add_student("Student4")
        service.add_course("TEST104", "Course")
        service.enroll(sid, "TEST104")

        with self.assertRaises(ValueError):
            service.enroll(sid, "TEST104")

    def test_compute_gpa(self):
        sid = service.add_student("Student5")
        service.add_course("TEST105", "Course1")
        service.add_course("TEST106", "Course2")

        service.enroll(sid, "TEST105")
        service.enroll(sid, "TEST106")

        service.add_grade(sid, "TEST105", 100)
        service.add_grade(sid, "TEST106", 80)

        gpa = service.compute_gpa(sid)
        self.assertEqual(gpa, 90)


if __name__ == "__main__":
    unittest.main()