
from inventory import resources, revenue
from recipe import menu


def check_resources():
    drink = menu[user_input]["ingredients"]
    for item in drink:
        if drink[item] > resources[item]:
            print(f'Sorry, insufficient {item}.')
            return False
    return True


payment = 0


def process_coins():
    total = 0
    global payment
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total += quarters * 0.25
    total += dimes * 0.1
    total += nickles * 0.05
    total += pennies * 0.01
    if total >= menu[user_input]["cost"]:
        change = total - menu[user_input]["cost"]
        print(f'Payment successful! Here is ${round(change, 2)} in change')
        payment = 1
    elif total <= menu[user_input]["cost"]:
        print("Insufficient payment! Money refunded.")
        payment = 0
    else:
        print("Payment successful!")
        payment = 1


def serve_drink():
    if payment == 1:
        print(f'Here is your {user_input} ☕. Enjoy!')
        revenue["profit"] += menu[user_input]["cost"]
        pack = menu[user_input]["ingredients"]
        for cont in pack:
            resources[cont] = resources[cont] - pack[cont]


is_on = True
while is_on:
    user_input = input("\nWhat would you like to drink? (espresso-$1.5 /latte-$2.5 /cappuccino-$3):  ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        for key in resources:
            print(key, ":", resources[key])
        print("profit : $", revenue["profit"])
    elif user_input in ("espresso", "latte", "cappuccino"):
        if check_resources():
            payment = 0
            process_coins()
            serve_drink()
    else:
        print("Incorrect input! \n")
