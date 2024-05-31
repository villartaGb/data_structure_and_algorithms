def get_smallest_integer(my_list):
    return min(my_list)

if __name__ == "__main__":
    my_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    print("Smallest integer in the list:", get_smallest_integer(my_list))