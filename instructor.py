from user import User
from course import Course

class Instructor(User, Course):
    """
    Class representing an Instructor, inheriting from User and Course.

    Methods
    -------
    __init__(username, email, password)
        Initializes the Instructor object with the given username, email, and password.

    add_course(course)
        Adds a course to the instructor's list of courses.

    remove_course(course_code)
        Removes a course from the instructor's list of courses based on the course code.

    display_info()
        Displays the instructor's information and all courses they are teaching.
    """
    def __init__(self, username, email, password):
        super().__init__(username, email, password)
        self.counter_courses = 0
        self.courses = {}

    def add_course(self, course):
        self.courses[self.counter_courses] = course
        self.counter_courses += 1

    def remove_course(self, course_code):
        for i in self.courses:
            if self.courses[i].code == course_code:
                del self.courses[i]
                self.counter_courses -=1
                break


    def display_info(self):
        print(f"Instructor Name: {self.username}")
        print(f"Instructor Email: {self.email}")
        for i in self.courses:
            self.courses[i].display_info()


# Example usage
if __name__ == "__main__":
    instructor = Instructor("john_doe", "john.doe@doe.com", "Password123!")
    course1 = Course("Python Programming", "CS101")
    instructor.add_course(course1)
    instructor.display_info()
