#!/bin/bash

#Program to find live systems in IIC LAB

max=255
for x in `seq 0 $max`
do
	for y in `seq 0 $max `
	do
		ping -c 1 10.104.$x.$y | grep "100% packet loss"
		if [ $? -ne 0 ]
		then
			echo "10.104.$x.$y is Alive\n" >> ping.txt
		fi
	done
done
