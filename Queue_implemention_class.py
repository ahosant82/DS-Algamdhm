"""Head session"""
print("Start The Programme".center(35, "-"))
from datetime import date, datetime, time
now = datetime.now()
days= date.today()
day= now.strftime("%d %B, %Y")
times = now.strftime('%I:%M:%S')
print(day.center(35),"\n",times.center(33))
print("".center(35, "="))
"""Main Program"""
# define the class
class queue:
    def __init__(self):
        self.item = [10,20]
    print("Create A Queue :-".center(35))
    #check Queue empty or not
    def empty(self):
        if len(self.item) == 0:
            return print("Queue is empty!")
        else:
            return print("Queue present eliment is =", self.item)

    # check lenthe of Queue
    def size(self):
        if len(self.item) == 0:
            pass
        else:
            return print('Queue size=',len(self.item))

    # Element enqueue in Queue
    def enqueue(self, Value):
        self.item.append(Value)
        return Value
    # Element deqeuue in Queue
    def dequeue(self):
        if len(self.item) == 0:
            return  print('Empty Queue!')
        else:
            return self.item.pop(0)
    # check the front value in Queue
    def front(self):
        return print("Queue Front Value is =",self.item[0])
    # check the rear value in Queue
    def rear(self):
        return print("Queue Rear Value is =",self.item[-1])
# object creating   
Working_Queue = queue()
#check Queue empty or not
Working_Queue.empty()
# check lenthe of Queue
Working_Queue.size()
# Pushing Start
print("Start Added element in Queue")
Working_Queue.enqueue(int(input('Pushing eliment 1st:-')))
Working_Queue.enqueue(int(input('Pushing eliment 2nd:-')))
Working_Queue.enqueue(int(input('Pushing eliment 3rd:-')))
Working_Queue.enqueue(int(input('Pushing eliment 4th:-')))
Working_Queue.enqueue(int(input('Pushing eliment 5th:-')))
print("After Pushing updated Queue is :-",Working_Queue.item)
# check front value
Working_Queue.front()
# check rear value
Working_Queue.rear()
# after update check Queue empty or not
Working_Queue.empty()
# after update check lenthe of Queue
print('Queue size=', len(Working_Queue.item))
# POP from Queue is start
print("Start Deleted element in Queue:")
print('OUT OF STACK 1st :-', Working_Queue.dequeue())
# after pop check front value
Working_Queue.front()
# after pop check rear value
Working_Queue.rear()
# again pop
print('OUT OF STACK 2nd :-', Working_Queue.dequeue())
print('OUT OF STACK 3rd :-', Working_Queue.dequeue())
print('OUT OF STACK 4th :-', Working_Queue.dequeue())
print('OUT OF STACK 5th :-', Working_Queue.dequeue())
# after poping check Queue empty or not
Working_Queue.empty()
print()
"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
