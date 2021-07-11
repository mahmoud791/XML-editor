from stack import*

def validate(s):

    mystack = Stack()

    s = s.replace('\\', '/')
    path = str(s)

    file = open(path, "r")

    sum = 0
    line_No = 0

    for line in file:
        for i in range(len(line)):
            if (line[i]=='<'):
                if(line[i+1] != '!' or line[i+1] != '?'):
                    j = i+1
                    tag = ''
                    while(line[j] != ' '):
                        tag += line[j]
                        j = j+1

                    mystack.push(tag)
                    




            

    
    file.close()
            



