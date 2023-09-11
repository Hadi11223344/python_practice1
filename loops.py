

# for i in range(11):
#     if i == 0:
#         continue
#     print(1/i)
user_input = input("Please enter a positive number: ")

try:
    number = int(user_input)
    if number < 0:
        print("Please enter a positive number.")
    else:
        while number >= 0:
            print(number)
            number -= 1

except ValueError:
    print("Invalid input. Please enter a valid positive number.")