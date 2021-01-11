start = int(input())
end = int(input())

for i in range(start, end + 1):
    next_number_in_string = str(i)
    # next_digit = 0
    odd_sum = 0
    even_sum = 0

    for next_digit, next_value in enumerate(next_number_in_string):
        if next_digit % 2 == 0:
            even_sum += int(next_value)
        else:
            odd_sum += int(next_value)

    if odd_sum == even_sum:
        print(i, end=" ")
