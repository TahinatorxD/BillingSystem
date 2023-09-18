import random
import time
print("|---------------------------|\n"
      "|1| Samosa            ~ $30 |\n"
      "|2| Cheese Parahta    ~ $80 |\n"
      "|3| Cheese Roll       ~ $50 |\n"
      "|4| Cold Drink        ~ $60 |\n"
      "|5| Ice Cream         ~ $30 |\n"
      "|---------------------------|\n")

order_count = 0
total_money = 0
Tip = 0
Discount = 0   
order_number = random.randrange(1, 350)
Name = str(input("Enter Your Name:- "))

try:
    while order_count < 3:
        order = int(input("Choose any two from the menu.\n"
                          "-->"))
        if order == 1:
            print("1 Samosa is on the way, please take a seat")
            order_count = order_count + 1
            total_money = total_money + 30
        elif order == 2:
            print("1 Cheese Parahta is on the way, please take a seat")
            order_count = order_count + 1
            total_money = total_money + 80
        elif order == 3:
            print("1 Cheese Roll is on the way, please take a seat")
            order_count = order_count + 1
            total_money = total_money + 50
        elif order == 4:
            print("1 Cold Drink is on the way, please take a seat")
            order_count = order_count + 1
            total_money = total_money + 60
        elif order == 5:
            Icecream_Flavour = int(input("Please Select The Flavour:\n"
                                         "1 - Mango \n"
                                         "2 - Vanilla\n"
                                         "3 - Chocolate\n"))
            if Icecream_Flavour == 1:
                print("1 Mango IceCream is on the way, please take a seat")
                order_count = order_count + 1
                total_money = total_money + 30
            elif Icecream_Flavour == 2:
                print("1 Vanilla IceCream is on the way, please take a seat")
                order_count = order_count + 1
                total_money = total_money + 30
            elif Icecream_Flavour == 3:
                print("1 Chocolate IceCream is on the way, please take a seat")
                order_count = order_count + 1
                total_money = total_money + 30
            else:
                print("Please Choose the options from the menu!!")
        else:
            print("Your options range from 1 - 5, please select form these!!")

    print("\nYour Sub Total Bill:- ", total_money)
    tax = (total_money*17) / 100
    print("Your tax is:- ", tax)

    Bill = total_money + tax
    if Bill > 200:
        Discount = (Bill*5) / 100
        print("You are eligible for discount:-", Discount)

    try:
        print("------------------------------------")
        Tip = int(input("Enter The Amount you want to Tip:- "))
        print("------------------------------------")
    except Exception as e:
        print("Enter The amount correctly please!!", e)

    Total = total_money + tax + Tip - Discount

    print("Wait while your receipt is being printed", end="")
    time.sleep(0.75)
    print(".", end=""), time.sleep(0.75), print(".", end=""), time.sleep(0.75), print(".", end=""), time.sleep(0.75), print(".", end=""), time.sleep(0.75), print(".", end="\n")


    print("____________________________________\n"
          "| Name                |", Name,    "\n"
          "| Order id            |", order_number,"\n"
          "|-----------------------------------|\n"
          "| Sub Total           |", total_money, "\n"
          "| Tax                 |", tax,         "\n"
          "| Discount            |", Discount,    "\n"
          "|-----------------------------------|\n"
          "| Total               ", Total,        "\n")


except Exception as e:
    print("Please Choose the options from the menu!!", "You can only use numbers!!\n", e)
