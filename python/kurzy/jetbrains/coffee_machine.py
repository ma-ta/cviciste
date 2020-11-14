class CoffeeMachine:
    from os import sys
    object_n = 0

    WRITE_ACTION = "write-action"
    PRODUCT_TO_BUY = "product-to-buy"
    EXIT = "exit"
    current_state = WRITE_ACTION

    menu_actions = ("buy", "fill", "take", "remaining", EXIT)
    menu_prompt = f"Write action ({', '.join(menu_actions)}):"
    to_buy_prompt = "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
    enough_resources_prompt = "I have enough resources, making you a coffee!"
    not_enough_prompt = "Sorry, not enough {}!"  # "".format() must be used


    resources_espresso_1 = {
        "water": 250,
        "milk": 0,
        "coffee_beans": 16,
        "disposable_cups": 1,
        "cash": 4,
    }
    resources_latte_2 = {
        "water": 350,
        "milk": 75,
        "coffee_beans": 20,
        "disposable_cups": 1,
        "cash": 7
    }
    resources_cappuccino_3 = {
        "water": 200,
        "milk": 100,
        "coffee_beans": 12,
        "disposable_cups": 1,
        "cash": 6,
    }

    def __new__(cls, water, milk, coffee_beans, disposable_cups, cash):
        if cls.object_n < 1:
            cls.object_n += 1
            return object.__new__(cls)
        return None

    def __init__(self, water, milk, coffee_beans, disposable_cups, cash):
        self.water = water  # ml
        self.milk = milk  # ml
        self.coffee_beans = coffee_beans  # g
        self.disposable_cups = disposable_cups  # pcs
        self.cash = cash  # $
        print(self.menu_prompt)

    def __repr__(self):
        return f"Object of CoffeeMachine({self.water}, " \
               f"{self.milk}, " \
               f"{self.coffee_beans}, " \
               f"{self.disposable_cups}, " \
               f"{self.cash})"

    # metody třídy CoffeeMachine

    def take_input(self, current_input):

        if self.current_state == self.WRITE_ACTION:
            action = current_input
            if action == "buy":
                print()
                self.current_state = self.PRODUCT_TO_BUY
                self.buy()
                print()
            elif action == "fill":
                print()
                self.fill()
                print()
            elif action == "take":
                print()
                print(self.take(), end="\n\n")
            elif action == "remaining":
                print()
                print(self.remaining(), end="\n\n")
            elif action == self.EXIT:
                self.current_state = self.EXIT
                return self.current_state
            
            print(self.menu_prompt)

    def buy(self):

        def calculate_resources(product):
            resources = {
                "water": self.water,
                "milk": self.milk,
                "coffee_beans": self.coffee_beans,
                "disposable_cups": self.disposable_cups
            }

            if product == "1":
                product = self.resources_espresso_1
            elif product == "2":
                product = self.resources_latte_2
            elif product == "3":
                product = self.resources_cappuccino_3

            post_resources = dict()
            post_resources.update({"water": resources.get("water") - product.get("water")})
            post_resources.update({"milk": resources.get("milk") - product.get("milk")})
            post_resources.update({"coffee_beans": resources.get("coffee_beans") - product.get("coffee_beans")})
            post_resources.update({"disposable_cups": resources.get("disposable_cups") - product.get("disposable_cups")})

            if min(post_resources.values()) >= 0:
                self.cash += product.get("cash")
                self.water = post_resources.get("water")
                self.milk = post_resources.get("milk")
                self.coffee_beans = post_resources.get("coffee_beans")
                self.disposable_cups = post_resources.get("disposable_cups")
                return "enough"
            else:
                is_missing = []
                for key, val in post_resources.items():
                    if val < 0:
                        is_missing.append(key)
                return is_missing


        choosen_product = "0"
        while choosen_product not in tuple("123") and choosen_product != "back":
            choosen_product = input(self.to_buy_prompt + "\n")
        if choosen_product == "back":
            self.current_state = self.WRITE_ACTION
        else:
            calc_res = calculate_resources(choosen_product)
            if calc_res == "enough":
                print(self.enough_resources_prompt)
                self.current_state = self.WRITE_ACTION
            else:
                to_print = (self.not_enough_prompt).format((", ".join(calc_res).replace("_", " ")))
                if len(calc_res) > 1:
                    rfind = to_print.rfind(",")
                    if rfind > -1:
                        to_print = to_print[:rfind] + " and" + to_print[rfind + 1:]
                print(to_print)
                self.current_state = self.WRITE_ACTION


    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        cash = self.cash
        self.cash = 0
        return f"I gave you ${cash}"

    def remaining(self):
        message = f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
{self.cash} of money """

        return message
            


# konec definice třídy CoffeeMachine


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while coffee_machine.take_input(input()) != coffee_machine.EXIT:
    pass