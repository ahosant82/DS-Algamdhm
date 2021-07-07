# Linkd list Impkemention 
#    Single link list
print('Create A Linked List'.center(35))
class Node:
    #node --> data | next
    def __init__(self, data=None, next= None) -> None:
        self.data = data
        self.next = next


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

    # add element at end
    def append_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        end_at_stor=self.head
        while end_at_stor.next:
            end_at_stor= end_at_stor.next
            
        end_at_stor.next = Node(data, None)


# class object create
if __name__ == '__main__':
    link_list = LinkedList()
    # add element at end
    print('Add Item On Linked List At End:-')
    link_list.append_at_end(input('Input 1st Element :-'))
    link_list.append_at_end(input('Input 2nd Element :-'))
    link_list.append_at_end(input('Input 3rd Element :-'))
    link_list.append_at_end(input('Input 4th Element :-'))
    link_list.print_linked_list()
    print('After end Linked List Lenght:-',link_list.get_length())
    print('After Insert Linked List Lenght:-',link_list.get_length())

