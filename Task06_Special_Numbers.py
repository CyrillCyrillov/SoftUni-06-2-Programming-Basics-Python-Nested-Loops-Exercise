n = int(input())

for i in range(1111, 10000):
    is_spacial_number = True
    help_number = i
    for j in range(1, 5):
        next_digit = help_number % 10
        if next_digit == 0:
            is_spacial_number = False
        elif n % next_digit != 0:
            is_spacial_number = False
        help_number = help_number // 10
    if is_spacial_number:
        print(i, end=" ")

