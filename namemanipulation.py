def main():
    # Get the user's name
    name = input("Hey there! What's your name? ")

    # Show the name as entered
    print(f"Here’s the name you entered: {name}")

    # Ask how many characters they want to see from the beginning
    n = int(input("How many characters from the start do you want to see? "))
    if n > len(name):
        print("Oops! You asked for more characters than the length of your name. Showing the whole name instead.")
        n = len(name)
    print(f"Here are the first {n} characters: {name[:n]}")

    # Count how many vowels are in the name
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in name if char in vowels)
    print(f"Your name has {vowel_count} vowels in it!")

    # Reverse the name
    reversed_name = name[::-1]
    print(f"And here's your name backwards: {reversed_name}")

# Run the program
if __name__ == "__main__":
    main()
