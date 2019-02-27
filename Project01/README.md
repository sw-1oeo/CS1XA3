Feature 5.1: script input

Once the script is executed, it first shows options of features.
As the user input their option of number, this input is stored to variable named jin.
If statements are used here, so, for example, if the user inputted 1, variable jin is matched with 1, so by the if statement, it will work on the feature 5.2 which is to create a TODO log using grep.   

Feature 5.4 create TODO log (option 1)
The command grep recursively find line that has #TODO in every file in your repo. The standard output that used to appear on your console is redirected to todo.log file. There fore those lines containing #TODO should all be seen from todo.log now. Just in case, if you are executing this option more than one time, since after executing it, todo.log will be made in your repo with all the #TODO lines, thinking that you would want to ignore this one so that you can use it just life first time you try, I exclude todo.log file when prepping #TODO. 

Custom feature 1(option 2): 
It tries to compile every python file in the repo using for loop and with the command “python -m py_compile”, and it redirect the standard error to python_error.log.
Therefore, you can view all the error message in the “python_error.log” 
 
Custom feature 2(option 3):
Using sed command, this feature changes all the uppercase to lowercase in any text file that are in the repo. The result of this is redirected(with >, which also means 1>) to “lowercase_txt.log” here. You can view all the text file contents with lowercases here.

Feature 5.5 File type count (option 4)
Firstly, using find command you find .html file or .htm file in your current directory and pipe the standard output to count number of the lines which means number of the files. This information is restored as the variable with $ sign in the count variable.  You echo the variable with after HTML: so that it will give out number of html files like HTML: 3 (if there are 3 html files in the repo). Same format for all the other languages. For Haskell, there were two options for its extensions. So “-o” were used just like html so that both .hs and .lhs could be counted.

Feature 5.6 Delete temporary file (option 5) 
This feature removes all the .tmp extensions files that are untracked in the repo. First, “echo git ls-files --others --exclude-standard” gives list of untracked file in the repo, this standard output is piped into grep using -E flag which extends regular expression, and grep all the .tmp file from the input. This standard output is again piped into rm command with xargs which makes standard output of grep to argument for the rm command. 

Custom feature 3(option 6):
It tries to compile every Haskell file in the repo using for loop and with the command “runhaskell”, and it redirect the standard error to haskell_error.log.
Therefore, you can view all the error message in the “haskell_error.log”


Feature 5.3 Compile error log (option 7)
Using the for loop with the command “do python -m py_compile” that compile all the python file, the command is affecting every python file in the repo(with the .py extension) until it is all done. The standard error will then be appear on your console usually but it is now, with “2>>”, redirected to compile_fail.log. Here, 2>> is used instead of 1>> (>>) since it is dealing with standard error, and >> is used instead of >, because you want the information to be all piled up in the log file. Then using cat you can see the content of the file, and the standard output will be piped into grep with pattern ‘File’ recursively. (I chose ‘File’ as the pattern to find file name because file name always appeared in the line where ‘File’ was stated). Then redirected the result to compile_fail.log. 
Same with python, runhaskell is the command that compile Haskell file. Using for loops, you compile all the Haskell file in the repo, redirects the error output to error_haskell.log, see the content of the file with cat command, then grep line with ‘error:’ (in Haskell case, file name appeared in the line where ‘error:’ appeared), then redirect in the compile_fail.log. Therefore, you get all the line with file names from python and Haskell that had error when compiled. 
