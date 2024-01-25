#!/bin/bash

weight="$1"
height="$2"
idealweight=$((height - 110))

if [ "$weight" -le $idealweight ] ; then
	echo "Eat more fat"
else
	echo "Eat less you pig!"
fi
