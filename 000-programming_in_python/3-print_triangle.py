def print_right_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

if __name__ == "__main__":
    height = int(input("Enter the height of the triangle: "))
    print_right_triangle(height)