#!/bin/bash

printf "select your feature:\n1:Create a TODO Log(5.2)\n2:Custom Feature-error log for python files\n3:Custom Feature-change upper to lowercase in all txt files\n4:File type count(5.5)\n5:Delete temporary files(5.6)\n6:Custom feature-error log for haskell files\n7:Compile error log(5.3)\n"
printf "your option(pick the number):"
read jin 
if [ $jin = "1" ];then
	grep --exclude=todo.log -r '#TODO' . > todo.log
fi
if [ $jin = "2" ];then
	for i in *.py; do python -m py_compile $i; done 2> python_error.log
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
if [ $jin = "6" ];then
        for i in *.hs; do runhaskell $i; done 2> haskell_error.log
fi
if [ $jin = "7" ];then
        for i in *.py; do python -m py_compile $i; done 2>> error_python.log
	cat error_python.log | grep -r 'File' >> compile_fail.log 
	for i in *.hs; do runhaskell $i; done 2>> error_haskell.log
	cat error_haskell.log | grep -r ': error:' >> compile_fail.log
fi




