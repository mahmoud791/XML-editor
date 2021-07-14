
from tree import*
from formate import*



def convert(s):

    formate(s)
    file = open("formatted.txt", "r")

    line_No = 0
    current_node = Node(parent=None,xmltag=None)

    for line in file:

        if(line_No == 0):
            line_No +=1
            continue
        for i in range(len(line)-1):
            
            if(line[i] == '<'):
                if(line[i+1] == '/'):
                    current_node = current_node.parent
                    break
                
                
                new_node = Node(parent=current_node,xmltag=None)
                current_node.children.append(new_node)
                current_node = new_node
                j = i+1


                tagAndattributes = ''
                while(line[j] != '>'):
                    tagAndattributes += line[j]
                    j +=1
                
                tagAndattributes = tagAndattributes.split()
                for i in range(len(tagAndattributes)-1):
                    if(i==0):
                        new_node.xmltag = tagAndattributes[0]
                    else:
                        new_node.attributes.append(tagAndattributes[i])
                
                break
            
            

            elif(line[i] != ' '):
                current_node.text += line[i]

            




        if (line_No == 1):
            head = current_node
        line_No += 1

    test(head)

        


def test (root):
    if(root.children == None):return
    print(root.xmltag)
    print(root.text)
    for child in root.children:
        test(child)







                


            