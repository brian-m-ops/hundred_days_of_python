# Write your code below this line 👇
def prime_checker(number):

    isPrime = True

    for i in range(2, number):

        if number % i == 0:
            isPrime = False

    if isPrime == True:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


# Write your code above this line 👆

# Example test 73 = It's a prime number
# Example test 75 = It's not a prime number.

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
