"""Head session"""
print("Start The Programme".center(35, "-"))
from datetime import date, datetime, time
from datetime import date, datetime, time
from os import DirEntry, closerange, curdir
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
    def __init__(self, data= 'Head', next= None):
        self.data = data 
        self.next = next

#crreate a Linked list
class linked_list:
    def __init__(self) -> None:
        self.head = Node()

    # create Linked lost
    def create_l_l(self):
        if self.head is None:
            print('Invalid Linked List')
            return
        #current node
        crnt_node= self.head
        data_stor=''
        while crnt_node != None:
            data_stor = data_stor + str(crnt_node.data) + ' --> '
            crnt_node = crnt_node.next
        print('Linked List : ', data_stor)


    # checkd lenght of list
    def get_lenght(self):
        #count--cnt
        cnt = 0
        #current node--crnt_node
        crnt_node = self.head
        # get current node index
        while crnt_node != None:
            cnt += 1
            crnt_node = crnt_node.next
        return cnt

    # insert linked list
    def insert(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        insert_value = self.head
        while insert_value.next:
            insert_value = insert_value.next

        insert_value.next = Node(data, None)

    # insert specific value
    def insert_spc_vslue(self, index, data):
        # check list empty or not
        if index < 0 or index > self.get_lenght():
            print('Invaild Index')
            return

        if index == 0:
            self.insert(data)
            return

        cnt= 0
        crnt_node= self.head
        while crnt_node:
            if cnt == index -1:
                node= Node(data, crnt_node.next)
                crnt_node.next = node
                break
            crnt_node = crnt_node.next
            cnt += 1

    def search(self, src_itm):
        crnt_node = self.head.next

        while crnt_node != None:
            if crnt_node.data == src_itm:
                print('find')
                return
            crnt_node = crnt_node.next
        print('not fond')

    #
    def reomve(self, rm_itm):
        if self.head.next is None:
            print('Item Not Found!')
            return

        prv = self.head
        crnt = prv.next
        while crnt != None:
            if crnt.data == rm_itm:
                break

            prv = crnt
            crnt = crnt.next
        prv.next = crnt.next


#object create 
l_l= linked_list()
# create linked list
l_l.create_l_l()
# check the lenght of list
print(l_l.get_lenght())
# insert
l_l.insert(10)
l_l.insert(20)
l_l.insert(30)
l_l.create_l_l()
#
l_l.insert_end('end')
l_l.create_l_l()
#
l_l.insert_spc_vslue(0, 100)
l_l.create_l_l()
print(l_l.get_lenght())

#
l_l.search(100)
l_l.search(1000)
l_l.reomve(100)
l_l.reomve(30)
l_l.reomve(10)
l_l.reomve(20)
l_l.reomve('end')
l_l.reomve(1)
l_l.create_l_l()
print(l_l.get_lenght())

"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
