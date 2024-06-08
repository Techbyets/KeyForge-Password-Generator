import random
import string
import math
import time
from colorama import Fore, Style

def generate_secure_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def calculate_crack_time(password):
    # Assuming a brute force attack with 1000 guesses per second
    guesses_per_second = 1000
    # Total possible characters
    total_characters = 94
    # Password length
    length = len(password)
    # Total possible combinations
    total_combinations = total_characters ** length
    # Estimated time to crack (in seconds)
    time_to_crack = total_combinations / guesses_per_second
    
    # Convert time to more human-readable format
    time_units = [('seconds', 60), ('minutes', 60), ('hours', 24), ('days', 365), ('years', None)]
    for unit, factor in time_units:
        if factor is not None and time_to_crack >= factor:
            time_to_crack /= factor
        else:
            return f"{time_to_crack:.2f} {unit}"

def assess_security_level(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    complexity_score = 0
    if length >= 8:
        complexity_score += 1
    if has_uppercase and has_lowercase:
        complexity_score += 1
    if has_digit:
        complexity_score += 1
    if has_special:
        complexity_score += 1

    security_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong"
    }

    return security_levels.get(complexity_score, "Unknown")

def loading_screen(message):
    print(Fore.YELLOW + "Loading...")
    print(Style.RESET_ALL)
    time.sleep(2)
    print(message)
    time.sleep(2)

def menu():
    print(Fore.BLUE + "======================")
    print(Fore.GREEN + "   KeyForge Password Generator")
    print(Fore.YELLOW + "   Made by DroidDevHub")
    print(Fore.BLUE + "======================" + Style.RESET_ALL)
    print(Fore.BLUE + "OPTIONS:" + Style.RESET_ALL)
    print(Fore.CYAN + "1. Generate Secure Password")
    print("2. Test Password Security")
    print("3. Check for Update")
    print("4. Exit" + Style.RESET_ALL)

if __name__ == "__main__":
    print(Fore.GREEN + "Welcome to KeyForge Password Generator!")
    print(Style.RESET_ALL)
    time.sleep(2)
    
    while True:
        menu()
        choice = input(Fore.YELLOW + "Enter your choice: " + Style.RESET_ALL)

        if choice == "1":
            loading_screen("Generating secure password...")
            password = generate_secure_password()
            print(Fore.GREEN + "Generated Password:", password + Style.RESET_ALL)
            time.sleep(2)
        elif choice == "2":
            password = input(Fore.YELLOW + "Enter the password to check: " + Style.RESET_ALL)
            loading_screen("Calculating amount of time to crack your password...")
            crack_time = calculate_crack_time(password)
            security_level = assess_security_level(password)
            print(Fore.GREEN + "Estimated time to crack:", crack_time)
            print("Security level:", security_level + Style.RESET_ALL)
            time.sleep(2)
        elif choice == "3":
            loading_screen("Checking for update...")
            print(Fore.GREEN + "No updates available.")
            print("Check out my GitHub profile for more projects: https://github.com/Techbyets" + Style.RESET_ALL)
            time.sleep(2)
        elif choice == "4":
            print(Fore.BLUE + "Exiting..." + Style.RESET_ALL)
            time.sleep(1)
            print(Fore.YELLOW + "Thank you for using KeyForge Password Generator! We hope to see you again soon!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
            time.sleep(1)