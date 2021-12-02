# create LinkedList class
class Node:
    def __init__(self, val=0, nex=None):
        self.val=val
        self.next=None

# create Linked List
#class LinkedList:
def LinkedList(list_of_values):
    head1=Node(list_of_values[0])
    h=head1
    for i in list_of_values[1:]:
        head1.next=Node(i)
        head1=head1.next

    global head
    head=h

    print('Your Linked List is:')
    while h:
        #print(h)
        print(h.val,'->',end=' ')
        h=h.next
    print()

print("Enter values for linked list: ")
list_of_values=[int(ele) for ele in input().split()]
LinkedList(list_of_values)

# function for solution
class OddEvenList():
    def oddEvenList(self, head):

        # base case
        if head is None or head.next is None or head.next.next is None:
            return head

        odd=head
        even=head.next
        evenhead=even

        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=evenhead

        return head

if __name__=="__main__":
    obj=OddEvenList()
    res=(obj.oddEvenList(head))
    print('OddEven List is:')
    while res:
        print(res.val,'->', end=' ')
        res=res.next