*11.30.2022*  
*IT FDN 110 A*  
*Assignment 07*  
*GitHub: https://github.com/ClassProfile10/Mod07*  
*Website: https://github.com/ClassProfile10/Mod07*  

# Error Handling and Pickling in Python 

## Introduction
During the seventh week of this course, we focused on error handing and pickling in Python. The main fucus was to learn how to use error handling to both the user and our advantage when writing programs. We learned about pickling in python as this is a way serialize python objects into bytes which the computer can interpret faster. Lastly we built upon our previous knowledge of creating a web page using the GitHub platform. This included formatting text as well as imbedding images on our webpage. The assignment for this week was a bit open ended however required that we demonstrated both error handling and pickling.

## Generating the program 
The script begins with a tittle block to inform any user, editor or even the creator as to the name of the file, a brief description, a creation date, and change log as seen below (Figure 1.1). 
<br/>
<br/>
```
# ------------------------------------------------- #
# Title: Assignment 07
# Description: '''Working with function, pickling, and error handling.
#                 When the program starts, load each "row" of data
#                 in "pickle_Xmas_list.dat" into a python Dictionary.
#                 Add the each dictionary "row" to a python list "table"
#                 data is saved as a byte stream to the file.
#                  previously saved byte stream data is also read from this file.
# '''
# ChangeLog: (Who, When, What)
# C,11.30.2022,Created Script
# ------------------------------------------------- #
``` 
#### *Figure 1.1: Title Block*  
<br/>

Next the main variable were declared that will be used throughout the program (figure 1.2). The first was assigning our text file “pickle_Xmas_list.dat” to a variable named “pickle_file_name.” Next was assigning “file_obj” which was used to create an object that represents a file. The next variable is a dictionary labeled “row_dic” that will represent each dictionary row. Following this we have a “table_lst” a variable which stores all of the dictionary rows. next, we have “choice_str” which captures the users menu selection. Lastly we import the pickle module by calling “import pickle”, this module will be used later on to convert our python objects into a byte stream. 
<br/>
<br/>
```
# Data ---------------------------------------------------------------------- #
# Declare variables and constants
pickle_file_name = "pickle_Xmas_list.dat"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Item,Cost}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection
import pickle
```
#### *Figure 1.2: Variable declaration*  
<br/>

The figure below (Figure 1.3) shows the first function contained in the “Processor” section. The first function, “read_data_from_file”, as you can imagine reads the data contained in the text file. In this function we utilized “try-except” block for structured error handling. The function first trys to open the file. If the file opens successful with byte stream formatted data it will be read. If the file opened is empty Python would throw an “end of file” error however if this happens we simply assign our list of rows to an empty string and move on. The last option is if there is no file in the location, we simply add a file with our file name to the local folder and set the list to an empty list.  
<br/>
<br/>
```
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

    file.close()
    return list_of_rows
```
#### *Figure 1.3: Processor function 1- read data from file*  
<br/>

The second function “add_data_to_list” allows the user to add data to the list that was generated from reading the original text file. This function has three parameters task, priority, and “list_of_rows”. In the main script arguments as passed into this function when it is called. Thus, once inside the function we had to add code that converted the two pieces of string data, task and priority, and put them into a dictionary. This dictionary was then appended the list of dictionaries which we used to track our to do list. Lastly this function returns “table_list” which is, as mentioned above a list of all of the rows of dictionaries which contain our to do items. Next the “remove_data_from_list” is used to remove a to do item from our list. 

<br/>
<br/>  

```
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
```
#### *Figure 1.4: Processor function 2- add data to list*  
<br/>

This function was a little more difficult to write and took some trial and error to flush it out. The function contains a while loop set to True, thus continuously running until a break point is reached.  Inside the while loop is a for loop which iterates through each row of data in the list of dictionaries looking for a task title that matches the users inputted task they wished to remove.

<br/>
<br/>  

```
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
```
#### *Figure 1.5: Processor function 3- remove data from list*  
<br/>

If there is a match the entire row will be removed from the list of dictionaries. There was also a tracker added to this function that prints out “row not found” if the users inputted task does not match any of the tasks currently in the list. If the user does input a valid task to be removed from the list, there is a print statement that will confirm with them that the item has been removed from the list. After each one of these paths, a valid input or an invalid input there is a break statement that causes the user to break out of the while loop. Lastly before the function closes the list of dictionaries is returned. The last function in the Processor class is the “write_data_to_file” which writes each component of the table to the text file. This function was fairly easy to write because we utilized the core components in our last assignment.

<br/>
<br/>  

```
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

```
#### *Figure 1.6: Processor function 4- write data to file*  

<br/>

