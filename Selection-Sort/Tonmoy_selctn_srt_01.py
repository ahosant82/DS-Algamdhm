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
print('Selection Sort Implemention 01:-'.center(35))
# creat function
def selctn_srt(data_list):
    lenght = len(data_list)

    #1st loop
    for i in range(lenght - 1):
        min_index = i

        #inner loop
        for j in range(i + 1, lenght):
            if data_list[j] < data_list[min_index]:
                min_index = j

        if min_index != i:
            #temporary data-->temp
            temp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = temp

#create list
data_list = ['Uzzol','Moinul','Tonmoy','Nahida','Himu']
print('Unsort', data_list)
selctn_srt(data_list)
print('Sorted', data_list)

"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
