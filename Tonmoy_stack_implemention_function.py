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
print("Create A Stack :-".center(35))
    #check Stack empty or not
def empty(self):
        if len(item) == 0:
            return print("Stack is empty!")
        else:
            return print("Stack present eliment is =", item), print('Stack lenth',len(item))

    # check lenthe of stack
def size():
        if len(item) == 0:
            pass
        else:
            return print('stack size=',len(item))

    # Element push in stack
def push(item,Value):
        item.append(Value)
    # Element pop in stack
def pop(item):
        if len(item) == 0:
            return  print('Empty Stack!')
        else:
            return item.pop()
    # check the top value in stack
def top(self):
        return print("Stack Top Value is =",item[-1])
# function calling  
item = []
#check Stack empty or not
empty(item)
# check lenthe of stack
# print('stack size=', len(item))
# Pushing Start
print("Start Added element in stack")
push(item, int(input('Pushing eliment 1st:-')))
push(item, int(input('Pushing eliment 1st:-')))
push(item, int(input('Pushing eliment 1st:-')))
push(item, int(input('Pushing eliment 1st:-')))
push(item, int(input('Pushing eliment 1st:-')))
print("After Pushing updated stack is :-",item)
print('stack size=', len(item))

# POP from stack is start

print("Start Deleted element in stack:")
# check top value
print('OUT OF STACK 1nd :-', pop(item))
top(item)
print('OUT OF STACK 2nd :-', pop(item))
print('OUT OF STACK 3rd :-', pop(item))
print('OUT OF STACK 4th :-', pop(item))
print('OUT OF STACK 5th :-', pop(item))

# after poping check stack empty or not
empty(item)
print()
"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
