def saveToFile():
    lst = []
    try:
        read_lines = open('exer5.txt', 'r')
        for words in read_lines:
            lst.append(words[:-1])
    except Exception as err:
        print(err)
    finally:
        read_lines.close()
    input_one = input("Enter String 1: ")
    input_two = input("Enter String 2: ")
    input_three = input("Enter String 3: ")

    lst.append(input_one)
    lst.append(input_two)
    lst.append(input_three)
    lst.sort()

    try:
        file = open('exer5.txt', 'w')
        for words in lst:
            file.write(words + "\n")
    except Exception as err:
        print(err)
    finally:
        file.close()


saveToFile()