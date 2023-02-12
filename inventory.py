# import modules
from tabulate import tabulate

# Classes section

# create a Shoe class and initialise the following attributes in the constructor:
#   country
#   code
#   product
#   cost
#   quantity.
# remember to initialise cost to a float and quantity to an integer
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    # define method to return the cost of the shoe
    def get_cost(self):
        return self.cost

    # define method to return the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # define method to return a string representation of a class
    def __str__(self):
        return f'''—————————————————————————————————————————————————
Country: \t{self.country}
Code: \t\t{self.code}
Product: \t{self.product}
Cost: \t\t{self.cost}
Quantity: \t{self.quantity}
—————————————————————————————————————————————————
'''
    # define method to put all the above information about a shoe into a list 
    # this will be used to represent this information into a table
    def table_format(self):
        return [self.country, self.code, self.product, self.cost, self.quantity]

    # defing a method to put the above information about the shoe and 
    # the values for each shoe that will be calculated later, into a list
    # this will be used to create a table representing the shoe information and the value of each shoe in the inventory
    def table_for_values(self):
        return [self.country, self.code, self.product, self.cost, self.quantity, self.get_cost() * self.get_quantity()]

# create a list that will be used to store a list of objects of shoes.
shoe_list = []

# variables to differentiate outputs making them different colours and/or bold:
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
PURPLE = "\033[95m"
BOLD = "\033[1m"
UNDERLINE = '\033[4m'
END = "\033[0m"


# Functions section

# define a function to read the data about the shoes from the inventory.txt file
def read_shoes_data():
    # create variable representing the file and set it to None
    #   try opening the file to read into and convert it to a list
    #   skipping first line of the file
    f = None
    try:
        f = open("inventory.txt", "r")
        lines = f.readlines()[1:]

        # for each line of the list version of the file
        #   strip the line of the new line character and split it by the comma creating
        #   variables for each index position pertaining to the country, code, product, cost, and quantity
        #   create a show object from the Shoe class using the above information to that object from the line
        #   append the shoe object to the shoe list
        for line in lines:
            country, code, product, cost, quantity = line.strip("\n").split(",")
            shoe = Shoe(country, code, product, cost, quantity)
            shoe_list.append(shoe)

    # if the file is not found 
    #   print the relevant error message
    except FileNotFoundError as error:
        print(f"{RED}Error. This File Cannot Be Found.{END}")
        print(error)
    
    # finally if the file is found
    #   close the file
    finally:
        if f is not None:
            f.close()


# define a function that will allow a user to capture data
# about a shoe and use this data to create a shoe object
# and append this object inside the shoe list.
def capture_shoes():
    # print the relevant message prompting the user to enter the following information about new shoe
    print(f"{UNDERLINE}Please Give The Following Information About The Shoe{END}\n")

    # ask the user to input the country of the new shoe
    country = input("Country: \t").title()

    # assuming that the codes for each product should be unique and therefore should not be duplicated
    # create a boolean that will be used to check whether the code exists and set it to True
    # while the code exists
    #   ask the user to input the code of the new shoe
    #   set the boolean to False
    #   for each item in the shoe list
    #       if the code that the user input matches a code within the list
    #           print the relevant error message to say it already exists and to try again
    #           set the boolean to True
    code_exists = True
    while code_exists:
        code = input("Code: \t\t")
        code_exists = False
        for item in shoe_list:
            if item.code == code:
                print(f"{RED}This Code Already Exists. Please Choose The Correct Code{END}")
                code_exists = True

    # ask the user for the product name
    #   create a while loop
    #   try 
    #       asking the user for the cost of the shoe and store it as a float 
    #       then break
    #   if the user does not input a number
    #       print the relevant error message and prompt them to try again
    product = input("Product: \t").title()
    while True:
        try:
            cost = float(input("Cost: \t\t"))
            break
        except ValueError:
            print(f"\n{RED}Incorrect Input. Please Try Again.{END}")
            

    # create a while loop
    #   try
    #       asking the quantity of these shoes that they want to store in the inventory and
    #       store as an interger
    #       break
    #   if the user does not input an integer
    #       print the relevant error message and prompt them to try again
    while True:
        try:
            quantity = int(input("Quantity: \t"))
            break
        except ValueError:
            print(f"\n{RED}Incorrect Input. Please Try Again.{END}")

    # create a new shoe object using the Shoe class with
    #  all the information gathered above as attributes
    shoe = Shoe(country, code, product, cost, quantity)

    # append this shoe object to the shoe list
    shoe_list.append(shoe)

    # NB: As per the instructions, I have appended the new shoe to the list however
    # they do not mention adding it to the file so I have not done that

    # print the relevant message to say the shoe has been added successfully
    print(f"\n{GREEN}Operation Successful. A New Product Has Been Added To The Inventory.{END}")


