print("Enter a number!")
print('To exit enter "e"!')

while True:
    length = input("> ")
    if length == "e":
        print("Bye Bye!")
        break
    else:
        for i in range(int(length)):
            if i % 2 == 0:
                for y in range(int(length)):
                    if y % 2 == 0:
                        print("+ ", end="")
                    else:
                        print("- ", end="")
                    if y == int(length) - 1:
                        print("")
            else:
                for u in range(int(length)):
                    if u % 2 == 0:
                        print("- ", end="")
                    else:
                        print("+ ", end="")
                    if u == int(length) - 1:
                        print("")
        print("")





