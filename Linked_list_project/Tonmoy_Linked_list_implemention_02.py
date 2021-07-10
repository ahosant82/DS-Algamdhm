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
# Linkd list Impkemention 
#    Single link list
print('Create A Linked List'.center(35))
# create a node class
class Node:
    #node --> data | next
    def __init__(self, data=None, next= None) -> None:
        self.data = data
        self.next = next

#create class at linked list
class LinkedList:
    #Head Node --> data | next
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
        print('Liked list =',stor)

    # check Lenght at linked list
    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node:
            cnt += 1
            current_node = current_node.next
        return cnt

    # add element at beginning
    def append_at_begining(self, data):
        node = Node(data,self.head.next)
        self.head.next = node

    # add element at end
    def append_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        end_at_stor=self.head
        while end_at_stor.next:
            end_at_stor= end_at_stor.next

        end_at_stor.next = Node(data, None)

    # insert elementat specific index
    def insert_at(self, index, data):
        #if the index not found at linked list
        if index < 0 or index > self.get_length():
            print('Invalid Index')
            return

        # if the index found at 0 
        if index == 0:
            self.append_at_begining(data)
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


# class object create
if __name__ == '__main__':
    link_list = LinkedList()
    # add element at beginning
    print('Add Item On Linked List At Beginning:-')
    link_list.append_at_begining(input("Input 1st Element :-"))
    link_list.append_at_begining(input("Input 2nd Element :-"))
    link_list.append_at_begining(input("Input 3ed Element :-"))
    link_list.append_at_begining(input("Input 4th Element :-"))
    link_list.print_linked_list()
    print('After Beginning Linked List Lenght:-',link_list.get_length())
    # add element at beginning
    print('Add Item On Linked List At End:-')
    link_list.append_at_end(input('Input 1st Element :-'))
    link_list.append_at_end(input('Input 2nd Element :-'))
    link_list.append_at_end(input('Input 3rd Element :-'))
    link_list.append_at_end(input('Input 4th Element :-'))
    link_list.print_linked_list()
    print('After end Linked List Lenght:-',link_list.get_length())
    # insert elementat specific index
    print('Insert Element Specific Index :-')
    link_list.insert_at(0, 2000)
    link_list.insert_at(3, 200)
    link_list.insert_at(5, 200)
    link_list.insert_at(7, 200)
    link_list.print_linked_list()
    print('After Insert Linked List Lenght:-',link_list.get_length())

"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))