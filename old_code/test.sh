#!/bin/bash
if [ "$#" -ne 1 ]; then
	FILES=./Files/*
    for path in $FILES
    do
        if [ -f "${path}" ]; then
            f=${path##*/}
            filename="${f%.*}"
            time python3 buffer_splitter_insertation.py ./Files/$filename.v ./OUT/"$filename"_jinkela.v
        fi
    done
else
	time python3 buffer_splitter_insertation.py -i testcase_iscas85/$1.v -o test_output/"$1"_jinkela.v
fi