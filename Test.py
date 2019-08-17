stop = False
print('Enter "e" to exit')
while stop == False:
    print("Enter the size of the Field!")
    length = input("> ")
    if length == "e" or length == "exit" or length == "quit" or length == "stop":
        print("")
        print("Bye Bye!")
        stop = True
    else:
        row = []
        for i in range(int(length)):
            row.append([])
        counter = 0

        def printer():
            for p in range(int(length)):
                for q in range(int(length)):
                    print(row[p][q], end=" ")
                print("")
            print("")


        for i in range(int(length)):
            if i % 2 == 0:
                for y in range(int(length)):
                    if y % 2 == 0:
                        row[counter].append("+")
                    else:
                        row[counter].append("-")
            else:
                for u in range(int(length)):
                    if u % 2 == 0:
                        row[counter].append("-")
                    else:
                        row[counter].append("+")
            counter = counter + 1

        printer()

        rechts = input("X - Achse > ")
        if rechts == "e" or rechts == "exit" or rechts == "quit" or rechts == "stop":
            print("")
            print("Bye Bye!")
            stop = True
            break
        else:
            rechts2 = int(rechts) - 1

        unten = input("Y - Achse> ")
        if unten == "e" or unten == "exit" or unten == "quit" or unten == "stop":
            print("")
            print("Bye Bye!")
            stop = True
            break
        else:
            unten2 = int(unten) - 1
        print("")

        row[unten2][rechts2] = "X"
        printer()