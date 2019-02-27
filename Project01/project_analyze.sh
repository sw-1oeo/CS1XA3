#!/bin/bash

printf "select your feature:\n1:Create a TODO Log\n2:Custom Feature-error log for python files\n3:Custom Feature-change upper to lowercase in all txt files\n4:file type count\n5:delete temporary files\n"
printf "your option(pick the number):"
read jin 
if [ $jin = "1" ];then
	grep --exclude=todo.log -r '#TODO' . > todo.log
fi
if [ $jin = "2" ];then
	python -m py_compile *.py 2> python_error.log
fi
if [ $jin = "3" ];then
        sed 'y/ABCDEFGHIJKLMNOPQRSTUVWXYZ/abcdefghijklmnopqrstuvwxyz/' *.txt > lowercase_txt.log
fi
if [ $jin = "4" ];then
        count=$(find . -type f -name '*.html' -o -name '*.htm' | wc -l)
	echo "HTML:$count"

	count=$(find . -type f -name '*.js' | wc -l)
	echo "Javascript:$count"

	count=$(find . -type f -name '*.css' | wc -l)
	echo "CSS:$count"

	count=$(find . -type f -name '*.py' | wc -l)
	echo "Python:$count"

	count=$(find . -type f -name '*.hs' -o -name '*.lhs' | wc -l)
	echo "Haskell:$count"

	count=$(find . -type f -name '*.sh' | wc -l)
	echo "Bashscript:$count" 
fi
if [ $jin = "5" ];then
        echo git ls-files --others --exclude-standard | grep -E .tmp | xargs rm 
fi




