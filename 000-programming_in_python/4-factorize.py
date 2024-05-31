def factorize(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors

if __name__ == "__main__":
    number = int(input("Enter a number to factorize: "))
    print("Prime factors of the number:", factorize(number))