# define a function will allow the user to view all shoes in the list as a table
def view_all():
    # create an empty list that will store all the items as a list and create a 2D list
    item_list = []

    # create a list that will be used to give heading to each column
    top_row = ["Country", "Code", "Product", "Cost", "Quantity"]

    # for each item in the shoe list
    #   append the item to the item list as its own list using the table format method create in the Shoe object
    for item in shoe_list:
        item_list.append(item.table_format())
    
    # create a table using tabulate representing 
    # all the information about each shoe store in the inventory and shoe list
    # to format the table with the 2D item list and the top row of heading
    # NB: The supplementary lecture helped and explained how to use this module and I used this in my program
    # I also did some research about tabulate and came across the following article which was aslo a great help particularly
    # in formatting the grid
    # Bansal, I. (2021) Python tabulate module: How to easily create tables in python?, AskPython. 
    # Available at: https://www.askpython.com/python-modules/tabulate-tables-in-python (Accessed: February 9, 2023). 
    inventory_table = tabulate(item_list, top_row, tablefmt='fancy_grid')

    # print the inventory table
    print(inventory_table)


# define a function that will restock the shoe with the lowest quantity stock
def re_stock():
    # create a variable that will store the shoe that has the minimum quantity and
    # initialise to -1
    minimum_quantity = -1

    # create a variable that will keep track of the index of a shoe in the list
    index_entry = 0

    # for each item in the shoe list
    #   if the quantity of that item is lower than the minimum quantity varialbe or
    #   if the minimum quantity is still -1
    #       the lowest quantity is equal to the quantity of that item
    #       create a variable to store the index of this shoe
    #   increment the index by 1
    for item in shoe_list:
        if item.quantity < minimum_quantity or minimum_quantity == -1:
            minimum_quantity = item.quantity
            smallest_index = index_entry
        index_entry += 1
    
    # print the lowest stocked item in the inventory
    print(f"\nYour Lowest stocked item:\n{shoe_list[smallest_index]}\n")

    # create a while loop 
    #   ask the use if they would like to restock this item
    while True:
        choice = input("Would you like to restock this item (Yes/No)? \t\t\t")

        # if the user chooses yes
        #   create a while loop:
        #       try 
        #           asking the user the amount of items they wish to add to the stock and store as integer
        #           add this amount to the quantity of shoes that the shoe with the lowest quantity has
        #           print the relevant message saying the item has been restocked
        #       if the user does not enter an integer
        #           print the relevant error message and prompt them to try again
        if choice.lower() == "yes":
            while True:
                try:
                    restock_quantity = int(input("How many items do you want to add to the existing stock? \t"))
                    shoe_list[smallest_index].quantity += restock_quantity
                    print(f"\n{GREEN}Operation Successful. This Product Has Now Been Restocked.{END}\n")
                    break
                except ValueError:
                    print(f"\n{RED}Invalid Input. Please Try Again.{END}")

            # create an empty list used to store the data
            data = []

            # open the inventory file to write to
            f = open("inventory.txt", "w")

            # append the heading saying country, code, product, cost, quantity to the data list
            data.append("Country,Code,Product,Cost,Quantity\n")

            # for each item in the shoe list
            #   convert the item into a string
            #   append the string the the data list
            # write the lines of the data list to the inventory file
            # break the loop
            for item in shoe_list:
                shoe_string = f"{item.country},{item.code},{item.product},{item.cost},{item.quantity}\n"
                data.append(shoe_string)
            f.writelines(data)
            break

        # if the user chooses no
        #   break the loop
        elif choice.lower() == "no":
            break

        # if the user type something other than a yes or a no
        #   print the relevant error message and prompt them to try again
        else:
            print(f"{RED}Invalid Input. Please Enter Yes or No.{END}")


# define a function will search for a shoe from the list using the shoe code
def search_shoe():
    # create a boolean that will check if the code exists and set to False
    correct_code = False

    # while the code is not correct
    #   ask the user for the code of the shoe that they would like to search for
    #   for each item in the shoe list
    #       if the code of that item is equal to the code the user input
    #           print a message introducing the information about that shoe
    #           print that shoe item
    #           set the correct code boolean to True
    #           break the loop
    while not correct_code:
        shoe_choice = input("Please enter the code of the shoe you are trying to find: ")
        for item in shoe_list:
            if item.code == shoe_choice:
                print(f"\nHere Is The Information Pertaining To The Shoe With Code: {item.code}.\n")
                print(item)
                correct_code = True
                break

        # if the correct code boolean in False
        #   print the relevant error message saying the item does not exist
        if correct_code == False:
            print(f"{RED}Error. This Item Does Not Exist.{END}\n")


