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
print('Binary search algorithm implementation of Recursive Method :')
def binary_search(arrey, low, high, found):

	# Check base case
	if high >= low:

		mid = (high + low) // 2

		# If element is present at the middle itself
		if arr[mid] == found_value:
			return mid
		# be present in left subarray
		elif arr[mid] > found_value:
			return binary_search(arr, low, mid - 1, found_value)

		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, found_value)
        # Element is not present in the array
	else:
		return -1

# Test array
arr = [ 2, 33, 22, 11,1,10,24,12,200,100,2000,334,550,123,444 ]
arr.sort()
print(arr, '\n')
found_value = int(input("Search eliment is ="))

# Function call
result = binary_search(arr, 0, len(arr)-1, found_value)
print('\n')
if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")

"""Footer Session"""
print("".center(35, "="))
print("End The Programme".center(35,"-"), "\n", "Developed By @A.R.Tonmoy".center(33))