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
class stack:
    def __init__(self):
        self.item = []
    print("Create A Stack :-".center(35))
    #check Stack empty or not
    def empty(self):
        if len(self.item) == 0:
            return print("Stack is empty!")
        else:
            return print("Stack present eliment is =", self.item)

    # check lenthe of stack
    def size(self):
        if len(self.item) == 0:
            pass
        else:
            return print('stack size=',len(self.item))

    # Element push in stack
    def push(self, Value):
        self.item.append(Value)
        return Value
    # Element pop in stack
    def pop(self):
        if len(self.item) == 0:
            return  print('Empty Stack!')
        else:
            return self.item.pop()
    # check the top value in stack
    def top(self):
        return print("Stack Top Value is =",self.item[-1])
# object creating   
Working_Satck = stack()
#check Stack empty or not
Working_Satck.empty()
# check lenthe of stack
Working_Satck.size()
# Pushing Start
print("Start Added element in stack")
Working_Satck.push(int(input('Pushing eliment 1st:-')))
Working_Satck.push(int(input('Pushing eliment 2nd:-')))
Working_Satck.push(int(input('Pushing eliment 3rd:-')))
Working_Satck.push(int(input('Pushing eliment 4th:-')))
Working_Satck.push(int(input('Pushing eliment 5th:-')))
print("After Pushing updated stack is :-",Working_Satck.item)
print('stack size=', len(Working_Satck.item))
# POP from stack is start

print("Start Deleted element in stack:")
print('OUT OF STACK 1st :-', Working_Satck.pop())
# check top value
Working_Satck.top()
print('OUT OF STACK 2nd :-', Working_Satck.pop())
print('OUT OF STACK 3rd :-', Working_Satck.pop())
print('OUT OF STACK 4th :-', Working_Satck.pop())
print('OUT OF STACK 5th :-', Working_Satck.pop())
print('OUT OF STACK 6th :-', Working_Satck.pop())
# after poping check stack empty or not
print()
"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
