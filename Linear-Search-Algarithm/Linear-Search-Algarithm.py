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
# linear search algorithm implementation
def linear_Search(arrey, search_list):
    found=False
    for index in range(len(arrey)):
        arrey_item= arrey[index]
        if arrey_item == search_list:
            found= True
            break
    if found == True:
        print('Search item found at index', index,".")
    else:
        print('Search item found not!')

lst = ['10','24','34','33','55','600','Apple','Benana','Ornge','Red','Green','Yollow']
print(lst,'\n')
saerch_item = (input('Input search item = '))
linear_Search(lst, saerch_item)
"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))