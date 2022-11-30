# Title
*RRoot, 1.1.2030*

## Introduction
this is the introductioin. this is what the text would look like

## Topic 1
This is what topic 1 would look like


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
#### Listing 13

![rocket picture](https://github.com/ClassProfile10/Mod07/blob/main/pictures/artemis%20rocket.jpg "Artemis Picture")

![Relative path rocket picture](/pictures/artemis%20rocket.jpg "Artemis Picture")
