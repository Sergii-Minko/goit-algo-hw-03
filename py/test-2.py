import random  # Import the random module to generate random numbers

min_value = 1
max_value = 49
quantity = 6


# Function to generate a list of unique random numbers within a given range
def get_numbers_ticket(min, max, quantity):
    numbers = []
    for i in range(quantity):
        number = random.randint(
            min, max
        )  # Generate a random number within the specified range
        while number in numbers:  # Check if the number is already in the list
            number = random.randint(min, max)  # If yes, generate a new random number
        numbers.append(number)  # Add the unique number to the list
    return sorted(numbers)  # Sort the list and return it


# Function to check and adjust the format of the input string
def check_format(string):
    global min_value, max_value, quantity
    # Check if the input is not empty and contains two commas (indicating three values)
    if (string != "") & (string.count(",") == 2):
        try:
            # Convert the input string into a list of integers
            numbers = [int(x) for x in string.split(",")]
            min_value = numbers[0]  # Extract the minimum value from the list
            max_value = numbers[1]  # Extract the maximum value from the list
            quantity = numbers[2]  # Extract the quantity from the list
        except:
            print(
                "Неправильний формат даних"
            )  # Print an error message if conversion fails
            return False

    else:
        print(
            "Неправильний формат даних"
        )  # Print an error message if input format is incorrect
        return False

    # Ensure the minimum value is less than or equal to the maximum value
    if min_value > max_value:
        min_value, max_value = max_value, min_value

    # If the range is smaller than the requested quantity of numbers, adjust the quantity
    if max_value - min_value + 1 < quantity:
        print("Неправильний формат даних quantity має бути меншим за max - min")
        quantity = (max_value - min_value) // 2
        print("Нова кількість чисел: ", quantity)

    # Print the obtained data for the lottery ticket
    print("Отримані данні для лотерейнього білету:")
    print(f"Мінімальне число: {min_value}")
    print(f"Максимальне число: {max_value}")
    print(f"Кількість чисел: {quantity}")

    return True


# Prompt the user to input the range and quantity of numbers for the lottery ticket
string = input("Введіть Ваш діапазон чисел min, max, quantity: ")

# Loop until the input format is correct
while not check_format(string):
    string = input("Введіть новий діапазон чисел min, max, quantity: ")

# Generate lottery numbers based on the provided range and quantity
lottery_numbers = get_numbers_ticket(min_value, max_value, quantity)

# Print the generated lottery numbers
print("Ваші лотерейні числа:", lottery_numbers)
