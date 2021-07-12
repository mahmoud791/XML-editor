from stack import*

def validate(s):

    mystack = []

    s = s.replace('\\', '/')
    path = str(s)

    file = open(path, "r")

    line_No = 0

    for line in file:
        for i in range(len(line)-1):
            if (line[i]=='<'):
                if(line[i+1] != '/' and line[i+1] != '!' and line[i+1] != '?' ):
                    j = i+1
                    tag = ''
                    while((line[j] != " " and line[j] != ">") and (j < len(line)-1)):
                        tag += line[j]
                        j = j+1

                    mystack.append(tag)

                elif(line[i+1] == '/'):
                    j = i+2
                    tag = ''
                    while(line[j] != '>'):

                        tag += line[j]
                        j = j+1
                    
                    if(mystack.pop() != tag):
                        print("error in line "+str(line_No)+" the closing tag '"+str(tag)+"' doesnt match it opening")
            
            if(line[i]=='>' and line[i-1]=='/'):
                x=mystack.pop()

        line_No = line_No + 1

    #while(len(mystack) != 0):
    #    print(mystack[-1])
    #    mystack.pop()

                    
            

    
    file.close()
            



