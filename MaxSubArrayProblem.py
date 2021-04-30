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
 
#change active array to A B or C to change for both algorithms
ACTIVE_ARRAY = A

start_time = time.time()
print("Maximum contiguous subarray total for A, according to Kadane's, is:", kadaneAlg(ACTIVE_ARRAY))
end_time = time.time()
elapsed_time = (end_time-start_time)*1000
print("Running time: " , f'{elapsed_time:.9f}')