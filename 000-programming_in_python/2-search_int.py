def find_first_occurrence(my_list, num):
    for index, value in enumerate(my_list):
        if value == num:
            return index
    return -1  # Return -1 if the number is not found

if __name__ == "__main__":
    my_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    num = int(input("Enter the number to find: "))
    print("First occurrence of the number:", find_first_occurrence(my_list, num))