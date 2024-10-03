
class Enrollment():
    """
        class Enrollment
            Represents the enrollment of a learner in a course with specified start and end dates.

            Method __init__(learner, course, startDate, endDate)
                Initializes an Enrollment instance with a learner, course, start date, and end date.

            Method display_info()
                Displays the information of the enrolled learner and course, along with enrollment start and end dates.
    """
    def __init__(self, learner, course, startDate, endDate):
        self.learner = learner
        self.course = course
        self.startDate = startDate
        self.endDate = endDate

    def display_info(self):
        self.learner.display_info()
        self.course.display_info()
        print("Start Date: " + self.startDate, "End Date: "  + self.endDate)


# Example usage
if __name__ == "__main__":
    from learner import Learner
    learner = Learner("john_doe", "john@example.com", "Password123!")
    from course import Course
    course = Course("Python Programming", "CS101")
    enrollment = Enrollment(learner, course,'20.01.2025', '20.05.2025')
    enrollment.display_info()
