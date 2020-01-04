def collatz(number):
    if number % 2 == False:
        return number // 2
    else:
        return 3 * number + 1


def try_out(user_number):
    while user_number != 1:
        user_number = collatz(user_number)
        print(user_number)

try:
    user_number = int(input("Type a number: "))
    try_out(user_number)

except ValueError:
    print("Value must be a number")


