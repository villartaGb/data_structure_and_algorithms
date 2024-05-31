def sum_even_numbers(my_list):
    return sum(x for x in my_list if x % 2 == 0)

if __name__ == "__main__":
    my_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    print("Sum of even numbers in the list:", sum_even_numbers(my_list))