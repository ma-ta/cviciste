# func exits the app
def exit_app():
    from sys import exit
    print("\nBye!")
    exit()


class Atm:

    # class constructor
    def __init__(self, db_name):
        import sqlite3
        self.db_con = sqlite3.connect(db_name)
        self.db_c = self.db_con.cursor()
        create_table = """
            CREATE TABLE "card" (
                "id"	    INTEGER NOT NULL UNIQUE,
                "number"	TEXT NOT NULL UNIQUE,
                "pin"	    TEXT NOT NULL CHECK(length("pin") == 4),
                "balance"	INTEGER DEFAULT 0,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            """
        try:
            self.db_c.execute(create_table)
        except Exception as error:
            # print("sqlite3:", error)  # debug
            pass

        self.main_menu()

    def __repr__(self):
        return "An object of class Atm()"

    # class methods
    def db_find_cardnum(self, number):
        exists_check = """
            SELECT
                *
            FROM
                "card"
            WHERE
                (number = ?)
            ;
            """
        self.db_c.execute(exists_check, (number,))
        return\
            self.db_c.fetchone()  # returns None or a list

    def db_edit(self, mode, number, pin, balance):
        if mode == "INSERT":
            db_query = """
                INSERT INTO "card"
                ("number", "pin", "balance")
                VALUES
                (?, ?, ?)
                ;
                """
            self.db_c.execute(db_query, (number, pin, balance))
            self.db_con.commit()

    def main_menu(self):
        while True:
            menu = "1. Create an account\n" + \
                   "2. Log into account\n" + \
                   "0. Exit"
            print(menu)
            option = input()

            if option == "1":  # Create an account
                self.new_card()
            elif option == "2":  # Log into account
                self.login()
            elif option == "0":  # Exit
                self.db_c.close()
                self.db_con.close()
                exit_app()

    def luhn_check(self, num):
        # a) multiply odd digits by 2 and subtract 9 if result > 9:
        for i in range(0, len(num)):
            if i % 2 == 0:
                change = int(num[i]) * 2
                if change > 9:
                    change -= 9
                num = num[0:i] + str(change) + num[i+1:]
        # c) (sum of all digits in card_num with check_sum) % 10 == 0
        digits_sum = 0
        for i in range(len(num)):
            digits_sum += int(num[i])

        if digits_sum % 10 != 0:
            return False
        else:
            return True

    def new_card(self):
        #  returns a unique new card number and a random pin
        def cardnum_and_pin():
            from random import randint

            # generates card number
            mii = "4"
            bin_ = mii + "00000"
            while True:
                account = str(randint(0, 999999999 + 1))
                account = ((9 - len(account)) * "0") + account  # adds zeros
                card_num = bin_ + account
                # Luhn Algorithm
                card_num_luhn = []
                for digit in card_num:
                    card_num_luhn.append(int(digit))
                # a) multiply odd digits by 2:
                for i in range(0, len(card_num_luhn) + 1, 2):
                    card_num_luhn[i] *= 2
                # b) subtract 9 to numbers over 9:
                for i in range(len(card_num_luhn)):
                    if card_num_luhn[i] > 9:
                        card_num_luhn[i] -= 9
                # c) (sum of all digits in card_num with check_sum) % 10 == 0
                check_sum = 0
                while (sum(card_num_luhn) + check_sum) % 10 != 0:
                    check_sum += 1
                card_num += str(check_sum)

                if self.db_find_cardnum(card_num) is None:
                    break
                else:
                    # print("Card number already exists!")  # debug
                    pass

            # generates pin
            pin = str(randint(0, 9999 + 1))  # number from 0 to 9999
            pin = ((4 - (len(pin))) * "0") + pin  # adds zeros

            return [card_num, pin]

        card_number, pin_ = cardnum_and_pin()
        self.db_edit("INSERT", card_number, pin_, 0)

        print("\nYour card has been created")
        print("Your card number:")
        print(card_number)
        print("Your card PIN:")
        print(pin_)
        print()

    def login(self):
        def logged_in(card_num):
            def add_income(how_much):
                new_balance = self.db_find_cardnum(card_num)[3] + how_much
                db_query = """
                UPDATE
                    "card"
                SET
                    "balance" = ?
                WHERE
                    "number" = ?
                ;
                """
                self.db_c.execute(db_query, (new_balance, card_num))
                self.db_con.commit()

            def do_transfer(recipient_card):
                def db_transfer():
                    db_query = """
                    UPDATE
                        "card"
                    SET
                        "balance" = ?
                    WHERE
                        "number" = ?
                    ;
                    """
                    sender_balance = str(self.db_find_cardnum(card_num)[3] - amount)
                    recipient_balance = str(self.db_find_cardnum(recipient_card)[3] + amount)

                    self.db_c.execute(db_query, (sender_balance, card_num))
                    self.db_c.execute(db_query, (recipient_balance, recipient_card))
                    self.db_con.commit()

                if card_num != recipient_card:
                    if self.luhn_check(recipient_card):
                        if self.db_find_cardnum(recipient_card) is not None:
                            amount = int(input("Enter how much money you want to transfer:\n"))
                            if amount <= self.db_find_cardnum(card_num)[3]:
                                db_transfer()
                                return "Success!"
                            else:
                                return "Not enough money!"
                        else:
                            return "Such a card does not exist."
                    else:
                        return "Probably you made a mistake in the card number. Please try again!"
                else:
                    return "You can't transfer money to the same account!"

            def close_account():
                db_query = """
                DELETE FROM
                    "card"
                WHERE
                    "number" = ?
                ;
                """
                self.db_c.execute(db_query, (card_num, ))
                self.db_con.commit()

            logged_in_menu = "1. Balance\n" + \
                             "2. Add income\n" + \
                             "3. Do transfer\n" + \
                             "4. Close account\n" + \
                             "5. Log out\n" + \
                             "0. Exit"
            while True:
                print(logged_in_menu)
                option = input()
                if option == "1":  # Balance
                    print("\nBalance:", self.db_find_cardnum(card_num)[3], end="\n\n")
                elif option == "2":  # Add income
                    add_income(int(input("\nEnter income:\n")))
                    print("Income was added!\n")
                elif option == "3":  # Do transfer
                    print("\nTransfer")
                    print(do_transfer(input("Enter card number:\n")), end="\n\n")
                elif option == "4":  # Close account
                    close_account()
                    print("\nThe account has been closed!\n")
                    break
                elif option == "5":  # Log out
                    print()
                    break
                elif option == "0":  # Exit
                    exit_app()

        card_number = input("\nEnter your card number:\n")
        pin = input("Enter your PIN:\n")

        record = self.db_find_cardnum(card_number)

        if record is None:
            print("\nWrong card number or PIN!\n")
        elif pin != record[2]:
            print("\nWrong card number or PIN!\n")
        else:
            print("\nYou have successfully logged in!\n")
            logged_in(record[1])


# new object of class Atm()
atm = Atm("card.s3db")  # db_name
