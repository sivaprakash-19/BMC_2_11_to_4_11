

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
def printTree(root) :
    if root is None :
        return 
    print(root.data, end = ' : ')
    if root.left :
        print('L',root.left.data, end = ' ')
    if root.right :
            print('R',root.right.data, end = ' ')
    print()
    printTree(root.left)
    printTree(root.right)

root = createTree('Enter root data : ', -1) 
printTree(root)


'''
class Student : 
    def __init__(self, name, department, rollNo):
        self.name = name 
        self.department = department 
        self.rollNo = rollNo
        print('Inside init : ' , self)
    def printStudent(self) :
        print('Name : ' ,self.name , ' Department : ', self.department, ' Roll No : ', self.rollNo) 

s1 = Student('Abc', 'BCA', 1) 
print('s1 : ', s1)
s2 = Student('Def', 'BBA', 2) 
print('s2 : ', s2)
# s1.printStudent()
# s2.printStudent()
'''

'''
class Node :
    def __init__(self, data):
        self.data = data
        self.next = None 
def printList(head) :
    if head is None :
        return
    print(head.data , end = ' -> ')
    printList(head.next)
def buildList() :
    head, tail = None, None 
    while True :
        data = int(input('Enter data : '))
        if data == -1 :
            return head 
        node = Node(data) 
        if head is None :
            head = tail = node 
        else :
            tail.next = node 
            tail = node  
head = buildList()
printList(head)
'''


'''
def callStack(n) :
    if n == 0 :
        return
    print(n , end = ' ')
    callStack(n - 1) 

n = 2
callStack(n) 
'''