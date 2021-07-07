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
    def __init__(self, data= 'Head', next=None):
        self.data = data
        self.next = next

# creare linked list class
class LinkedList:
    def __init__(self):
        self.head= Node()

    # print Linked list
    def print_linked_list(self):
        if self.head is None:
            print('Linked List is Invalid!')
            return

        current_node = self.head
        info_stor =''
        while current_node:
            info_stor = info_stor + str(current_node.data) + ' --> '
            current_node= current_node.next
        print('Linked List is:-', info_stor)

    # check length
    def get_lenght(self):
        cnt = 0
        current_node = self.head
        while current_node:
            cnt += 1
            current_node= current_node.next
        return print("List Lenght is:-", cnt)


    # Add element at beginning
    def append_at_beginning(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    #
    def remove_data(self, remove_data):
        prevuse_node= self.head
        current_node = prevuse_node.next

        while current_node != None:
            if current_node.data == remove_data:
                break
            prevuse_node = current_node
            current_node = current_node.next

        prevuse_node.next = current_node
        
        if self.head is None:
                print('linked list empty!')
                return

    
#class object creare
list= LinkedList()
# print linked list
list.print_linked_list()
list.get_lenght()
#add element at beginning
list.append_at_beginning(input('Enter 1st Element:-'))
list.append_at_beginning(input('Enter 2nd Element:-'))
list.append_at_beginning(input('Enter 3rd Element:-'))
list.append_at_beginning(input('Enter 4th Element:-'))
#After append  List is
list.print_linked_list()
list.get_lenght()
list.remove_data(input('remove data:-'))
list.print_linked_list()

"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
