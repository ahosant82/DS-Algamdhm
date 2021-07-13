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
print('Insertion Sort Implemention for Asending:-'.center(35), '\n')
# creat a Function
def insrtion_srt(data_list):
    lenght = len(data_list)   #lenght of data list

    for i in range(1, lenght):             # 1st loop

        element = data_list[i]   # elemnt----> value of datalist
        j = i-1
        while j>= 0 and data_list[j] > element:   # 2nd loop

            data_list[j+1]= data_list[j]
            j = j-1
        data_list[j+1] = element

# create data List
data_list = [13,4,1,8,7,10]
print('Unsorted List', data_list)
insrtion_srt(data_list)
print('After Insertion Sort:-')
print('Sorted List', data_list)
"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
