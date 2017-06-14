#!/bin/bash
for (( i=30; i >= 1; i-- ))    
do
    python int_array_gen.py $i 20
done