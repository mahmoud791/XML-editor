
from tree import*
from formate import*



def convert(s):

    formate(s)    #the file must be idented first to be able to put in a tree
    file = open("formatted.txt", "r")

    line_No = 0
    current_node = Node(parent=None,xmltag=None)

    for line in file:

        if(line_No == 0):
            line_No +=1
            continue
        for i in range(len(line)):
            
            if(line[i] == '<'):
                if(line[i+1] == '/'):
                    current_node = current_node.parent
                    break
                
                if(line_No == 1):
                    new_node = Node(parent=None,xmltag=None)
                else:
                    new_node = Node(parent=current_node,xmltag=None)
                current_node.children.append(new_node)
                current_node = new_node
                j = i+1


                tagAndattributes = ''
                while(line[j] != '>'):
                    tagAndattributes += line[j]
                    j +=1
                
                tagAndattributes = tagAndattributes.split()
                for i in range(len(tagAndattributes)):
                    if(i==0):
                        new_node.xmltag = tagAndattributes[0]
                    else:
                        new_node.attributes.append(tagAndattributes[i])
                
                break
            
            

            elif(line[i] != ' '):
                j=i
                while(j < len(line)-1):
                    current_node.text += line[j]
                    j += 1
                break

            




        if (line_No == 1):
            head = current_node
        line_No += 1

    json_file = open('json.txt','x')
    json_file.write('{\n')
    write_json(head,json_file=json_file)
    json_file.write('}')

    
        


def write_json (root,json_file):

    json_file.write('\"'+root.xmltag+'\"'+':')
    if(root.parent == None):
        json_file.write('{\n')
        write_atrr_text(root=root,json_file=json_file)
        for child in root.children:
            write_json(child,json_file=json_file)
        json_file.write('}\n')
    
    else:
        json_file.write('[\n')
        json_file.write('{\n')
        write_atrr_text(root=root,json_file=json_file)
        if not (len(root.children)):
            json_file.write('}\n],\n')
            return

        for child in root.children:
            write_json(child,json_file=json_file)

        

    


        
        

    

    #forloop for children




def write_atrr_text(root,json_file):

    if(len(root.text)):
        if(len(root.attributes)):
            json_file.write('\"'+'_'+'\":')
            json_file.write('\"'+root.text+'\",'+'\n')
        else:
            json_file.write('\"'+root.text+'\"'+'\n')


    

    if(len(root.attributes)):
        json_file.write('\"'+'$'+'\"'+':{\n')
    
        for i in range(len(root.attributes)):
            if(i>=len(root.attributes)-1):
                attr = root.attributes[i].split('=')
                json_file.write('\"'+attr[0]+'\":')
                json_file.write(attr[1]+'\n')

            else:
                attr = root.attributes[i].split('=')
                json_file.write('\"'+attr[0]+'\":')
                json_file.write(attr[1]+',\n')
            
        json_file.write('}\n')





                


            