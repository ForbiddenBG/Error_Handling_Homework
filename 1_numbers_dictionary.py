numbers_dictionary = {}

line = input()
while line != "Search":
    if line.isalpha():
        if line not in numbers_dictionary:
            numbers_dictionary[line] = ""
    elif line.isdigit():
        line = int(line)
        if line == 1:
            numbers_dictionary['one'] = 1
        elif line == 2:
            numbers_dictionary['two'] = 2
    line = input()

command = input()
while not command == "Remove":
    if command in numbers_dictionary:
        print(numbers_dictionary[command])
    command = input()

next_command = input()
while not next_command == "End":
    if next_command in numbers_dictionary:
        del numbers_dictionary[next_command]
    else:
        print("Number does not exist in dictionary")
    next_command = input()

for key, value in numbers_dictionary.items():
    if value == "":
        print("The variable number must be an integer")
        numbers_dictionary.clear()
        print(numbers_dictionary)
        break
    else:
        print(numbers_dictionary)
