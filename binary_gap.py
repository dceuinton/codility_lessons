#!/usr/bin/env python3 

# My solution to the codility challange of finding the binary gap in a number 

def solution(N):
    
    count = 0
    nOnes = 0
    currentMax = 0
    
    for i in range(32):
        if (N >> i & 1): # If it's a 1
            nOnes += 1
            
            if nOnes > 1 and count > currentMax: 
                currentMax = count
            count = 0
        
        else:            # If it's a 0
            if nOnes >= 1: 
                count += 1

    return currentMax

def run_solution(N):
	print("Num:", N, "binary:", bin(N))
	print(solution(N))



run_solution(1)
run_solution(4)
run_solution(5)
run_solution(15)
run_solution(1041)
# run_solution(31)
# run_solution(33)
# run_solution(49)
# run_solution(61)
# run_solution(257)
# run_solution(244)