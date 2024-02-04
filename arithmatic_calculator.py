import pyfiglet
import os
# title
def print_title(text):
    font = pyfiglet.Figlet()
    title = font.renderText(text)
    print(title)

# operands
def operation():
    print("Enter your first operand")
    first_operand = input("Here : ")
    if len(first_operand) == 0:
        print("You didn't enter anything. Please provide a value.")
    first_operand = int(first_operand)

    print("Enter your second operand")
    second_operand = input("Here : ")
    if len(second_operand) == 0:
        print("You didn't enter anything. Please provide a value.")
    second_operand = int(second_operand)
    print("Operation you want to perform")
    print("Add")
    print("Sub")
    print("Multi")
    print("Div")
    operation = input("Here : ")
    operation.lower()
    match  operation:
        case "add":
            print(f"{first_operand} + {second_operand} = {first_operand+second_operand} ")
        case "sub":
            print(f"{first_operand} - {second_operand} = {first_operand-second_operand} ")
        case "multi":
            print(f"{first_operand} * {second_operand} = {first_operand*second_operand} ")
        case "div":
            print(f"{first_operand} / {second_operand} = {first_operand/second_operand} ")
        case _: 
            print("Invalid task")


print_title("Calculator")
while True:
    operation()
    print("Enter exit for exit : Hit enter for continue")
    exitt = input("Here : ")
    exitt.lower()
    # clear terminal for next loop
    if os.name == 'nt':
        os.system('cls')
    if exitt == "exit":
        break
