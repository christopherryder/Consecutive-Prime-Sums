# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:37:16 2022

@author: Christopher
"""

import math
from dataclasses import dataclass

#POD type of structure to refactor the need for two lists in the generator function.
@dataclass
class Prime_Candidate:
    value : int
    is_prime : bool

#A quick hand-rolled 'sieve of Eratosthenes`.
def generate_primes_up_to_n(n):
    
    prime_candidates = [Prime_Candidate(i, True) for i in range(n)]
    
    #We define this generator for two reasons:
    #   1. Convenience. if the prime_candidates list includes 0 and 1, then the Prime_Candidate objects' value is also it's index. 
    #   2. Because we attempt to decompose the object as (i^2 + j*i) where j = 0, ... , n then we need only consider candidates whose value is
    #   less than sqrt(n).
    #   3. We do not consider 0 or 1 to be prime numbers.
    candidate_generator = (candidate for candidate in prime_candidates if candidate.value >= 2 and candidate.value < int(math.sqrt(n)))
    
    for candidate in candidate_generator:
        #For each candidate we have assumed that it is prime. We now need to test this assertion.
        #So, we iterate all of the 'assumed-True' candidates whose value is less than int(root(n)) (this is because of how we decompose the candidate values)
        if candidate.is_prime and candidate.value < int(math.sqrt(n)):
            
            #We now wish to decompose the candidate value in such a way as to determine whether it is prime or not.
            candidate_decomposition = 0
            
            for i in range(n):
                
                #This decomposition represents a non-prime number. We can mark it's corresponding value in the candidates list as non-prime.
                #(As long as the decomposition is present in the list.)
                candidate_decomposition = (candidate.value**2) + (candidate.value * i)
                
                if candidate_decomposition < n:
                    prime_candidates[candidate_decomposition].is_prime = False
                else:
                    #These values are not prime but extend beyond our range, hence we stop processing. 
                    break
        
    #return all values marked as prime, and whose value is >= 2.
    return [prime.value for prime in prime_candidates if prime.is_prime and prime.value >= 2]
    
def is_prime(x):
    
    #If a number is less than 2 it is not prime.
    if(x < 2):
        return False
    
    #If a number is divisble by another number that is not 1 or itself then it is not prime.
    for i in range(2, int(x / 2)):
        if(x % i == 0):
            return False
    
    #Therefore, any number which has gotten to this stage must be prime.
    return True

def longest_consecutive_sum(sum_upper_bound):
    primes = generate_primes_up_to_n(sum_upper_bound)
    
    maximum_cumulative_sum = 0
    maximum_cumulative_length = 0
    
    for i in range(len(primes)):
        cumulative_sum = 0
        cumulative_length = 0
        sum_index = i
        
        while(cumulative_sum < sum_upper_bound and sum_index < len(primes)):
            
            if(cumulative_length > maximum_cumulative_length and is_prime(cumulative_sum)):
                maximum_cumulative_length = cumulative_length
                maximum_cumulative_sum = cumulative_sum
            
            cumulative_sum += primes[sum_index]
            cumulative_length += 1
            sum_index += 1
            
    return maximum_cumulative_length, maximum_cumulative_sum
            
def main():
    largest_prime = 100000
    print("The longest sum of consecutive primes below %d that adds to a prime, contains %d terms, and is equal to %d." %(largest_prime, *longest_consecutive_sum(largest_prime)))
    
if __name__ == '__main__':
    main()