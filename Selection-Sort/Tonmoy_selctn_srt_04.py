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
print('Selection Sort Implemention 04:-'.center(35))
# creat function
def selctn_srt(data_list):
    lenght = len(data_list)

    #1st loop
    for i in range(lenght - 1):
        #minimum index ---> min_indx
        min_indx = i

        for j in  range(i + 1, lenght):
            if data_list[j] < data_list[min_indx]:
                min_indx = j

            if min_indx != i:
                #
                temp = data_list[i]
                data_list[i] = data_list[min_indx]
                data_list[min_indx] = temp

#create list
data_list = [2,33,12,4,111,24,1]
print('Unsorted', data_list)
selctn_srt(data_list)
print('Sorted', data_list)

"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
