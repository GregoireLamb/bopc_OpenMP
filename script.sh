#!/bin/bash

for n in 80 1200; do 
	for p in 1 2 4 8 16 24 32; do 
		for i in {1..3}; do
			{ time -p ./bin/juliap_runner -n $n -p $p ;}

		done 
	done
done
