'''
Number: 154
Task: Given an array of unique integers and a sum value, can you write code to find the number of triplets with
      a sum smaller than the given value?
Solution: We can use a sorted array and a two-pointer approach, which results in an efficient solution
          with a time complexity of O(n2)O(n^2)O(n2).
'''

def find_and_count_triplets(arr, target_sum):
    #Sort an array and apply the two-pointer technique
    arr.sort()
    n = len(arr)
    count = 0
    triplets = []

    #Iterate over the array for looking for triplets
    for i in range(n-2):
        #initiate two pointers
        left = i+1
        right = n-1

        while left < right:
            #calculate the sum of the current triplet
            current_sum = arr[i] + arr[left] + arr[right]

            #If the sum is less that the target, then all triplets
            #between left and right have a sum less than target_sum

            if current_sum < target_sum:
                #Store all valid triplets between left and right
                for k in range(left, right):
                    triplets.append((arr[i], arr[k], arr[right]))
                count += (right - left) # All pairs (arr[left], arr[left+1]...arr[right]) are valid
                left += 1 #move left pointer to the right
            else:
                right -= 1 #move the right pointer to the left
    return count, triplets


#We will put the information about array and target sum from the console
arr = list(map(int,input("Enter an array of integer (separated by spaces): ").split()))
target_sum = int(input("Enter the target sum: "))

#Getting the results
count, triplets = find_and_count_triplets(arr, target_sum)

#Printing the results
print("Number of triples with sum less than", target_sum, ":", count)
print("Triplets with sum less than", target_sum, ":")
for triplet in triplets:
    print(triplet)


