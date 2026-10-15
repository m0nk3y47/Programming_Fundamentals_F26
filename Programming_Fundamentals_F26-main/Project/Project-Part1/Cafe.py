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

name =("")

###################################################
def greet (name):
        print(f"Welcome to Python Cafe, {name}!")
        
def show_menu(menu):
    for item in menu.items():
            print (str(item[0]) + ": $" + str(item[1]) )


def show_order(order, menu):
    if len(order) == 0:
        print()
        print("Your order is empty.")
        
    else:
        print()
        print("--- Your Order ---")

    for item in order:
            print (f"{item}: ${menu[item]:.2f}" )
    print ("Items: "+ str(len(order)))

def calculate_subtotal(order, menu):
    for item in order:
        subtotal = 0
        subtotal += int(order[item(1)])
    return subtotal
        

############################################



print(f"*** {cafe_name} ***")
name = input("What's your name? ")
print()
greet(name)
is_member = input("Are you a rewards member? (yes/no) ")


#############################################

member = False


if is_member.lower() == "yes":
    member = True
elif is_member.lower() == "no":
    become_member = input("Would you like to become a member? (yes/no) ")

    if become_member.lower() == "yes":
        member = True
        print("You are now a member of Python Cafe!")
    elif become_member.lower() == "no":
        member = False
        print("You are not a member of Python Cafe.")
        
def get_discounts(subtotal, is_member):
    if member == True and calculate_subtotal >= 20:
        discount = calculate_subtotal * 0.15
        subtotal = calculate_subtotal - discount
        return discount
        return subtotal
    elif member == True and calculate_subtotal >=10:
        discount = calculate_subtotal * 0.10
        subtotal = calculate_subtotal - discount
        return discount
        return subtotal
    elif member == False and calculate_subtotal >=25:
        discount = calculate_subtotal * 0.5
        subtotal = calculate_subtotal - discount
        return discount
        return subtotal
    else:
        discount = 0
        return discount
        return subtotal
def print_receipt(name, order, menu, is_member):
    discount, subtotal = get_discounts(subtotal, is_member)

    tot_tax = subtotal * tax_rate
    overall_total = subtotal - discount + tot_tax
    
    print(f"Customer: {name}")
    for item in order:
            print (f"{item}: ${menu[item]:.2f}" )
    print("Subtotal: $"+ str(calculate_subtotal(order, menu)))
    print("Discount: -$"+ str(discount))
    print("Tax: $"+ str(tot_tax))
    print("Total: $"+ str(overall_total))

   

##############################################
print()

print ("""
1. View menu
2. Add an item
3. Remove an item
4. View my order
5. Check out
""")

loop = True

while loop == True:
    print()
    option = input("Choose an option (1-5): ")
    
#DONE
    if option == "1":
        show_menu(menu)
        
#DONE
    elif option == "2":
        add_item = input("What would you like? ").lower()
        amount = int(input("How many? "))
        for i in range(amount):
            order.append(add_item)
        print(f"Added {amount} {add_item} to your order. ")
        
#DONE
    elif option == "3":
        remove_item = input("What would you like to remove? ").lower()
        order.remove(remove_item)
        print(f"Removed one {remove_item} from your order.")

#DONE        
    elif option == "4":
        show_order(order, menu)
       
#PRINT SUBTOTAL, DISCOUNT, TAX, AND TOTAL
    elif option == "5":
        loop == True
        if len(order) == 0:
            print()
            print("Your order is empty.")
        else:
            
            print("==== Python Cafe Receipt ====")

            print_receipt(name, order, menu, is_member)
            
            print(f"Thanks for visiting, {name}!")

#DONE
    else:
        loop == True
        print("Please choose a number from 1 to 5.")
            
