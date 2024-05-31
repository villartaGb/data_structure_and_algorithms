def character_frequency(string):
    frequency = {}
    for char in string.lower():
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

if __name__ == "__main__":
    string = input("Enter a string: ")
    print("Character frequency:", character_frequency(string))