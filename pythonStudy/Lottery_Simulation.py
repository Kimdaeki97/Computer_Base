from random import randint

def genetrate_number(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers

def draw_winning_numbers():
    winning_numbers = genetrate_number(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

print(draw_winning_numbers())

def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count += 1

    return count


