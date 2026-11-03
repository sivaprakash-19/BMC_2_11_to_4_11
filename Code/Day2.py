





def buildGraph() :
    n = int(input('Enter no of vertices : '))
    edges = int(input('Enter no of edges : '))
    adjMatrix = [[0] * n for _ in range(n)]
    for _ in range(edges) :
        v1 = int(input('Enter v1 : '))
        v2 = int(input('Enter v2 : '))
        adjMatrix[v1][v2] = 1 
        adjMatrix[v2][v1] = 1 
    return adjMatrix 

adjMatrix = buildGraph()
for row in adjMatrix :
    for col in row :
        print(col , end = ' ')
    print()


'''
from collections import deque

class TreeNode :
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 

def createTree(msg, rootData) :
    if rootData == -1 :
        print(msg, end = ' ')
    else :
        print(msg, '', rootData, ':', end = ' ') 
    data = int(input())
    if data == -1 :
        return None 
    root = TreeNode(data)
    root.left = createTree('Enter left of ', data)
    root.right = createTree('Enter right of ', data)
    return root 

def levelOrder(root) :
    if root is None :
        return 
    pendingNodes = deque()
    pendingNodes.append(root) 
    while pendingNodes :
        size = len(pendingNodes) 
        for x in range(size) :
            current = pendingNodes.popleft() 
            print(current.data , end = ' ') 
            if current.left : 
                pendingNodes.append(current.left)
            if current.right :
                pendingNodes.append(current.right) 
        print()
root = createTree('Enter root data : ', -1) 
levelOrder(root)
'''