import time
import csv

data = []
csvdata = open('data.csv')
reader = csv.reader(csvdata, delimiter=';')
for row in reader:
    data.append([int(x) for x in row])

A = data[0] #10000 Entries
B = data[1] #5000 Entries
C = data[2] #1000 Entries
#Change active array to A B or C to change for both algorithms
ACTIVE_ARRAY = C

#Kadanes Algorithm - the alleged best way to find maximum contiguous subarray
def kadaneAlg(given_array):
    #Storage for the best subarray maximum found so far
    best_total = 0
 
    #Storage for the best subarray ending, at the current entry being checked
    best_for_this_entry = 0
 
    n = 0

    #Traverse every entry in given array
    for i in given_array:
        #Update the maximum sum of sublist "ending" at index `i` (by adding the
        #Current element to maximum sum ending at previous index `i-1`)
        best_for_this_entry = best_for_this_entry + i
 
        #If the maximum sum for this entry is negative, set to 0 (basically an empty sublist)
        best_for_this_entry = max(best_for_this_entry, 0)
 
        #Update best total if the current subarray sum is found to be greater
        best_total = max(best_total, best_for_this_entry)
    #Output best results
    return best_total


#Lowest middle and highest refers to the index of the array, not the value of the entry
def divAndConqMiddle(given_array, lowest, middle, highest):
    lowest_total = 0
    total = 0

    for i in range(middle, lowest-1, -1):
        total = total + given_array[i]
        if total > lowest_total:
            lowest_total = total

    total = 0
    highest_total = 0

    for i in range(middle+1, highest+1):
        total = total + given_array[i]
        if total > highest_total:
            highest_total = total
    
    return lowest_total+highest_total


def divAndConq(given_array, lowest, highest):
    
    #Catcher to stop infinite recursion
    if highest == lowest:
        return given_array[lowest]

    #Establish the middle of the array
    middle = (lowest+highest)//2

    #Recursive splitting to smaller and smaller subarrays to find the maximum subarray total for each
    maxLows = divAndConq(given_array, lowest, middle)
    maxHighs = divAndConq(given_array, middle+1, highest)

    #Get maximum subarray total crossing the middle
    maxMiddle = divAndConqMiddle (given_array, lowest, middle, highest)

    #Output the best of the three
    return max(maxLows,maxHighs,maxMiddle)


start_time = time.time()
print("Maximum contiguous subarray total for A, according to Kadane's, is:", kadaneAlg(ACTIVE_ARRAY))
end_time = time.time()
elapsed_time = (end_time-start_time)*1000
print("With a running time of: " , f'{elapsed_time:.9f}',"ms")

start_time2 = time.time()
print("Maximum contiguous subarray total for A, according to Divide-And-Conquer, is:", divAndConq(ACTIVE_ARRAY, 0, len(ACTIVE_ARRAY)-1))
end_time2 = time.time()
elapsed_time2 = (end_time2-start_time2)*1000
print("With a running time of: " , f'{elapsed_time2:.9f}',"ms")