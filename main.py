# Import required libraries:
import secrets
import string


# Try Branch:
try:
    password_length = int(input("Please enter password length: "))

    if password_length >= 1:

        # Special characters
        special = secrets.choice(string.punctuation)
        # Lowercase letters
        lower = secrets.choice(string.ascii_lowercase)
        # Uppercase letter
        upper = secrets.choice(string.ascii_uppercase)
        # Digit selection
        digit = secrets.choice(string.digits)


        main_characters = list()


        # Append all the selected characters into the list "main_characters".
        main_characters.append(special)

        main_characters.append(lower)

        main_characters.append(upper)

        main_characters.append(digit)


        # Combine: special characters, lower, upper and digits to new variable.
        combine_pass = string.ascii_letters + string.digits + string.punctuation

        # Create additional characters and add to the 4 characters already created
        additional_characters = [secrets.choice(combine_pass) for x in range(password_length - 4)]

        # Add "additional_characters" to list: "main_characters".
        additional_characters.extend(main_characters)

        # Create your password
        password = "".join(additional_characters)

        print(password)

    else:
        print("Please enter a number greater than or equal to 1")


# Except Branch
except:
    print("Please enter a valid number")
