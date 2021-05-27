import math

'''
prime number is only decompostion by 1 * self_num
it can be use all data to define prime or not 
But time o is o(n)

to speed up
use sqrt(square root) 
time o(root(n))
'''
def check_prime(number):
    sqrt_number = math.sqrt(number)
    for i in range(2, int(sqrt_number) + 1):
        if (number / i).is_integer():
            return False
    return True
print(f"check_prime(10000000) = {check_prime(10000000)}")
print(f"check_prime(10000019) = {check_prime(10000019)}")
