from formate import*

def reduce(s):
    formate(s)
    file = open("formatted.txt", "r")

    try:
        minified_file = open("Minified.txt", "x")
    except FileExistsError:
        return

    for line in file:
        for i in range(len(line)):
            if(line[i] == ' ' or line[i]=='\n'):continue
            minified_file.write(line[i])


    