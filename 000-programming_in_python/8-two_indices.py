def two_indices(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index

if __name__ == "__main__":
    nums = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    target = int(input("Enter the target number: "))
    print("Indices of the numbers that add up to target:", two_indices(nums, target))