import os

def load_file(file_path):
    """Load content from a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_file(file_path, content):
    """Save content to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def list_files(directory):
    """List all files in a directory."""
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Example usage for debugging
if __name__ == "__main__":
    import time
    import textwrap
    import pwinput

    # Debugging example: Save and load a test file
    test_file = "example.txt"
    content = "This is a test file created using file_handler.py.\n"

    save_file(test_file, content)
    print("File saved.")

    loaded_content = load_file(test_file)
    print("Loaded content:")
    print(loaded_content)

    # Debugging example: List files in the current directory
    print("Listing files in the current directory:")
    print(list_files("."))

    # Using pwinput for debugging secure password input
    password = pwinput.pwinput(prompt="Enter a secure password: ")
    print("Password received securely.")

    # Using textwrap for debugging text formatting
    formatted = textwrap.fill(content, width=40)
    print("Formatted content:")
    print(formatted)

    # Adding a short delay to demonstrate time usage
    print("Waiting for 2 seconds...")
    time.sleep(2)
    print("Done waiting.")