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
    # 2: store the adress of current head node, since we are inserting at start so to will
    # point to the current head Node
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


    #inserting data at the anywhere.

    # 1.traverse to that index
    # 2.create a node with data and next pointing to the index node.
    # 3.set next of its previous node of the index to the newly created node.


    def insertAtindex(self, data, index):
        itr = self.head
        prev = self.head
        c = 1
        while itr:
            if c == index:
                node = Node(data, itr)
                if index == 1:
                    self.head = node
                if index != 1:
                    prev.next = node
            prev = itr
            itr = itr.next
            c += 1
        if index >= c:
            ll.insertAtEnd(data)





    #deleting the data at the start/begining.(queue pop out)
    def deleteAtStart(self):
        self.head = self.head.next


    #deleting data at the end.(stack pop out)
    def deleteAtend(self):
        itr = self.head
        prev = itr
        while itr:
            if itr == self.tail:
                if self.tail == self.head:
                    self.head = None
                prev.next = None
                self.tail = prev
            prev = itr
            itr = itr.next


    #deleting data at the anywhere/index.
    # we are taking 1 based indexing everywhere in all index operations

    def deleteAtIndex(self, index):
        if index == 1:
            self.head = self.head.next
            return
        itr = self.head
        prev = itr
        c = 1
        while itr:
            if c == index:
                itr = itr.next
                prev.next = itr
                if itr == None:
                    self.tail = prev
                return
            prev = itr
            itr = itr.next
            c += 1


    #printing the data.
    def print(self):
        if self.head is None:
            print("No data found")
        itr = self.head
        while itr:
            print(itr.data,end = ' ')
            itr = itr.next

    #searching the data.
    #In linkedlist we have to perform linear search only as
    #binary search is not possible
    def search(self, data):
        itr = self.head
        index = 1
        while itr:
            if itr.data == data: return index
            itr = itr.next
            index += 1
        return 'Number not found'



ll = LinkedList()
for _ in range(int(input())):
    ll.insertAtEnd(int(input()))
ll.print()
print("\n"+ll.search(41))
ll.print()
print()
ll.deleteAtIndex(6)
ll.print()
print()
# directly access to the recently added data of the linkedlist(stack)
print(ll.tail.data)

# directly access to the first added data of the linkedlist(queue)
print(ll.head.data)


