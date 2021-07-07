"""Head session"""
print("Start The Programme".center(35, "-"))
from datetime import date, datetime, time
from os import curdir
now = datetime.now()
days= date.today()
day= now.strftime("%d %B, %Y")
times = now.strftime('%I:%M:%S')
print(day.center(35),"\n",times.center(33))
print("".center(35, "="))
"""Main Program"""
print('Create A Linked List:-'.center(35))
# creat a node class
class Node:
    def __init__(self, data= 'Head', next = None):
        self.data = data
        self.next = next

# create a linked list class
class LinkedList:
    def __init__(self) -> None:
        self.head = Node()

    #linked_list print function
    def print_linked_list(self):
        if self.head is None:
            print('Linked List is Empty!')
            return
        
        cerrent_node = self.head
        stor= ''
        while cerrent_node:
            stor= stor + str(cerrent_node.data) + ' --> '
            cerrent_node = cerrent_node.next
        print('Linked List =',stor)

    # check Lenght at linked list
    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node:
            cnt += 1
            current_node = current_node.next
        return cnt

    # insert elementat specific index
    def insert_at(self, index, data):
        #if the index not found at linked list
        if index < 0 or index > self.get_length():
            print('Invalid Index')
            return

        if self.head.next == None:
         node = Node(data, self.head.next)
         self.head.next = node
         return
        
        # if the index found at linked list 
        cnt = 0
        cerrent_node = self.head
        while cerrent_node:
            if cnt == index - 1:
                node = Node(data, cerrent_node.next)
                cerrent_node.next = node
                break
            cerrent_node = cerrent_node.next
            cnt += 1

# object create
linked_list= LinkedList()
linked_list.print_linked_list()
# insert value
print('Data Insert In Linked List!')
linked_list.insert_at(0, 0000)
linked_list.insert_at(1, 1000)
linked_list.insert_at(2, 2000)
linked_list.insert_at(3, 3000)
linked_list.insert_at(4, 4000)
linked_list.insert_at(5, 5000)
linked_list.insert_at(6, 6000)
linked_list.print_linked_list()
print("After Insert List Size:-", linked_list.get_length())
#
print('Data Insert At Specific Index In Linked List!')
linked_list.insert_at(1, 'Start')
linked_list.insert_at(9, 'End')

linked_list.print_linked_list()
print("After Insert List Size:-", linked_list.get_length())

"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
