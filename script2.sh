#!/bin/bash
 
for i in {1..3}; do
	{ time -p ./bin/juliap_runner -n 1200 -p 16 ;}
done 
