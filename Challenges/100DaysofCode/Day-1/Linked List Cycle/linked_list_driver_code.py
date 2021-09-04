class Node:
    def __init__(self, data):
        self.data=data
        self.next=None  

class LinkedList:
    def __init__(self):
        self.head=None
        self.__size=0
    
    def push(self, data):
        """creating function
        for a defualt push at the beginning
        """
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.__size+=1
    
    def display(self):
        if self.isEmpty():
            print("Linked List has no elements.")
        else:
            n=self.head
            while n:
                print(n.data,"--->",end=" ")
                n=n.next

    def get_size(self):
        return self.__size

    def isEmpty(self):
        return (self.get_size()==0)

if __name__=="__main__":
    ll=LinkedList()
    ll.push(2)
    ll.push(-4)
    ll.push(0)
    ll.push(2)
    ll.push(3)
    ll.display()

