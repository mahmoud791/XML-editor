
def shift_amount(numberOfSpaces):
    shift = ""
    for i in range(numberOfSpaces):
        shift += " "
    return shift








def formate(s):
    s = s.replace('\\', '/')
    path = str(s)

    file = open(path, "r")
    file = file.readlines()
    formatted_file = open("formatted.txt", "x")
    current_spaces = 0
    
    i = 0
    while(i < len(file)-1):
        
        j = 0
        while(j < len(file[i])-1):

            if(file[i][j] == '<'):
                j = j+1
                if(file[i][j] != '/' and file[i][j] != '!' and file[i][j] != '?'):
                    new_line = ""
                    while( file[i][j] != '>'):
                        if(j >= len(file[i])-2):
                            new_line += file[i][j]+file[i][j+1]
                            j = 0
                            i += 1
                        else:
                            new_line += file[i][j]
                            j +=1
                        
                    shift = shift_amount(current_spaces)
                    printed_line = shift +"<"+new_line+">"
                    formatted_file.write(printed_line)
                    formatted_file.write("\n")
                    current_spaces += 3
                
                elif (file[i][j]=='/'):
                    new_line = ""
                    while( file[i][j] != '>'):
                        if(j >= len(file[i])-2):
                            new_line += file[i][j]+file[i][j+1]
                            j = 0
                            i += 1
                        else:
                            new_line += file[i][j]
                            j +=1

                    current_spaces -= 3   
                    shift = shift_amount(current_spaces)
                    printed_line = shift +"<"+new_line+">"
                    formatted_file.write(printed_line)
                    formatted_file.write("\n")
                    

                    

            else:
                new_line = ""                                 #to write text between tags
                while(j < len(file[i])-1 and file[i][j] != '<'):
                    new_line += file[i][j]
                    j +=1
                    
                if(file[i][j] == '<'):
                    j -= 1
                
                shift = shift_amount(current_spaces)
                printed_line = shift + new_line
                formatted_file.write(printed_line)
                formatted_file.write("\n")




                    



            j = j+1
        
        i =i+1
   


