#Create a shopping cart for a pet store that allows users to add, remove items and display balance. 
#Include section for advice around pet care and adoption centres

#Plan: 
# Create a dictionaries of different items and prices or one nested dictionary with everything 
#Create a menu on a while loop to give options and then several nested menus for different choices.
#eg. menu 1: browse & buy (then browse, remove, basket & check out), 
#adoption centre information (ask for pet type, county), pet care information (which pet and beneath that what info they need). 
#figure out whether my basket shoudl be a list or a dictionary and also how to edit amounts
# define a function for check out so user can access it from any menu
#Figure out how i can adjust quantity of item - can i display this in a grid with tabulate function?
#Figure out my_basket - might need to nest dictionary and set values -eg. {'product' : <default value>, 'price' : <default value>}. 
#would also need to be able to create a new nested dictionary for each item += (revisit lecture 1pm/2pm sunday 14th Jan)
#use round to make sure we only round to 4 digits

#declaring a number checker function for meausuring quantity:

import os
from datetime import datetime, date
DATETIME_STRING_FORMAT = "%Y-%m-%d"


def number_checker(user_input):
    while True:
        try:
            user_input = int(user_input)
            if user_input > 0:
                return user_input
            else:
                user_input = input("Invalid input. Please enter a positive number: ")
        except ValueError:
            user_input = input("Invalid input. Please enter a number: ")

#declaring a function to add to basket:
def add_to_basket(user_input, user_dictionary, username):            
    if user_input in user_dictionary:
        file_path = f"{username}_shopping_basket.txt"
        with open(file_path, 'a') as txt_file:
            txt_file.write(f"{user_input}: {user_dictionary[user_input]}\n" * basket_quantity)
    else:
        user_input = input("That is an invalid choice. Please enter the name of the product you would like to buy")

#declaring a dynamic checkout function:

def check_out():
    with open('mybasket.txt', 'r') as file:
        products = []
        prices = []
        total_cost = 0.0
        print(f"\n\033[1mYour basket:\033[0m\n")
        for line in file:
            print(line)
        # for line in file:
            data = line.split()

            price = float(data[-1])
            prices.append(price)
           

            product = " ".join(data[:-1])
            products.append(product)
            

            total_cost += price

        print(f"\n\033[1mTotal:\033[0m\n")
        print(f"£{total_cost}")



#declaring items availab:

dog_toys = {"Tennis ball" : 2.49 , "Frisbee" : 4.99 , "Chew toy" : 9.60}
dog_food = {"Chicken and turkey" : 1.99 , "Beef" : 2.99 , "Vegetarian" : 0.99}
dog_medical = {"Flea drops" : 12.99 , "Worming tablets" : 11.45 , "Toothpaste" : 4.50}

cat_toys = {}
cat_food = {}
cat_medical = {}

parrot_toys = {}
parrot_food = {}
parrot_medical = {}

my_basket = {}

date_today = date.today()
formatted_date_today = date_today.strftime("%d-%m-%y")
current_month = int(formatted_date_today[3:5])
print(formatted_date_today)
print(current_month)

print('*' * 100)
print("\nWelcome to Daniel's pet shop!\n")
print('*' * 100)

# Creating user txt file if it doesn't exist
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password


logged_in = False
while not logged_in:

    login_register = input("""Type 'login' if you are an existing customer.
                           Or 'register' if you are a new customer.""")
    
    if login_register == "login":

        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        if curr_user not in username_password:
            print("User does not exist")
            continue
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            logged_in = True

    elif login_register == "register":
        new_username = input("New Username: ")
        while True:
            if new_username in username_password:
                print("""That username has already been taken. 
            Please enter a new one or enter 0 to return to previous menu.\n""")
                new_username = input("New Username: ")
            elif new_username == 0:
                break
            else:
                break

        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
        else:
                print("Passwords do no match")

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))    
    else:
        print("""I'm sorry but that is not a valid option.
              Returning to the log in menu.""")
        break

for k in username_password.keys():
    try:
        basket = open (f"{k}_shopping_basket.txt", 'x')
        basket.close()
    except FileExistsError:
        pass
            


main_menu = ' '

