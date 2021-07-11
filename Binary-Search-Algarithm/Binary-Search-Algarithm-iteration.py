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
# Binary search algorithm implementation
print('Binary search algorithm implementation of Iteration Method :', '\n')

def binary_search(list, find_value):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2

        if find_value== list[mid]:
            print('Yes! This Value Found At Index! ', mid)
            return

        if find_value > list[mid]:
            low = mid + 1

        if find_value < list[mid]:
            high = mid - 1
        
    print('OOPS! value not found.')
    print('\n')

list = [10,20,30,40,55,66,77]
print(list)
search = input('Input The Search Item = ')
binary_search(list, int(search))

"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))