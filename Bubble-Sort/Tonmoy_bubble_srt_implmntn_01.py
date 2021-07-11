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
print('Bubble Sort Implemention 01:-'.center(35))
# creat a node class
def bubble_srt(data_list):
    n = len(data_list)      #  n------> Lenght of data list
    for i in range(0, n):
        for j in range(0, n-i-1):
            if data_list[j] > data_list[j+1]:
                # J > j+1 then swap
                temp = data_list[j]       # temp -----> temporary data
                data_list[j] = data_list[j+1]
                data_list[j+1] = temp

# create data List
data_list = [22,13,6,3,25,10,4]
print('Unsorted List =', data_list)
print()
bubble_srt(data_list)
print('After Bubble Sort :')
print('Sorted List =', data_list)
print()
"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
#
n = 6