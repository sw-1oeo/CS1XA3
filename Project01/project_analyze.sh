#!/bin/bash

printf "select your feature:\n1:Create a TODO Log\n2:Compile Error Log\n3:Custom Feature-change upper to lowercase in all txt files\n4:file type count\n5:delete temporary files\n"
printf "your option(pick the number):"
read jin 
if [ $jin = "1" ];then
		grep --exclude=todo.log -r '#TODO' . > todo.log
fi
if [ $jin = "2" ];then
	echo  not done yet, spared for part2
fi
if [ $jin = "3" ];then
        sed 'y/ABCDEFGHIJKLMNOPQRSTUVWXYZ/abcdefghijklmnopqrstuvwxyz/' *.txt > lowercase_txt.log
fi
if [ $jin = "4" ];then
        echo not done yet, spared for part2 
fi
if [ $jin = "5" ];then
        echo git ls-files --others --exclude-standard | grep -E .tmp | xargs rm 
fi




