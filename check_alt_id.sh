#!/bin/bash

for ciffile in cif/*
do
    echo $ciffile
    grep "^ATOM" $ciffile | awk '{print $5}' | sort | uniq 
done

