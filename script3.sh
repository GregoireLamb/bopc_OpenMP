#!/bin/bash
	
for p in {1 2 4 8 16 24 32}; do
	for i in {1..3}; do
		{ time -p ./bin/filter_runner -i ./contrib/input1.png -p $p -r 1;}
	done 
done
