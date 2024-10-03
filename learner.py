from user import User

class Learner(User):
    """
        Learner class, inheriting from User class.

        Methods:
            __init__(self, username, email, password):
                Initializes a new Learner instance.

            display_info(self):
                Displays information about the learner.
    """
    def __init__(self, username, email, password):
        super().__init__(username, email, password)

    def display_info(self):
        super().display_info()

if __name__ == "__main__":
    try:
        learner = Learner("john_doe", "john_doe@example.com", "Password123!")
        learner.display_info()
    except ValueError as e:
        print(e)