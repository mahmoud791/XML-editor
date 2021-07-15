class Node:
    def __init__(self,count):
        self.left = None
        self.right = None
        self.parent = None
        self.count = count
    def isLeft(self):
        return self.parent.left == self


def createNodes(counts):
    return [Node(count) for count in counts]


def HTree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item:item.count)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_parent = Node(node_left.count + node_right.count)
        node_parent.left = node_left
        node_parent.right = node_right
        node_left.parent = node_parent
        node_right.parent = node_parent
        queue.append(node_parent)
    queue[0].parent = None
    return queue[0]



def Encoding(nodes,root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.parent
    return codes
        


def getHuffmanCode(s):
    Encoded_file = open('Encoded_file.txt','x')   
    dict1 ={}
    s = s.replace('\\', '/')
    path = str(s)

    file = open(path, "r")

    line_No = 0

    for line in file:
        for i in line:
            if i in dict1.keys():
                dict1[i] += 1
            else :
                dict1[i] = 1 
    chars_counts  = sorted(dict1.items(), key = lambda kv:(kv[1], kv[0]))
    nodes = createNodes([item[1] for item in chars_counts])
    root = HTree(nodes)
    codes = Encoding(nodes,root)
    dict2 = {}
    for item in zip(chars_counts,codes):
        dict2[item[0][0]] = item[1]
    

    file = open(path, "r")

    for line in file:
        for i in range(len(line)):
            Encoded_file.write(dict2[line[i]])

    #print(codes)

    
    #Encoded_file.write(tag)