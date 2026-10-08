cafe_name = "Python Cafe"
tax_rate = 0.08

menu = {
    "espresso": 3.00,
    "latte": 4.50,
    "cappuchino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25
    }

order = []

print(f"*** {cafe_name} ***")
name = input("What's your name? ")
rewards = input("Are you a rewards member? (yes/no) ")

print ("""
1. View menu
2. Add an item
3. Remove an item
4. View my order
5. Check out
""")

loop = True

while loop == True:
    option = input("Choose an option (1-5): ")

    if option == "1":
        print(menu)

    elif option == "2":
        add_item = input("What would you like? ")
        amount = int(input("How many? "))
        order.append(add_item)
        print(f"Added {amount} {add_item} to your order.")
    elif option == "3":
        remove_item = input("Which item should I remove? ")
        order.remove(remove_item)
        print(f"Removed one {remove_item}")

    elif option == "4":
        print("--- YOUR ORDER ---")
        print(order)
        print

    elif option =="5":
        print("==== Python Cafe Receipt ====")
        break

    else:
        print("Please choose a number from 1 to 5.")
        loop == True
            
