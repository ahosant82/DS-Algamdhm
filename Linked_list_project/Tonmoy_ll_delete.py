"""Head session"""
print("Start The Programme".center(35, "-"))
from datetime import date, datetime, time
from datetime import date, datetime, time
from os import DirEntry, closerange, cpu_count, curdir, link, path
now = datetime.now()
days= date.today()
day= now.strftime("%d %B, %Y")
times = now.strftime('%I:%M:%S')
print(day.center(35),"\n",times.center(33))
print("".center(35, "="))
"""Main Program"""
print('Element Delete in Linked List:-'.center(35))
# creat a node class
class Node:
    def __init__(self, data= "Head", next= None) -> None:
        self.data = data
        self.next = next

# create a linked list class
class LinkedList:
    def __init__(self) -> None:
        self.head = Node()

    #create linked list
    def Linkd_list(self):
        if self.head is None:
            print('Invalid Link list!')
            return

        #current node ---> crnt
        crnt_node = self.head
        Data_Stor = ''
        while crnt_node != None:
            Data_Stor = Data_Stor + str(crnt_node.data) + ' --> '
            crnt_node = crnt_node.next
        print('Linked List is :-', Data_Stor)

    # Insert value in linked list
    def insert(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    # Delete Element
    def remove_itm(self , rm_itm):
        if self.head.next is None:
            print('Value is Not Found!')
            return
        prev = self.head
        crmt_node = prev.next
        while crmt_node != None:
            if crmt_node.data == rm_itm:
                break
            prev = crmt_node
            crmt_node = crmt_node.next
        prev.next = crmt_node.next

# class object create
linkd_lst = LinkedList()
linkd_lst.Linkd_list()
#inserted Value
print('Insert Value In List:', '\ns')
linkd_lst.insert(input('Input Insert Element:-'))        
linkd_lst.insert(input('Input Insert Element:-'))        
linkd_lst.insert(input('Input Insert Element:-'))        
linkd_lst.insert(input('Input Insert Element:-'))     
linkd_lst.Linkd_list()   
# delete value 
print('Delete element from Linked List:','\n')
linkd_lst.remove_itm(input('Input Delete Element :-'))
linkd_lst.remove_itm(input('Input Delete Element :-'))
linkd_lst.Linkd_list()


"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
