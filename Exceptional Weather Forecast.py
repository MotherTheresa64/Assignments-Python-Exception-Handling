# Task 1: Ask for user input
# Task 2: Attempt to convert input to float
def weather_app():
    try:
        temp = float(input("Please enter the temperature in Fahrenheit"))
# Handle the exception if input is not a number       
    except ValueError:
        print("Please make sure to use a number!")
# Task 3: Print the converted temperature    
    else:
        print((temp -32) * 5/9)
# Task 4: Thank the user        
    finally:
        print("Thanks for using my application!")
weather_app() 