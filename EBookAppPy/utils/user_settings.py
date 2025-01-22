import pwinput

class UserSettings:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def change_email(self, new_email):
        """Change the user's email."""
        self.email = new_email

    def change_username(self, new_username):
        """Change the user's username."""
        self.username = new_username

    def change_password(self, new_password):
        """Change the user's password."""
        self.password = new_password

    def __str__(self):
        return f"Email: {self.email}\nUsername: {self.username}"

# Example usage for debugging
if __name__ == "__main__":
    import time

    # Initial user settings
    user = UserSettings(email="user@example.com", username="user123", password="password123")
    print("Initial settings:")
    print(user)

    # Change email
    new_email = input("Enter new email: ")
    user.change_email(new_email)

    # Change username
    new_username = input("Enter new username: ")
    user.change_username(new_username)

    # Change password using secure input
    new_password = pwinput.pwinput(prompt="Enter new password: ")
    user.change_password(new_password)

    # Display updated settings
    print("Updated settings:")
    print(user)

    # Adding a short delay for demonstration
    print("Saving settings...")
    time.sleep(2)
    print("Settings saved successfully.")