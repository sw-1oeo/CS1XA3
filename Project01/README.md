Feature 5.1: script input

Once the script is executed, it first shows options of features.
As the user input their option of number, this input is stored to variable named jin.
If statements are used here, so, for example, if the user inputted 1, variable jin is matched with 1, so by the if statement, it will work on the feature 5.2 which is to create a TODO log using grep.   

Custom feature 1(option 2): 
It tries to compile every python file in the repo using for loop and with the command “python -m py_compile”, and it redirect the standard error to python_error.log.
Therefore, you can view all the error message in the “python_error.log” 
 
Custom feature 2(option 3):
Using sed command, this feature changes all the uppercase to lowercase in any text file that are in the repo. The result of this is redirected(with >, which also means 1>) to “lowercase_txt.log” here. You can view all the text file contents with lowercases here.

Custom feature 3(option 6):
It tries to compile every Haskell file in the repo using for loop and with the command “runhaskell”, and it redirect the standard error to haskell_error.log.
Therefore, you can view all the error message in the “haskell_error.log”
