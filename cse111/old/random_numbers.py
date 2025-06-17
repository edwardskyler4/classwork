import random

def main():
    numbers = [16.2, 75.1, 52.3]
    words = ["Bread", "Formula", "Sauce"]
    print(numbers)
    print()

    append_random_numbers(numbers)
    print(numbers)
    print()
    
    append_random_numbers(numbers, 3)
    print(numbers)
    print()

    print(words)
    print()

    append_random_words(words)
    print(words)
    print()

    append_random_words(words, 3)
    print(words)
    print()


def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        number = random.uniform(10, 100)
        num_rounded = round(number, 1)
        numbers_list.append(num_rounded)

def append_random_words(words_list, quantity=1):
    words_to_add = ["cat", "house", "sun", "book", "tree", "river", "shoe", "cloud", "song", "food"]
    for _ in range(quantity):
        word = random.choice(words_to_add)
        while word in words_list:
            word = random.choice(words_to_add)
        words_list.append(word.capitalize())

if __name__ == "__main__":
    main()