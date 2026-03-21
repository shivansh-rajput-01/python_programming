# in python we can write an else after loop that will do task in it if loop does not terminate with break

# why else is useful with loop

# WAP to find whether a number is prime or not

isPrime = True # say n is prime by default

n = int(input("Enter a number to check for prime: "))

if n < 2:
    print(f"{n} is not a prime number")
else:
    for i in range(2, n//2):
        if n % i == 0: # i.e. i is divisor of n that means n is not a prime number
            print(f"{n} is not a prime number")
            isPrime = False
            break

    if isPrime:
        print(f"{n} is a prime number")



# why we have written the logic like this
# just because inside the loop if a number divides n then we can print it is not prime but when loop terminates how we will know that the number is divided by iterator in any iteration or not and how we will tell if it is prime
# so for this purspose we have made a boolean variable isPrime and make it True by default means assuming n is prime
# if in loop n % i == 0 than we can make isPrime = False and print that n is not prime and break
# after loop if isPrime = True it means no number divided n in loop i.e. n is prime and if it is false then we need to do nothing



# in python we can do it in a different way
# using else with loops
# else is written just after loop and executes if loop does not terminate with break


n = int(input("Enter a number to check for prime: "))

if n < 2:
    print(f"{n} is not a prime number")
else:
    for i in range(2, n//2):
        if n % i == 0: # i.e. i is divisor of n that means n is not a prime number
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")
