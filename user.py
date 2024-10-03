import re  # regular expressions library


class User:
    """
        Class User:

        Represents a user with a username, email, and password.

        Methods:

        __init__(self, username, email, password)
            Initializes the User object with a username, email, and password.

        set_password(self, password)
            Sets the password for the User object after validation.

        validate_password(self, password)
            Validates the password based on predefined criteria. Returns True if the password is valid, otherwise False.

        display_info(self)
            Displays the user's username and email.

        __str__(self)
            Returns a string representation of the User object in the format 'User(username=<username>, email=<email>)'.
    """
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        if not self.validate_password(password):
            raise ValueError("Password does not meet the validation criteria.")
        self.password = password

    def validate_password(self, password):
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[!@#\$%\^&\*]", password):
            return False
        return True

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def __str__(self):
        return f'User(username={self.username}, email={self.email})'


# Example usage:
if __name__ == "__main__":
    try:
        user = User("john_doe", "john_doe@example.com", "Password123!")
        print(user)
    except ValueError as e:
        print(e)
