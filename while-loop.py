while True :

    name = input ("Enter your name: ")

    while any(char.isdigit() for char in name) or name == "" or len(name) == 1:
        name = input("Enter your name: ")

    age = input("Enter your age: ")

    while age.isdigit() == False or int(age) < 0:
        print("Age can't be letter or age can't be less than 0!")
        age = input("Enter your age: ")

    print(f"Hello {name}!")
    print(f"You're {age} years old!")
