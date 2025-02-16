

def count_words(text):
    words = text.split()  # Split the text into words
    return len(words)     # Return the number of words

def main():
    while True:
        user_input = input("Enter a sentence or paragraph: ").strip()
        if not user_input:
            print("Error: Input cannot be empty. Please enter a sentence or paragraph.")
        else:
            word_count = count_words(user_input)
            print(f"Number of words: {word_count}")
            break

if __name__ == "__main__":
    main()