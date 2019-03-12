#!/usr/bin/env python3 

# My solution to the codility challange of finding the binary gap in a number 

def solution(N):
	check = 2**31 -1
	if N < 1 or N > check:
		return -1

	count = 0
	num1s = 0
	current_max = 0
	for i in range(32):
		if ((N >> i) & 1):
			num1s += 1
			if num1s % 2 is 0:
				if count > current_max:
					current_max = count
				count = 0
		elif num1s % 2 is 1:
			count += 1

	if num1s > 1: 
		return current_max
	else:
		return 0

def run_solution(N):
	print("Num:", N, "binary:", bin(N))
	print(solution(N))



run_solution(1)
run_solution(4)
run_solution(5)
run_solution(31)
run_solution(33)
run_solution(49)
run_solution(61)
run_solution(257)
run_solution(244)