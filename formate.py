def formate(s):
    s = s.replace('\\', '/')
    path = str(s)

    file = open(path, "r")
    current_spaces = 0

    for line in file:
        for i in range(len(line)-1):
            if(line[i] == "<"):
                if(line[i+1] != "/"):
                    
