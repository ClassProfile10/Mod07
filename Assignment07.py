# ------------------------------------------------- #
# Title: Assignment 07
# Description: '''Working with function, pickeling, and error handeling.
#                 When the program starts, load each "row" of data
#                 in "pickle_Xmas_list.dat" into a python Dictionary.
#                 Add the each dictionary "row" to a python list "table"
#                 data is saved as a byte stream to the file.
#                  previously saved byte stream data is also read from this file.
# '''
# ChangeLog: (Who, When, What)
# C,11.30.2022,Created Script
# ------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
pickle_file_name = "pickle_Xmas_list.dat"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Item,Cost}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection
import pickle

# Processing  --------------------------------------------------------------- #

def read_data_from_file(file_name, list_of_rows):
    """ Reads data from a file into a list of dictionary rows

    :param file_name: (string) with name of file:
    :param list_of_rows: (list) you want filled with file data:
    :return: (list) of dictionary rows
    """
    list_of_rows.clear()  # clear current data
    counter = 0
    try:
        file = open(file_name, "rb")
    except EOFError:
        list_of_rows = []
        counter += 1
    except:
        file = open(file_name, 'x')
        counter +=2
        list_of_rows = []
    if counter == 2:
        pass
    elif counter == 1:
        pass
    else:
        try:
            list_of_rows = pickle.load(file)
        except EOFError:
            pass
        except pickle.UnpicklingError as e:
            raise Exception("Sorry, file must be in byte stream format ")

    file.close()
    return list_of_rows


def add_data_to_list(Item, Cost, list_of_rows):
    """ Adds data to a list of dictionary rows

    :param Item: (string) with name of Item:
    :param Cost: (string) with name of Cost:
    :param list_of_rows: (list) you want filled with file data:
    :return: (list) of dictionary rows
    """
    row = {"Item": str(Item).strip().lower(), "Cost": str(Cost).strip().lower()}

    table_lst.append(row)

    return table_lst

def remove_data_from_list(Item, list_of_rows):
    """ Removes data from a list of dictionary rows

    :param Item: (string) with name of Item:
    :param list_of_rows: (list) you want filled with file data:
    :return: (list) of dictionary rows
    """
    while True:
        tracker = 0
        for row in list_of_rows:
            if row["Item"].lower() == Item.lower():
                print('This row was removed: ', row)
                table_lst.remove(row)
                tracker = + 1
        if tracker == 0:
            print('row not found')
            break
        break
    return list_of_rows


def write_data_to_file(list_of_rows , file_name):
    """ Writes data from a list of dictionary rows to a File

    :param file_name: (string) with name of file:
    :param list_of_rows: (list) you want filled with file data:
    :return: (list) of dictionary rows
    """

    objFile = open(pickle_file_name, "wb")
    pickle.dump(list_of_rows,objFile)
    objFile.close()
    return list_of_rows



# Presentation (Input/Output)  -------------------------------------------- #
def output_menu_Items():
    """  Display a menu of choices to the user

    :return: nothing
    """
    print('''
    Menu of Options
    1) Add a new Item
    2) Remove an existing Item
    3) Save Data to File     
    4) Exit Program
    ''')
    print()  # Add an extra line for looks


def input_menu_choice():
    """ Gets the menu choice from a user

    :return: string
    """
    choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
    print()  # Add an extra line for looks
    return choice


def output_current_Items_in_list(list_of_rows):
    """ Shows the current Items in the list of dictionaries rows

    :param list_of_rows: (list) of rows you want to display
    :return: nothing
    """
    print("******* Current Christmas List *******")
    for row in list_of_rows:
        print(row["Item"] + " ($" + row["Cost"] + ")")
    print("*******************************************")
    print()  # Add an extra line for looks

def input_new_Item_and_Cost():
    """  Gets Item and Cost values to be added to the list

    :return: (string, string) with Item and Cost
    """
    str_Item = str(input("What is the item? - ")).strip()
    str_Cost = str(input("What is the cost? [dollars] - ")).strip()
    return str_Item, str_Cost

def input_Item_to_remove():
    """  Gets the Item name to be removed from the list

    :return: (string) with Item
    """
    str_Item = str(input("What Item would you like to remove? - ")).strip()

    return str_Item


# Main Body of Script  ------------------------------------------------------ #

table_lst = read_data_from_file( file_name=pickle_file_name, list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    output_current_Items_in_list(list_of_rows=table_lst)  # Show current data in the list/table
    output_menu_Items()  # Shows menu
    choice_str = input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Item
        Item, Cost = input_new_Item_and_Cost()
        table_lst = add_data_to_list(Item=Item, Cost=Cost, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Item
        Item = input_Item_to_remove()
        table_lst = remove_data_from_list(Item=Item, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        write_data_to_file(file_name=pickle_file_name, list_of_rows=table_lst)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop
