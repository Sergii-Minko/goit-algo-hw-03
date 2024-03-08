import random


def get_numbers_ticket(min, max, quantity):
    numbers = []
    for i in range(quantity):
        number = random.randint(min, max)
        while number in numbers:
            number = random.randint(min, max)
        numbers.append(number)
    return sorted(numbers)


string = "1, 49, 6"
numbers = [int(x) for x in string.split(",")]
min_value = numbers[0]
max_value = numbers[1]
quantity = numbers[2]

print(f"Мінімальне число: {min_value}")
print(f"Максимальне число: {max_value}")
print(f"Кількість чисел: {quantity}")


lottery_numbers = get_numbers_ticket(min_value, max_value, quantity)
print("Ваші лотерейні числа:", lottery_numbers)