while main_menu != '5':
    print('''\n \t Menu: \n
          1. Browse the shop\n
          2. Adoption centre information\n
          3. Pet care information\n
          4. Check out\n
          5. Exit\n''')
    main_menu = input("\nEnter a number from the menu above to proceed: ")

    if not main_menu.isnumeric() or int(main_menu) >= 6:
        print("Invalid input. Please enter either the number '1', '2', '3', '4' or '5'.")
        main_menu = input("\nEnter a number from the menu above to proceed: ")

    if main_menu == '1':
        print('*' * 100)
        print("Welcome to our pet shop. We only stock the best quality food, toys and pet medical supplies!")
        
        shop_menu = ' '
        while shop_menu != '5':
             print('''\n \t Menu: \n
          1. Dog\n
          2. Cat\n
          3. Parrot\n
          4. Check out\n
          5. Go back\n''')
             shop_menu = input("Enter a number from the menu above to proceed: ")

             if not shop_menu.isnumeric() or int(shop_menu) >= 6:
                print("Invalid input. Please enter either the number '1', '2', '3', '4' or '5'.")
                menu1 = input("\nEnter a number from the menu above to proceed: ")

             if shop_menu == '1':
                 print('\n*' * 100)
                 print("\n Welcome to our dog products! We hope you find something for your canine friend.")

                 dog_menu = ' '
                 while dog_menu != '5':
                    print('''\n \t Dog menu: \n
          1. Dog toys\n
          2. Dog food\n
          3. Dog medical supplies\n
          4. Check out\n
          5. Go back\n''')
                    dog_menu = input("Enter a number from the menu above to browse products: ")

                    if not dog_menu.isnumeric() or int(dog_menu) >= 6:
                        print("Invalid input. Please enter either the number '1', '2', '3', '4' or '5'.")
                        dog_menu = input("\nEnter a number from the menu above to proceed: ")

                    if dog_menu == '1':
                        for toys in dog_toys.items():
                            print(*toys)

                        dog_toy_choice = ''
                        while not dog_toy_choice in dog_toys:
                            dog_toy_choice = input("Please type the name of the product you would like to buy:  ")
                            dog_toy_choice = dog_toy_choice.capitalize()
                            basket_quantity = input("How many would you like to buy")
                            basket_quantity = number_checker(basket_quantity)
                            add_to_basket(dog_toy_choice, dog_toys, curr_user)
                        
                    elif dog_menu == '2':
                        for food in dog_food.items():
                            print(*food)
                        
                        dog_food_choice = ''
                        while not dog_food_choice in dog_food:
                            dog_food_choice = input("Please type the name of the product you would like to buy:  ")
                            dog_food_choice = dog_food_choice.capitalize()
                            basket_quantity = input("How many would you like to buy")
                            basket_quantity = number_checker(basket_quantity)
                            add_to_basket(dog_food_choice, dog_food, curr_user)
                            if current_month >=3 <= 7:
                                print("""Its Spring and that means more fleas in the grass.
As the grass grows longer, it is easier for fleas to hide 
and jump onto your dog when it is outside playing. We would recommend 
buying some flea drops""")
                                spring_recommendation_choice = input("Would you like us to add flea drops to your basket? Y/N")
                                if spring_recommendation_choice == 'Y' or 'y':
                                    spring_chosen_recommendation = "Flea drops"
                                    print("Added to your basket")
                                    add_to_basket(spring_chosen_recommendation, dog_medical, curr_user)
                                else:
                                    print("No problem. Returning to menu.")
                            elif current_month > 7 <= 9:
                                print("""Summer is a great time for your dog to go and get some sunshine.
The sunshine is great for their physical and mental health. 
We'd recommend playing some light games of frisbee with your dog.""")   
                                summer_recommendation_choice = input("Would you like us to add a frisbee to your basket? Y/N")
                                if summer_recommendation_choice == 'Y' or 'y':
                                    summer_chosen_recommendation = "Frisbee"
                                    print("Added to your basket")
                                    add_to_basket(summer_chosen_recommendation, dog_toys, curr_user)
                                else:
                                    print("No problem. Returning to menu.")
                    
                    elif dog_menu == '3':
                        for medical_supplies in dog_medical:
                            print(*medical_supplies)
                        
                        dog_medicine_choice = ''
                        while not dog_medicine_choice in dog_medical:
                            dog_medicine_choice = input("Please type the name of the product you would like to buy:  ")
                            dog_medicine_choice = dog_medicine_choice.capitalize()
                            basket_quantity = input("How many would you like to buy")
                            basket_quantity = number_checker(basket_quantity)
                            add_to_basket(dog_medicine_choice, dog_medical, curr_user)
                    
                    elif dog_menu == '4':
                        check_out()

                    else:
                        print("Sorry but you have made an invalid choice.")