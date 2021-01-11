next_comand = " "
prime_number_sum = 0
non_prime_number_sum = 0

while next_comand != "stop":
    next_comand = input()
    if next_comand != "stop":
        next_number = int(next_comand)
        if next_number < 0:
            print("Number is negative.")
        else:
            is_prime = True
            for i in range(2, next_number):
                if next_number % i == 0:
                    is_prime = False
                    break

            if is_prime:
                prime_number_sum += next_number
            else:
                non_prime_number_sum += next_number

print(f"Sum of all prime numbers is: {prime_number_sum}")
print(f"Sum of all non prime numbers is: {non_prime_number_sum}")
