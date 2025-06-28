# Simple calculator

# conditional statement base project

History_File = "history.txt"

def show_history():
    file = open(History_File , "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("History not found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(History_File , "w")
    file.close()
    print("History Cleared!")

def save_history(equation , result):
     file = open(History_File , "a")
     file.write(equation + " = " + str(result) + '\n' )
     file.close()   

import re

def calculate(user_input):
    try:
        # Use eval to calculate the result of the full expression
        result = eval(user_input)

        # Convert to int if result is a whole number
        if int(result) == result:
            result = int(result)

        print("Result:", result)
        save_history(user_input, result)

    except ZeroDivisionError:
        print("Can't divide by zero")
    except:
        print("Invalid input! Please enter a valid expression like 4 + 6 or (4 + 5) * 2")

def main():
    print("Calculator (type history , clear or exit)") 
    while True:
        user_input = input("Enter calculation (+ , - , * , / , // , % & **) or command history , clear or exit: ")
        if user_input == "exit" :
            print("Thanks for using calculator, Goodbye ")   
            break
        elif user_input == "history" :
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)        


main()