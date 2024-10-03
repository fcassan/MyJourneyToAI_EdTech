# This is a sample Python script.
import threading
from sltech import SLTech
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

slTech = SLTech()

def main():
    """
    SMS - School Management System

    This is the main function that provides an interactive menu for managing a school system.
    Users can add, delete, or list courses, instructors, and learners. All operations are
    executed in separate threads.

    :return: None
    """
    option = 0

    while option != 16:
        print ("SMS - School Management System:\n",
            "\n",
            "1. Add a course\n",
            "2. Add a instructor\n",
            "3. Add a learner\n",
            "4. Add a instructor to a course\n",
            "5. Enroll an learner to a course\n",
            "\n",
            "6. Delete an enrolment\n",
            "7. Delete a course from an instructor\n",
            "8. Delete an instructor\n",
            "9. Delete a learner\n",
            "10. Delete a course\n",
            "\n",
            "11. List Courses\n",
            "12. List Instructors\n",
            "13. List Learners\n",
            "14. List Course of an Instructor\n",
            "15. List Learners of Course\n",
            "\n",
            "16. Exit\n")
        option = input("Enter your choice: ", )
        if not option.isnumeric():
            print("Only numbers are allowed!")
        if option == "1":
            t1 = threading.Thread(target=add_course)
            t1.start()
            t1.join()
        elif option == "2":
            t2 = threading.Thread(target=add_instructor)
            t2.start()
            t2.join()
        elif option == "3":
            t3 = threading.Thread(target=add_learner)
            t3.start()
            t3.join()
        elif option == "4":
            t4 = threading.Thread(target=add_instructor_to_course)
            t4.start()
            t4.join()
        elif option == "5":
            t5 = threading.Thread(target=enroll_learner_to_course)
            t5.start()
            t5.join()
        elif option == "6":
            t6 = threading.Thread(target=delete_enrolment)
            t6.start()
            t6.join()
        elif option == "7":
            t7 = threading.Thread(target=delete_course_from_instructor)
            t7.start()
            t7.join()
        elif option == "8":
            t8 = threading.Thread(target=delete_instructor)
            t8.start()
            t8.join()
        elif option == "9":
            t9 = threading.Thread(target=delete_learner)
            t9.start()
            t9.join()
        elif option == "10":
            t10 = threading.Thread(target=delete_course)
            t10.start()
            t10.join()
        elif option == "11":
            t11 = threading.Thread(target=list_courses)
            t11.start()
            t11.join()
        elif option == "12":
            t12 = threading.Thread(target=list_instructors)
            t12.start()
            t12.join()
        elif option == "13":
            t13 = threading.Thread(target=list_learners)
            t13.start()
            t13.join()
        elif option == "14":
            t14 = threading.Thread(target=list_course_of_instructor)
            t14.start()
            t14.join()
        elif option == "15":
            t15 = threading.Thread(target=list_learners_of_course)
            t15.start()
            t15.join()
        elif option == "16":
            exit()
        else:
            print("Invalid option!")


def add_course():

    code = input("Enter course code - use CS as prefix:")
    name = input("Enter course name:")
    try:
        slTech.add_course(name, code)
    except ValueError as error_message:
        print("Add Course error:"  + error_message.__str__())
    else:
        input("Course added successfully!. Press any key to continue...")
    pass

def add_instructor():
    username = input("Enter instructor username:")
    email = input("Enter instructor email:")
    password = input("Enter instructor password:")
    try:
        slTech.add_instructor(username, email, password)
    except ValueError as error_message:
        input("Add Instructor error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Instructor added successfully!. Press any key to continue...")
    pass

def add_learner():
    username = input("Enter learner username:")
    email = input("Enter learner email:")
    password = input("Enter learner password:")
    try:
        slTech.add_learner(username, email, password)
    except ValueError as error_message:
        input("Add Learner error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Learner added successfully!. Press any key to continue...")
    pass

def add_instructor_to_course():
    email = input("Enter instructor email:")
    course_code = input("Enter course code:")
    try:
        slTech.add_instructors_course(course_code, email)
    except ValueError as error_message:
        input("Add Instructor to Course error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Course added to the instructor successfully!. Press any key to continue...")
    pass

def enroll_learner_to_course():
    email = input("Enter learner email:")
    course_code = input("Enter course code:")
    start_date = input("Enter start date:")
    end_date = input("Enter end date:")
    try:
        slTech.enroll_leaner(email, course_code, start_date, end_date)
    except ValueError as error_message:
        input("Enroll Learner to Course error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Learner enrolled to the course successfully!. Press any key to continue...")
    pass

def delete_enrolment():
    learner_email = input("Enter learner email:")
    course_code = input("Enter course code:")
    try:
        slTech.remove_enrollment(learner_email, course_code)
    except ValueError as error_message:
        input("Delete Enrollment error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Enrollment deleted successfully!. Press any key to continue...")
    pass

def delete_course_from_instructor():
    email = input("Enter instructor email:")
    course_code = input("Enter course code:")
    try:
        slTech.remove_instructors_course(course_code, email)
    except ValueError as error_message:
        input("Delete Course from Instructor error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Course deleted from the instructor successfully!. Press any key to continue...")
    pass

def delete_instructor():
    email = input("Enter instructor email:")
    try:
        slTech.remove_instructor(email)
    except ValueError as error_message:
        input("Delete Instructor error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Instructor deleted successfully!. Press any key to continue...")
    pass

def delete_learner():
    email = input("Enter learner email:")
    try:
        slTech.remove_learner(email)
    except ValueError as error_message:
        input("Delete Learner error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Learner deleted successfully!. Press any key to continue...")
    pass

def delete_course():
    code = input("Enter course code:")
    try:
        slTech.remove_course(code)
    except ValueError as error_message:
        input("Delete Course error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Course deleted successfully!. Press any key to continue...")
    pass

def list_courses():
    try:
        slTech.list_all_courses()
    except ValueError as error_message:
        input("List Courses error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Courses listed successfully!. Press any key to continue...")
    pass
def list_instructors():
    try:
        slTech.list_all_instructors()
    except ValueError as error_message:
        input("List Instructors error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Instructors listed successfully!. Press any key to continue...")
    pass
def list_learners():
    try:
        slTech.list_all_learners()
    except ValueError as error_message:
        input("List Learners error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Learners listed successfully!. Press any key to continue...")
    pass
def list_course_of_instructor():
    email = input("Enter instructor email:")
    try:
        slTech.list_courses_instructor(email)
    except ValueError as error_message:
        input("List Course of Instructor error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Courses listed successfully!. Press any key to continue...")
    pass
def list_learners_of_course():
    code = input("Enter course code:")
    try:
        slTech.list_learners_course(code)
    except ValueError as error_message:
        input("List Learners of Course error: "  + error_message.__str__() + ".Press any key to continue... ")
    else:
        input("Learners listed successfully!. Press any key to continue...")
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
