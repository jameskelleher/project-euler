# the smallest divisor of any number must be prime, otherwise there exists a smaller divisor
# therefore, find the smallest divisor of the input, and "exhaust" it as a factor from the input
# recurse on the result to see if there is a larger prime number
def largest_prime_factor(num, start_at=3):
    # print(num)

    # if the number is even, halve it and check that
    # the "if num == 2" check handles the case when the input is a power of 2
    if num == 2:
        return 2
    elif num % 2 == 0:
        return largest_prime_factor(num // 2)
    

    for i in range(start_at, num // 3 + 1, 2):
        # found a prime factor
        if num % i == 0:

            # exhaust the prime factor from the input
            while num % i == 0:
                num = num // i

            # if input is a power of i, return i
            if num == 1:
                return i

            # find the highest prime factor of the "exhausted" input
            # we set start_at to the next largest odd number, 
            # since we've already checked the smaller range
            return largest_prime_factor(num, start_at=i + 2)

    # the input is prime
    return num

if __name__  == '__main__':
    print(largest_prime_factor(600851475143))

# below is a previous implementation that ran slow
# I realized that I could speed it up by dividing by smaller prime numbers,
# since prime numbers are denser when they are smaller and therefore more likely to occur,
# and I could speed up the problem by shrinking the serach space
# note that the "faster" implementation should have the same runtime for prime numbers 
# since you have to check the entire problem space in both cases

# def lpf(num):

#     print(f'searching {num}')
#     div = num // 2
#     while div >= 2:
#         if num % div == 0:
#             return lpf(div)
#         div -= 1
#     return num

# the improved runtime is still linear, but I belive that it is O(largest_prime_factor + number_of_factors)
# that is to say, there should be an upper bound based on the inputs largest prime factor
# and the number of factors that it has