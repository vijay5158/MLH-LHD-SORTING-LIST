# 1. Insertion Sort - Time complexity on best , average , worst cases- Ω(n)	θ(n^2)	O(n^2)
def insertion_sort(input_list):   
    for i in range(1, len(input_list)):
        j = i-1
        next_element = input_list[i]
		
        while (input_list[j] > next_element) and (j >= 0):
            input_list[j+1] = input_list[j]
            j=j-1
        input_list[j+1] = next_element

# 2. Selection Sort - Time complexity on best , average , worst cases- Ω(n^2) θ(n^2) O(n^2)
def selection_sort(input_list):

    for index in range(len(input_list)):

        min_index = index
        for j in range( index + 1, len(input_list)):
            if input_list[min_index] > input_list[j]:
                min_index = j


        input_list[index], input_list[min_index] = input_list[min_index], input_list[index]

# 3. Merge Sort - Time complexity on best , average , worst cases- Ω(n log(n)) θ(n log(n)) O(n log(n))
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):

    out = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            out.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            out.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        out = out + right_half
    else:
        out = out + left_half
    return out

# 4. Bubble Sort - Time complexity on best , average , worst cases-	Ω(n) θ(n^2) O(n^2)
def bubble_sort(input_list):
    for i in range(len(input_list)-1,0,-1):
        for j in range(i):
            if input_list[j]>input_list[j+1]:
                temp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = temp


# 5. Quick Sort - Time complexity on best , average , worst cases- Ω(n log(n)) θ(n log(n)) O(n^2)
# Function for partitioning .
def partition(input_list, low, high): 
	i = (low-1)		 # index of smaller element 
	pivot = input_list[high]	 # pivot 

	for j in range(low, high): 

		# If current element is smaller than or 
		# equal to pivot 
		if input_list[j] <= pivot: 

			# increment index of smaller element 
			i = i+1
			input_list[i], input_list[j] = input_list[j], input_list[i] 

	input_list[i+1], input_list[high] = input_list[high], input_list[i+1] 
	return (i+1) 



# Function to do Quick sort 


def quick_sort(input_list, low, high): 
	if len(input_list) == 1: 
		return input_list 
	if low < high: 

		# pi is partitioning index, input_list[p] is now 
		# at right place 
		pi = partition(input_list, low, high) 

		# Separately sort elements before 
		# partition and after partition 
		quick_sort(input_list, low, pi-1) 
		quick_sort(input_list, pi+1, high) 


input_list = [10, 7, 81, 93,56, 1, 5] 
n = len(input_list) 
quick_sort(input_list, 0, n-1) 
print(input_list) 
# ilist = [6,59,37,14,86,70,22,4]

# insertion_sort(ilist)
# print(ilist)

# Python has built in function to sort called sort()
# sorting list of challenge of MLH LHD using sort() function

challenges_list = ['Design an Outfit for Ellie',
    '!Light in your Kitchen',
    'Use the Twilio API',
    'Build a Data Visualization',
    'Write Code to Sort a List',
    'Submit a Challenge with Someone in your Guild',
    'Make a Logo for a Project',
    'Explore Hardware (Emulators Welcome!)',
    'Build a Battlesnake',
    'Share a Meal with Someone in Your Guild'
    ]

challenges_list.sort()
print(challenges_list) 