Next Figure 1.7 shows the first function contained in the input/output section. The “output_menu_tasks” simply outputs the menu, the “input_menu_choice” asks the user which menu item they want and returns that response and the “output_current_tasks_in_list” simply prints the current items that are contained in each dictionary that is in the list of dictionaries. 


<br/>
<br/>

```
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
```
#### *Figure 1.7: Input/Output function 1- output menu items*  

<br/>

This portion on the program was re-used from assignment 06 and thus has no significance in relation to assignment 07.

<br/>
<br/>

```
def input_menu_choice():
    """ Gets the menu choice from a user

    :return: string
    """
    choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
    print()  # Add an extra line for looks
    return choice
```
#### *Figure 1.8: Input/Output function 2- input menu choice*  

<br/>

The input menu choice prompts the user to select a menu choice and then returns that choice. This portion on the program was also re-used from assignment 06 and thus has no significance in relation to assignment 07.


<br/>
<br/>

```
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
```
#### *Figure 1.9: Input/Output function 3- output current items in list*  

<br/>

The output current item’s function outputs the current items in the list. Minor verbiage edits were made however the majority of this function was re-used from assignment 06 and thus has no significance in relation to assignment 07.

<br/>
<br/>

```
def input_new_Item_and_Cost():
    """  Gets Item and Cost values to be added to the list

    :return: (string, string) with Item and Cost
    """
    str_Item = str(input("What is the item? - ")).strip()
    str_Cost = str(input("What is the cost? [dollars] - ")).strip()
    return str_Item, str_Cost
```
#### *Figure 1.10: Input/Output function 4- input new item and cost*  

<br/>

The input new item and cost function prompts the user to input and new item and its cost, then returns two string variables. Minor verbiage edits were made however the majority of this function was re-used from assignment 06 and thus has no significance in relation to assignment 07.

<br/>
<br/>

```
def input_Item_to_remove():
    """  Gets the Item name to be removed from the list

    :return: (string) with Item
    """
    str_Item = str(input("What Item would you like to remove? - ")).strip()

    return str_Item
```
#### *Figure 1.11: Input/Output function 5- input item to remove*  

<br/>

The input item to remove function prompts the user to input an item they would like to remove, then returns that item. This function was re-used from assignment 06 and thus has no significance in relation to assignment 07.

<br/>


The last section of code was the main body of the script and it was the first thing ran upon running this python script. It has four “Steps”, the first step and the very first thing the program does when it is ran is runs the “read_data_from_file” function and passes two arguments, “pickle_file_name”, and “table_lst.” As explained above this function reads each item from our byte file and inputs each task and its priority as a dictionary, saving all of the dictionaries into a list.  

<br/>
<br/>

```
# Main Body of Script  ------------------------------------------------------ #

table_lst = read_data_from_file( file_name=pickle_file_name, list_of_rows=table_lst)  # read file data
print("read file")
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
        #table_lst =
        write_data_to_file(file_name=pickle_file_name, list_of_rows=table_lst)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop

```
#### *Figure 1.12: Main body of script*  

<br/>

Step two of the main script is a while loop which contains step 3 and 4 and is always set to True. Step 3 runs the “output_current_Items_in_list” function which passes in the argument of “table_lst” and outputs all of the tasks and their priorities so the user can see them. The next line calls the “output_menu_Items” function which prints the menu options for the user. The last function call for the function “input_menu_choice” function receives the input on their menu selection and assigns the response to the “choice_str” variable. The last step in the main portion of the script is step 4 which is a series of if, elif, and a final else statement which run various functions dependents on the users input.  

<br/>
<br/>

```
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
print("read file")
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
```
#### *Figure 1.13: Final Script*  

<br/>


## Testing the Program

After the final edition of the script was written (Figure 1.9), it had to be tested in both PyCharm as well as the OS command prompt to ensure the output was nearly identical to what the assignment asked for, which indeed it was (Figure 2.1 - Figure 2.6 and Appendix A).


# Title
## Introduction
## Topic 1
### Subtopic
## Summary


**Dev:** *RRoot*  
**Date:** *1.1.2030*


```
# ------------------------------------------------- #
# Title: Listing 13
# Description: A try-catch with manually raised errors
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

try:
    new_file_name = input("Enter the name of the file you want to make: ")
    if new_file_name.isnumeric():
        raise Exception('Do not use numbers for the file\'s name')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')    
```
#### Figure 1.1: Title Block

![rocket picture](https://github.com/ClassProfile10/Mod07/blob/main/pictures/artemis%20rocket.jpg "Artemis Picture")

![Relative path rocket picture](/pictures/artemis%20rocket.jpg "Artemis Picture")

![Relative path rocket picture](https://classprofile10.github.io/Mod07/artemis%20rocket.jpg "Artemis Picture")


![Relative path rocket picture](https://docs.github.com/assets/cb-12181/images/help/writing/quoted-text-rendered.png "Penguin")
