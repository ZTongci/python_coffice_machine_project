from material import MENU, resources

resources['money'] = 0


def enough_resources(coffee):
    count_false = 0
    ingredients = MENU[coffee]["ingredients"]
    for ingredients_material in MENU[coffee]["ingredients"]:
        if resources[ingredients_material] < ingredients[ingredients_material]:
            count_false += 1
    if count_false == 0:
        return True
    else:
        return False


def enough_ingredients(coffee):
    ingredients = MENU[coffee]["ingredients"]
    result = []
    if coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        for ingredients_material in MENU[coffee]["ingredients"]:
            if resources[ingredients_material] < ingredients[ingredients_material]:
                result.append(ingredients_material)
        if len(result) > 0:
            for element in result:
                print(f'Sorry there is not enough {element}.')
            return False
        else:
            return True


def making_coffee(coffee):
    if coffee == "espresso":
        ingredients = MENU[coffee]["ingredients"]
        if enough_ingredients(coffee):
            take_money(coffee)
            resources["water"] = resources["water"] - ingredients["water"]
            resources["coffee"] = resources["coffee"] - ingredients["coffee"]

    elif coffee == "latte" or coffee == "cappuccino":
        ingredients = MENU[coffee]["ingredients"]
        if enough_ingredients(coffee):
            take_money(coffee)
            resources["water"] = resources["water"] - ingredients["water"]
            resources["coffee"] = resources["coffee"] - ingredients["coffee"]
            resources["milk"] = resources["milk"] - ingredients["milk"]
    else:
        print('Choose again')


def take_money(customer_manu):
    print('Please insert coins.')
    receive_quarters = int(input('how many quarters?:  '))
    receive_dimes = int(input('how many dimes?:  '))
    receive_nickles = int(input('how many nickles?:  '))
    receive_pennies = int(input('how many pennies?:  '))
    receive_total = receive_quarters * 0.5 + receive_dimes * 0.1 + 0.05 * receive_nickles + 0.01 * receive_pennies
    if MENU[customer_manu]['cost'] > receive_total:
        print('Sorry that\'s not enough money. Money refunded.')
    else:
        resources['money'] += MENU[customer_manu]['cost']
        charge = receive_total - MENU[customer_manu]['cost']
        print(f'Here is ${charge} in change')
        print(f'Here is your {customer_manu} ☕️. Enjoy!')


while enough_resources("espresso"):
    request_manu = input('What would you like? (espresso/latte/cappuccino): ')
    if request_manu != 'report':
        making_coffee(request_manu)
    else:
        for material in resources:
            if material == "water" or material == "milk":
                print(f"{material}: {resources[material]}ml")
            elif material == "coffee":
                print(f"{material}: {resources[material]}g")
            else:
                print(f"{material}: ${resources[material]}")