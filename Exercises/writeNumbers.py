numbers = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

def write_numbers():
    phone_number = input("Type your Phone Number: ")
    for number in phone_number:
        print(numbers.get(number))
    return


write_numbers()