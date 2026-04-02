from gradebook import service

id1 = service.add_student("Diellona")
id2 = service.add_student("Stina")

service.add_course("CS101", "Intro to CS")
service.add_course("MATH101", "Math")

service.enroll(id1, "CS101")
service.enroll(id2, "CS101")

service.add_grade(id1, "CS101", 90)
service.add_grade(id1, "CS101", 80)