#logical operator (and,or,not) = used to check if two or more conditional statements is true

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay inside!")

# if we put "not" next to if, the conditions are going to change  because of that we should reverse the conditions inside statements