# defina function to calculate and display that value for each item
def value_per_item():
    # create an empty list that will store all the data including the value of each shoe
    value_list = []

    # create a list to store the heading used to create the table including a heading for the value
    top_row = ["Country", "Code", "Product", "Cost", "Quantity", "Value"]

    # for each item in the shoe list
    #   append the item to the list using the method created for the value table in the Shoe object
    for item in shoe_list:
        value_list.append(item.table_for_values())

    # create a table representing the information in the list with the top row as the headings and
    # the appropriate formatting
    value_table = tabulate(value_list, top_row, tablefmt='fancy_grid')

    # print the table
    print(value_table)


# define a function to determine the product with the highest quantity and
# print this shoe as being for sale
def highest_qty():
    # create a variable to store the product with the highest quantity and 
    # initialise to 0
    max_quantity = 0

    # create a variable to keep track of the index of each item that will be iterated through
    # and initialise to 0
    index_entry = 0

    # for each item in the shoe list
    #   if the quantity of that item is greater than the product with the highest quantity
    #   store the quantity of that item as the new highest quantity in the variable
    #   store the index of that item
    # increment the index counter by 1
    for item in shoe_list:
        if item.quantity > max_quantity:
            max_quantity = item.quantity
            largest_index = index_entry
        index_entry += 1
    
    # print the item with the highest quantity as being for sale with the relevant message
    print(f"\n{GREEN}FOR SALE ITEM:{END}\n{shoe_list[largest_index]}\n")


# Main Code Section

# print a heading in yellow and bold welcoming the user
print(f"{YELLOW}{BOLD}———————————————————— •Welcome• ———————————————————————{END}\n")

# call the read shoes data function to store all the data from inventory.txt
read_shoes_data()

# create a while loop
#   present a menu to the user and ask them to choose an option from the following:
#       v - \tView all shoes in the inventory
#       a - \tAdd a shoe to the inventory
#       r - \tRestock a shoe in the inventory
#       ss - \tSearch for a shoe in the inventory
#       vs - \tFind the value of each shoe in the inventory
#       fs - \tDisplay the shoe that is for sale
#       e - \tExit
while True:
    menu = input(f'''{UNDERLINE}Please select a choice from the options below:{END}\n
● v - \tView all shoes in the inventory
● a - \tAdd a shoe to the inventory
● r - \tRestock the shoe with the lowest quantity in the inventory
● ss - \tSearch for a shoe in the inventory
● vs - \tFind the value of each shoe in the inventory
● fs - \tDisplay the shoe that is for sale
● e - \tExit
: ''')
    
    # if the user chooses v to view all the shoes in the inventory
    #   print a heading introducing the user to their choice
    #   call the view all function
    if menu.lower() == "v":
        print(f"{CYAN}{BOLD}——————————————— •ALL ITEMS• ———————————————{END}\n")
        view_all()

    # if the user chooses a to add a shoe to the inventory
    #   print a heading introducing the user to their choice
    #   call the capture shoes function to add the shoe
    #   call the view all function to view the updated inventory
    elif menu.lower() == "a":
        print(f"{CYAN}{BOLD}——————————————— •ADD ITEM• ———————————————{END}\n")
        capture_shoes()
        view_all()

    # if the user chooses r to restock a shoe
    #   print a heading introducing the user to their choice
    #   call the function to restock
    elif menu.lower() == "r":
        print(f"{CYAN}{BOLD}——————————————— •RESTOCK• ———————————————{END}\n")
        re_stock()

    # if the user chooses ss to search for a shoe in the inventory
    #   print a heading introducing the user to their choice
    #   call the search shoe function
    elif menu.lower() == "ss":
        print(f"{CYAN}{BOLD}——————————————— •SEARCH• ———————————————{END}\n")
        search_shoe()

    # if the user chooses vs to view each shoes value
    #   print a heading introducing the user to their choice
    #   call the value per item function
    elif menu.lower() == "vs":
        print(f"{CYAN}{BOLD}——————————————— •VALUE PER ITEM• ———————————————{END}\n")
        value_per_item()

    # if the user chooses fs to view the item that is for sale
    #   print a heading introducing the user to their choice
    #   call the highest quantity function
    elif menu.lower() == "fs":
        print(f"{CYAN}{BOLD}——————————————— •SALE ITEMS• ———————————————{END}\n")
        highest_qty()

    # if the user chooses e to exit
    #   print the relevant message thanking the user for using the program
    elif menu.lower() == "e":
        print(f"\n{YELLOW}Thank You For Using This Inventory. Have A Lovely Day!{END}")
        exit()

    # if the user types soemthing other than the options in the menu
    #   print the relevant error message and prompt them to try again
    else:
        print(f"\n{RED}Invalid Selection. Please Try Again.{END}")
