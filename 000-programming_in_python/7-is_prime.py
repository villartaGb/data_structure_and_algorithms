def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    number = int(input("Enter a number to check if it is prime: "))
    print("Is the number prime?", is_prime(number))