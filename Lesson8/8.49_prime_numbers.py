# ####2DO
# Your goal in this task is to create two functions:
#
# 1. list_primes
# Function that will list all the prime numbers up to the specified limit, e.g. list_primes(10) will list all the prime numbers from 0 to 10 including. The function should return a set or a list of prime numbers found.
#
# Example of using list_primes() function:
#
# >>> list_primes(54)
# {11, 13, 17, 19, 2, 23, 29, 3, 31, 37, 41, 43, 47, 5, 53, 7}
# 2. is_prime
# Function that will tell, whether a number is prime. It will take one argument of type int and return a boolean value.
#
# Example of using is_prime() function:
#
# >>> is_prime(54)
# False
# >>> is_prime(53)
# True
# Algorithm to list prime numbers
# To generate a list of prime numbers, you will probably want to follow algorithm designed by Eratosthenes:
#
# Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
#
# Initially, let p equal 2, the smallest prime number.
#
# Enumerate the multiples of p (prime number) by counting from 2p (prime number multiplied by 2) to n (limit) in increments of p, and erase them from the list of generated numbers (these will be 2p, 3p, 4p, ...; the p itself should not be erased).
#
# Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
#
# When the algorithm terminates, the numbers remaining not erased in the list are all the primes below n.
# #######


def list_primes(end):
    _list = list(range(2, end + 1)) #list of all numbers in the range except 0,1
    index = 0
    while _list[index]:
        prime = _list[index]
        to_remove = prime
        while to_remove <= end:
            to_remove += prime  #will remove multiplies from prime numbers
            if to_remove in _list: #check if exist in the list to avoid error
                _list.remove(to_remove)
        index += 1
        if index >= len(_list): #prevent to be out of list range
            break
    return _list


def is_prime(end_Nr):
    return end_Nr in list_primes(end_Nr)

#print(list_primes(53))
print(is_prime(53))

# #Engeto solution
# #Comments: result of the 1st function is set -disadv unordered
# #result of the function is built new, total list number is being reduced - no need to use indexing
# def list_primes(n):
#
#     nums = list(range(2,n+1))
#     result = set()
#
#     while nums:
#         i = nums.pop(0)
#         result.add(i)
#         for num in nums:
#             if num % i==0:
#                 nums.remove(num)
#     return result
#
# def is_prime(n):
#     return n in list_primes(n)
#
# print(is_prime(23))
# ################