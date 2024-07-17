import random
import string #used to grab all the upper and lowercase letters, special characters, numbers, and digits

def generate_password(min_length, contain_numbers=True, contain_special_characters=True):
    '''
    create array variables and set them to the corresponding arrays
    string module has built in arrays you can set variables to
    '''
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    '''
    Set characters to letters because the password will always have letters
    Next check the arguments see if the user wants numbers and/or special characters in their password
    Add whichever prefernce the user has to characters
    '''
    characters = letters
    if contain_numbers:
        characters += digits
    if contain_special_characters:
        characters += special_characters

    password = ""
    meets_criteria = False
    has_number = False
    has_special_character = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_characters:
            has_special_character = True

        meets_criteria = True
        if contain_numbers:
            meets_criteria = has_number
        if contain_special_characters:
            meets_criteria = meets_criteria and has_special_character

    return password


min_length = int(input("Enter the minimum length: ")) # type cast b/c input in Python is naturally a string
contain_number = input("Doy you want to have numbers? (y/n) ").lower() == "y"
contain_special_characer = input("Do you want to have special characters? (y/n) ").lower() == "y"
password = generate_password(min_length, contain_number, contain_special_characer)
print(f"The generated password is: {password}")