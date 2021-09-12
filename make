#!/bin/bash

cd $1

mkdir -p $2 2>/dev/null
cd $2

code A.py B.py C.py D.py

cd ../../