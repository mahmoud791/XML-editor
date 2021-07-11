from os import write
from typing import Counter


def convert(s):
    s = s.replace('\\', '/')
    path = str(s)

    file = open(path, "r")
    flag = 0
    f = open("json.txt", "x")

    for line in file:
        for i in range(len(line)):
            if (line[i]=='<'): 
                if (line[i+1] != '/'):
                    f.write('\"')
                    j = i+1
                    while(line[j] != '>'):
                        if (line[j] == ' '):
                            flag = 1
                            break
                        f.write(line[j])
                        j+=1
                    f.write("\":")
                    f.write(" {\n")


                    if(flag == 1):
                        j+=1
                        flag =0
                        while (line[j] != '>'):
                            f.write("\"@")
                            while(line[j] != '='):
                                if(line[j] == ' '):
                                    j+=1
                                    continue
                                f.write(line[j])
                                j+=1
                            f.write("\": ")
                            j+=1
                            f.write(line[j])
                            j+=1
                            while(line[j] != '\"'):
                                f.write(line[j])
                                j+=1
                            f.write(line[j])
                            j+=1

                            f.write(',')
                            f.write('\n')
                    break
                else:
                    f.write("\n}")
                    break
            else:
                f.write('\"')
                for j in range(len(line)-1):
                    f.write(line[j])
                f.write('\"')
                break
                
            









                


            