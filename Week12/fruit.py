def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")
    fruit_list.append('orange')
    print(f"append orange: {fruit_list}")
    fruit_list.insert(1,'cherry')
    print(f"insert cherry: {fruit_list}")
    fruit_list.remove('banana')
    print(f"remove banana: {fruit_list}")
    print(f"pop: {fruit_list.pop()} {fruit_list}")
    fruit_list.sort()
    print(f"sorted: {fruit_list}")
    fruit_list.clear()
    print(f"cleared: {fruit_list}")
main()