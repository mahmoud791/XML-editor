class Node:
    def __init__(self,freq):
        self.left = None
        self.right = None
        self.parent = None
        self.freq = freq
    def isLeft(self):
        return self.parent.left == self


def createNodes(freqs):
    return [Node(freq) for freq in freqs]


def HTree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item:item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_parent = Node(node_left.freq + node_right.freq)
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

# Unzip the huffman file
def decode_huffman(input_string,  char_store, freq_store):
    #input_string Huffman encoding
    #char_store character set 
    #freq_store Character transcoding 01 sequence
    encode = ''
    decode = ''
    for index in range(len(input_string)):
        encode = encode + input_string[index]
        for item in zip(char_store, freq_store):
            if encode == item[1]:
                decode = decode + item[0]
                encode = ''
    return decode;           


def getHuffmanCode(s):   
    dict1 ={}
    s = s.replace('\\', '/')
    path = str(s)

    file = open(path, "r")

    line_No = 0

    for line in file:
        for i in range(len(line)-1):
            if i in dict1.keys():
                dict1[i] += 1
            else :
                dict1[i] = 1 
    chars_freqs  = sorted(dict1.items(), key = lambda kv:(kv[1], kv[0]))
    nodes = createNodes([item[1] for item in chars_freqs])
    root = HTree(nodes)
    codes = Encoding(nodes,root)
    dict2 = {}
    for item in zip(chars_freqs,codes):
        dict2[item[0][0]] = item[1]
    tag = ''
    for line in file:
        for v in range (len(line)-1):
            tag += dict2[v]
        return [tag,dict2]