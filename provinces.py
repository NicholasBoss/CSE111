

def main():
    print(read_list("provinces.txt"))
    read_list("provinces.txt")
    

def read_list(filename):
    text_list = []
    name_count = 0
    with open("provinces.txt", "rt") as text_file:

        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)

    text_list.pop(0)

    
    text_list.pop()

    print()

    for index, item in enumerate(text_list):
        if item == "AB":
            text_list[index] = "Alberta"

    for item in text_list:
        if item == "Alberta":
            name_count += 1
    print(f"Alberta occurs {name_count} times in the modified list.")
    return text_list


if __name__ == "__main__":
    main()