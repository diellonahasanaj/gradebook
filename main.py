import argparse
from gradebook import service


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    # add-student
    p = subparsers.add_parser("add-student")
    p.add_argument("--name")

    # add-course
    p = subparsers.add_parser("add-course")
    p.add_argument("--code")
    p.add_argument("--title")

    # enroll
    p = subparsers.add_parser("enroll")
    p.add_argument("--student-id", type=int)
    p.add_argument("--course")

    # add-grade
    p = subparsers.add_parser("add-grade")
    p.add_argument("--student-id", type=int)
    p.add_argument("--course")
    p.add_argument("--grade", type=float)

    # list
    p = subparsers.add_parser("list")
    p.add_argument("type")

    # avg
    p = subparsers.add_parser("avg")
    p.add_argument("--student-id", type=int)
    p.add_argument("--course")

    # gpa
    p = subparsers.add_parser("gpa")
    p.add_argument("--student-id", type=int)

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            print("ID:", service.add_student(args.name))

        elif args.command == "add-course":
            service.add_course(args.code, args.title)

        elif args.command == "enroll":
            service.enroll(args.student_id, args.course)

        elif args.command == "add-grade":
            service.add_grade(args.student_id, args.course, args.grade)

        elif args.command == "list":
            print(getattr(service, f"list_{args.type}")())

        elif args.command == "avg":
            print(service.compute_average(args.student_id, args.course))

        elif args.command == "gpa":
            print(service.compute_gpa(args.student_id))

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()