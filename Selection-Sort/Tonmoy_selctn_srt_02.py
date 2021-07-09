"""Head session"""
print("Start The Programme".center(35, "-"))
from datetime import date, datetime, time
from os import curdir
from os import listdir
now = datetime.now()
days= date.today()
day= now.strftime("%d %B, %Y")
times = now.strftime('%I:%M:%S')
print(day.center(35),"\n",times.center(33))
print("".center(35, "="))
"""Main Program"""
print('Selection Sort Implemention 02:-'.center(35))
# creat function
def selctn_srt(list):
    lenght = len(list)

    # 1st loop list = length - 1
    for i in range(lenght - 1):
        # minimum index -- min_index
        min_index = i

        for j in  range(i + 1, lenght):
            if list[j] < list[min_index]:
                min_index = j

        if min_index != i:
            #temporary data -- temp
            temp = list[i]
            list[i] = list[min_index]
            list[min_index]= temp

# list create
list = [10,2,0,55,1,444]
print('Unsorted List', list)
selctn_srt(list)
print('Sorted List', list)
            
"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
