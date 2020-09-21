#!/bin/bash
FILES=testcase_iscas85/*
for path in $FILES
do
    f=${path##*/}
    filename="${f%.*}"
    python3 src/main.py -i testcase_iscas85/$filename.v -o test_output/"$filename"_jinkela.v
done