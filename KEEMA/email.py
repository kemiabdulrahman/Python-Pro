import random

# Get user's first name and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Generate a random number
random_num = random.randint(0, 100)

# Create possible email options
email_options = [
    f"{first_name}.{last_name}@example.com",
    f"{first_name}{random_num}@example.com",
    f"{first_name[0]}{last_name}@example.com",
    f"{first_name}{last_name[0]}@example.com",
    f"{first_name}{last_name}{random_num}@example.com"
]

# Print the options
print("Please select one of the following email options:")
for i, option in enumerate(email_options):
    print(f"{i+1}. {option}")

# Get user's choice
choice = int(input("Enter your choice (1-5): "))

# Print the selected option
selected_option = email_options[choice-1]
print(f"Your selected email option is: {selected_option}")

