class Node:
    def __init__(self,data, next):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        
    #inserting the data at the start/begining.
    #three things we will have to do:
    # 1: creating the Node
    # 2: store the adress of current head node, since we are inserting at start so to will point to the current              head Node
    # 3: change the current head node to the newly added node as its now at the start
    def insertAtStart(self, data):
        node = Node(data,self.head)
        self.head = node

    #inserting data at the end.
    def insertAtEnd(self, data):
        node = Node(data,None)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


    #inserting data at the middle.
    #deleting the data at the start/begining.
    #deleting data at the end.
    #deleting data at the middle.


    #printing the data.
    def print(self):
        if self.head is None:
            print("No data found")
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next


    #searching the data.
ll = LinkedList()
for _ in range(int(input())):
    ll.insertAtEnd(int(input()))
ll.print()
