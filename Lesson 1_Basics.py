#The objective of this lesson is to demonstrate basics understanding a functionality of Python

name = input("What's your name? ")

#f-strings are formatted strings that allow you to use string literal with {}
print(f"Hello, {name}!")

while True:
    question = input("Are you new to programming? ")

    if question == "Yes":
        print(f" Welcoming {name} to the journey of programming. The code has no limit!")
        break
    elif question == "No":
        print("Glad to know we are working with an experienced dev this should be fun :).")
        break
    else:
        print("Sorry, the only answer you can reply with is Yes or No. Try again :D.")
print(f"Thank you {name}, for testing my basic programming demo!")