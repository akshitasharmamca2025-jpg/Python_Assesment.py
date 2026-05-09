# Check for palindrome after removing punctuation and spaces
import string

def check_palindrome():
    original_str = input("Enter a string: ")
    # Convert to lowercase and remove non-alphanumeric characters
    clean_str = "".join(char.lower() for char in original_str if char.isalnum())
    
    if clean_str == clean_str[::-1]:
        print(f"'{original_str}' is a palindrome.")
    else:
        print(f"'{original_str}' is not a palindrome.")

check_palindrome()

"""
Expected Output:
Enter a string: Madam, In Eden, I'm Adam
'Madam, In Eden, I'm Adam' is a palindrome.
"""