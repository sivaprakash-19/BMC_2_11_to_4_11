



def helper(maze, i, j, visited) :
    if i < 0 or i == len(maze) or j < 0 or j == len(maze[0]) or maze[i][j] == 0 or visited[i][j] :
        return False 
    if i == len(maze) - 1 and j == len(maze[0]) - 1 :
        return True
    visited[i][j] = True
    if helper(maze, i - 1, j, visited) or helper(maze, i, j + 1, visited) or helper(maze, i + 1, j, visited) or helper(maze, i, j - 1, visited) :
        return True 
    return False 

def solveMaze(maze, m, n) :
    visited = [[False] * n for _ in range(m)] 
    return helper(maze, 0, 0, visited)

maze = [
    [1,1,0],
    [0,0,1],
    [0,0,1]
]
print('Is path exist -> ', solveMaze(maze, 3, 3))





'''
# Tower of hanoi
def tower(disks, source, helper, destination):
    if disks == 1 :
        print(source , ' ', destination)
        return 
    tower(disks - 1, source, destination, helper) 
    print(source , ' ', destination)
    tower(disks - 1, helper, source, destination)

disks = int(input('Enter no of disks : ')) 
tower(disks, 's', 'h', 'd')
'''


'''
from collections import deque

def buildGraph() :
    n = int(input('Enter no of vertices : '))
    edges = int(input('Enter no of edges : '))
    adjMatrix = [[0] * n for _ in range(n)]
    for _ in range(edges) :
        print('Enter the vertices at edge ' , _ )
        v1 = int(input('Enter v1 : '))
        v2 = int(input('Enter v2 : '))
        adjMatrix[v1][v2] = 1 
        adjMatrix[v2][v1] = 1 
    return adjMatrix 

def dfsTraversal(adjMatrix, currentVertex, visited) :
    print(currentVertex , end = ' ')
    visited[currentVertex] = True
    for i in range(len(adjMatrix)) :
        if adjMatrix[currentVertex][i] == 1 and visited[i] == False :
            dfsTraversal(adjMatrix, i, visited) 

def bfTraversal(adjMatrix) :
    visited = [False] * len(adjMatrix)
    pendingVertices = deque() 
    for vertex in range(len(adjMatrix)) :
        if not visited[vertex] :
            pendingVertices.append(vertex) 
            visited[vertex] = True
            while pendingVertices :
                v1 = pendingVertices.popleft()
                print(v1 , end = ' ')
                for i in range(len(adjMatrix)) :
                    if adjMatrix[v1][i] == 1 and not visited[i] :
                        pendingVertices.append(i) 
                        visited[i] = True

def path(adjMatrix, visited, start, destination) : 
    if start == destination :
        res = [start]
        visited[start] = True  
        return res 
    visited[start] = True
    for i in range(len(adjMatrix)) :
        if adjMatrix[start][i] == 1 and not visited[i] :
            ans = path(adjMatrix, visited, i, destination)
            if ans :
                ans.append(start)
                return ans
    return None

adjMatrix = buildGraph()
print('--------')
for row in adjMatrix :
    for col in row :
        print(col , end = ' ')
    print()
print('--------')

visited = [False] * len(adjMatrix)
ans = path(adjMatrix, visited, 0, 3)
print('Path btw 0 and 3 -> ', ans[::-1])

# bfTraversal(adjMatrix)

# visited = [False] * len(adjMatrix)
# for i in range(len(adjMatrix)) :
#     if not visited[i] :
#         dfsTraversal(adjMatrix, i, visited) 
#         print()
'''