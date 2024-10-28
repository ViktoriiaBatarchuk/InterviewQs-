 #Number: 150
 #The task is to find the smallest sub-array in the array with the sum
 #greater that a given value 'x'. Given the array, the array lenght n and value x
 #function should return:
 # -the length 'n' of the shortest subarray that has a sum greater than x
 # - the actuall subarray that has sum greater than x


 #Sliding window approach
def smallest_subarray_with_sum(array, value):
    n=len(array)
    min_length = float('inf')  #start with the inf length
    current_sum = 0
    start = 0
    smallest_subarray = []

    #iterate over the array
    for end in range(n):
        #add current element to current sum
        current_sum += array[end]

        #while current sum is greater than value, try to minimize the window
        while current_sum > value:
            #update minimum lenght and subarray if a smaller one found
            if end-start + 1 < min_length:
                min_length = end-start+1
                smallest_subarray = array[start:end+1]

            #subtract the starting element and move the pointer forward
            current_sum -= array[start]
            start += 1
    #if no valid subarrays found, just return 0 and empty array
    if min_length == float('inf'):
        return 0, []

    return min_length, smallest_subarray


#testing the function
array = [1, 4, 45, 81, 0, 19]
x=51
result = smallest_subarray_with_sum(array, x)
print("Length of smallest subarray: ", result[0])
print("Smallest subarray with sum greater than",x,":",result[1])
