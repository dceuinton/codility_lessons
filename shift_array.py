#!/usr/bin/env python3 

def cyclic_rotate_array(arr, N):
	
	if len(arr) is 0:
		return []

	length = len(arr)
	shift = length - (N % length)

	second_arr = arr[shift:]

	for i in range(shift):
		second_arr.append(arr[i])

	return second_arr