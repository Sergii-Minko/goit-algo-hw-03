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
string = input("Введіть діапазон чисел min, max, quantity: ")
if (string != "") & (string.count(",") == 2):
    try:
        numbers = [int(x) for x in string.split(",")]
        min_value = numbers[0]
        max_value = numbers[1]
        quantity = numbers[2]
    except:
        print("Неправильний формат даних")
else:
    print("Неправильний формат даних")

if min_value > max_value:
    min_value, max_value = max_value, min_value

if max_value - min_value + 1 < quantity:
    print("Неправильний формат даних quantity має бути меншим за max - min + 1")
    quantity = (max_value - min_value) // 2
    print("Нова кількість чисел: ", quantity)

print("отримані данні для лотерейнього білету:")
print(f"Мінімальне число: {min_value}")
print(f"Максимальне число: {max_value}")
print(f"Кількість чисел: {quantity}")

lottery_numbers = get_numbers_ticket(min_value, max_value, quantity)
print("Ваші лотерейні числа:", lottery_numbers)
