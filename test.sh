#!/bin/bash
if [ "$#" -ne 1 ]; then
	FILES=testcase_iscas85/*
    for path in $FILES
    do
        if [ -f "${path}" ]; then
            f=${path##*/}
            filename="${f%.*}"
            time python3 src/main.py -i testcase_iscas85/$filename.v -o test_output/"$filename"_jinkela.v
        fi
    done
else
	time python3 src/main.py -i testcase_iscas85/$1.v -o test_output/"$1"_jinkela.v
fi