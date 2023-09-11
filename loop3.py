while True:
    user_input = input("Enter an even number: ")
    
    try:
        number = int(user_input)
        
        if number % 2 == 0:
            print(f"{number} is an even number")
        
        else:
            print(f"{number} is not an even number")


    except ValueError:
        print(f'Invalid input, Please enter a valid numbers')