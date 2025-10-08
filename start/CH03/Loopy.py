#!/usr/bin/env python3
# example workign with Loops
#By Rene Garcia 10/08

def hi():
    for i in range(3):
        print("Hello World")
        print(i)

def while_example():
    count = 0
    while count < 6:
        print(f"The account is : {count}")
        count = count + 1

def loop_array():
    fruits = ["Apple", "Banana", "Cherry", "Tomato"]
    for fruit in fruits:
        print(fruit)

def loop_break():
    fruits = ["Apple", "Banana", "Cherry", "Tomato", "Avocado"]
    for fruit in fruits:
        print(fruit)
        if fruit == "Tomato":
            print("That's not a Vegetable?")
            break
            
def nested_loop():
    fruits = ["Apple", "Banana", "Cherry", "Tomato"]
    adj = ["Shiny", "Big", "Tasty", "Tomato?"]
    for fruit in fruits:
        for a in adj:
            print(f"{a} {fruit}")

        


print("Starting")
hi()
while_example()
loop_array()
loop_break()
nested_loop()
print("Done!")