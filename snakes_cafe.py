menu = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
>
"""
# Define a menu to valedate the order process to order only from the menu
menuList = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado", "A Literal Garden", "Ice Cream", "Cake", "Pie","Coffee","Tea","Unicorn Tears"]

def startOrder(order):
    print("Order function executed")
    if menuList.count(order) == 0:
        print("Sorry, we don't have this item in the menu")
    else:
        cart = []
        cart.append(order)
        count = cart.count(order)
        print(f"** {count} order of {order} have been added to your meal **")
        # addingToOrder = input(" > ")
        while order != "quit":
            if order != "quit":
                addingToOrder = input(" > ")
                if(addingToOrder != "quit"):
                    if menuList.count(addingToOrder) == 0:
                        print("Sorry, we don't have this item in the menu")
                    else:
                        cart.append(addingToOrder)
                        count = cart.count(addingToOrder)
                        if count == 1:
                            print(f"** {count} order of {addingToOrder} have been added to your meal **")
                        else:
                            print(f"** {count} orders of {addingToOrder} have been added to your meal **")
                else:
                    print(f"You have ordered the following:")
                    for x in cart:
                        print(x)
                    break
            else:
                print(f"You have ordered the following:")
                for x in cart:
                    print(x)
                break



def intro():
    print("intro function executed")
    order = input(menu)
    while order != "quit":
        startOrder(order)
        break


intro()