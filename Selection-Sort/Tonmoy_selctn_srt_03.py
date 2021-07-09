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
print('Selection Sort Implemention 03:-'.center(35))
# creat function
def selctn_srt(stor):
    lenght = len(stor)

    # 1st loop
    for i in range(lenght - 1):
        # minimum index-->min_indx
        min_indx = i

        for j in range(i + 1, lenght):
            if stor[j] < stor[min_indx]:
                min_indx = j

        if min_indx != i:
            #
            tmp = stor[i]
            stor[i] = stor[min_indx]
            stor[min_indx]= tmp

list = [22,11,2,6,3,0]
print('Unsorted List', list)
selctn_srt(list)
print('Sorted List', list)

"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
