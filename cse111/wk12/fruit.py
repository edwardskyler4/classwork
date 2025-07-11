def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")
    fruit_list.append("orange")
    print(f"step 4: {fruit_list}")
    apple_locale = fruit_list.index("apple")
    fruit_list.insert(apple_locale, "cherry")
    print(f"step 5: {fruit_list}")
    fruit_list.remove("banana")
    print(f"step 6: {fruit_list}")
    popped = fruit_list.pop()
    print(f"step 7: popped: {popped}, list: {fruit_list}")
    fruit_list.sort()
    print(f"sorted: {fruit_list}")
    fruit_list.clear()
    print(f"cleared: {fruit_list}")

if __name__ == "__main__":
    main()