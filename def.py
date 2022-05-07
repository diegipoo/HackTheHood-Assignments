def greeting(First_name, last_name):
    print(f"Hey {First_name} {last_name}")
    print("Welcome to the team!")


greeting("Diego", "Ortega")
greeting("Hector", "Ortega")
greeting("Kevin", "Matita")

def get_greeting(name):

    return f"Hi {name}"

new_greeting = get_greeting("Kevin Mata")
second_greeting = get_greeting("Diegipoopoo")
print(new_greeting)
print(second_greeting)

def multiplication(five, another, six = 6):
    return five * six * another

print(multiplication(5, another=7))

def Welcome(f_name, l_name):
    print(f"Wassaap {f_name} {l_name}")
    print("What ya doin out heyuh??")


Welcome("Changa", "Gomez")
Welcome("Marcos", "Ortega")

def multiply(*numbers):
    for number in numbers:
        print(number)

multiply(1, 2, 3, 4, 5)

