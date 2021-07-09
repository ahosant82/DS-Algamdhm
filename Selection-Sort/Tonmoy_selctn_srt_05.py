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
print('Selection Sort Implemention 05:-'.center(35))
# creat function
class Srtd_lst:
    def __init__(self) -> None:
        pass
    def selctn_srt(self, data_list):
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
out = Srtd_lst()
data_list = ['X','E','S','A','D','Z','t']
print('Unsorted', data_list)
out.selctn_srt(data_list)
print('Sorted', data_list)

"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))
