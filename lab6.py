#question1
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:  
        return x * factorial(x - 1)

print(factorial(5))  

#question2

import math

sine_step = lambda x, n: (((-1) ** n) * (x ** (2 * n + 1))) / factorial1(2 * n + 1)


def sine_x(x, n):
    rad = x * math.pi / 180 
    val = 0
    for i in range(n):  
        val += sine_step(rad, i)  
    return val


def factorial1(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial1(x - 1)


def main():
    
    x = float(input("Enter the angle in degrees: "))
    n = int(input("Enter the number of terms: "))
    print(f"sin({x}) ≈ {sine_x(x, n)}")


if __name__ == "__main__":
    main()

#question3

total_sum = 0

def recursive_sum(n):
    """
    This function calculates the sum of the first 'n' natural numbers
    using recursion. The result is stored in the global variable `total_sum`.
    
    Parameters:
    n (int): The number up to which the sum should be calculated.

    Returns:
    None: This function does not return any value, it modifies the global `total_sum`.
    """
    global total_sum  

    if n > 0:
        total_sum += n  
        recursive_sum(n - 1)  


n = int(input("Enter a number: "))
recursive_sum(n)
print(f"The sum of the first {n} numbers is: {total_sum}")
