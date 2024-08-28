while True:   

    operator = input("Enter an operator(+ - * /): ")

    if operator not in ['+', '-', '*', '/']:
        print(f"{operator} is not a valid operator")
        continue

    try: # The try block lets you test a block of code for errors.
        num1 = float(input("Enter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))

        if operator == "+":
            result = num1 + num2
            print(round(result, 3))
        elif operator == "-":
            result = num1 - num2
            print(round(result, 3))
        elif operator == "*":
            result = num1 * num2
            print(round(result, 3))
        elif operator == "/":
            
            if num2 == 0:
                    print("Cannot divide by zero!")
                    continue
            result = num1 / num2
            print(round(result, 3)) 

    except ValueError: # The except block lets you handle the error, code to execute if there is a ValueError.
        print("Invalid input! Please enter numeric values for the numbers.")
        
