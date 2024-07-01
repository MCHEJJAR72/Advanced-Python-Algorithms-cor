
Tasks Today:
In-Place Algorithms
     a) Syntax
     a) Out of Place Algorithm
     b) In-Class Exercise #1
Two Pointers
Linked Lists
Merge Sort
     a) Video on Algorithms
     b) How it Works
Exercises
     a) Exercise #1 - Reverse a List in Place Using an In-Place Algorithm
     b) Exercise #2 - Find Distinct Words
     c) Exercise #3 - Write a program to implement a Linear Search Algorithm.
In-Place Algorithms
Syntax
# var[i], var[i+1] = var[i+1], var[i]
# Sometimes known as a swap algorithm
def swap(a_list, x, y, z):
    a_list[x], a_list[y], a_list[z] = a_list[z], a_list[y], a_list[x]
    return a_list 

my_list = [20, 4, 10]
print(f"Before swap: {my_list}")

# swap
swap(my_list, 2, 0, 1)

print(f"After swap: {my_list}")
    
    
    
    
    
    
    
    
Before swap: [20, 4, 10]
After swap: [20, 10, 4]
Out of Place Algorithm

In-Class Exercise #1
Write a function that takes in four arguments (list, index1, index2, index3), and swaps those three positions in the list passed in.

l_1 = [10, 4, 3, 8, 4, 2, 6]

def switch(lists, x, y, z):
    lists[x],lists[y],list[z] = lists[z],lists[y],list[x]
    return lists

def switch(lists, a, b, c, d, e, f, g):
    lists[a], lists[b],lists[c],lists[d],lists[e],lists[f],lists[g]
    return lists

print(switch(l_1,0,1,2,3,4,5,6))

    
        
[10, 4, 3, 8, 4, 2, 6]
Two Pointers
Syntax
def twoPointers(alist):
    #create the pointers
    left = 0
    right = len(alist) - 1
    #set up a loop that works through our list and swaps things one pair at a time
    while left <= right:
        alist[left], alist[right] = alist[right], alist[left]
        left += 1
        right -= 1
    return alist

my_list2 = [1, 2, 3, 12, 9, 8, 4, 11, 22]
twoPointers(my_list2)
    
    
    
    
    
    
    
    
[22, 11, 4, 8, 9, 12, 3, 2, 1]
Video of Algorithms
Watch the video about algorithms.

https://www.youtube.com/watch?v=Q9HjeFD62Uk

https://www.youtube.com/watch?v=kPRA0W1kECg

https://www.youtube.com/watch?v=ZZuD6iUe3Pc

Sorting Algorithms
Bubble Sort
Worst Case: O(n^2) Time - O(1) Space

# Best case: O(n) - linear
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def bubbleSort(array):
    isSorted = False
    while not isSorted:
        isSorted = True
        for num in range(len(array) - 1):
            if array[num] > array[num+1]:
                swap(num, num + 1, array)
                isSorted = False
    return array
bubbleSort([22, 55, 44, 1, 100, 34, 66])
[1, 22, 34, 44, 55, 66, 100]
Insertion Sort
Worst Case: O(n^2) time - O(1)space

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j - 1, array)
            j -= 1
    return array
insertionSort([22, 55, 88, 44, 1, 100, 34, 66])
[1, 22, 34, 44, 55, 66, 88, 100]
Merge Sort
How it Works
# Step 1: Split everything into it's own group
# Step 2: From left to right, merge two groups toghter
# Step 3: While merging, place each item in the correct position within the merged group
# Step 4: continue steps 3 - 4 until only one group is left.

from random import randint
# used to generate a ramdom list of 5 numbers from 0 to 20 
nums = [randint(0,20) for i in range(5)]

# Write our merge sort below
def mergeSort(alist):
    print("Splitting...",alist)
    
    # Step 1: Divide the array into equal parts (as much as possible) 
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
# recursively call mergeSort to perform splits if needed
# Then merge once the spilts are done
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
# index pointers for our list
        i = 0 # pointer for left half
        j = 0 # pointer for right half
        k = 0 # pointer for main half
        
# Step 2: Compare the lefthalg and the righthalf
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
# Step 3: While merging, place items in the correct positions
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
        print("Merging...", alist)
        return alist
    
    mergeSort(nums)
            
        
    
        
    
Binary Search
The Binary Search algorithm works by finding the number in the middle of a given array and comparing it to the target. Given that the array is sorted

The worst case run time for this algorithm is O(log(n))
 
Exercises
Exercise #1
Reverse the list below in-place using an in-place algorithm.
For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']

start, end = 0, len(words) - 1
while start < end:
    # Swap elements at start and end indices
    words[start], words[end] = words[end], words[start]
    start += 1
    end -= 1

# Reverse the strings within the list
words = [word[::-1] for word in words]

print(words)
['.', 'ecnetnes', 'a', 'si', 'siht']
Exercise #2
Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
Should output:
{'a': 5,
'abstract': 1,
'an': 3,
'array': 2, ... etc...

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def count_distinct_words(text):
    # Remove punctuation and convert to lowercase
    text = text.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace(':', '')
    
    # Split the text into words
    words = text.split()

    # Count the occurrences of each word using a dictionary
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Input string
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

# Call function
result = count_distinct_words(a_text)
print(result)
{'in': 1, 'computing': 1, 'a': 5, 'hash': 4, 'table': 2, 'map': 2, 'is': 1, 'data': 2, 'structure': 2, 'which': 2, 'implements': 1, 'an': 3, 'associative': 1, 'array': 2, 'abstract': 1, 'type': 1, 'that': 1, 'can': 2, 'keys': 1, 'to': 2, 'values': 1, 'uses': 1, 'function': 1, 'compute': 1, 'index': 1, 'into': 1, 'of': 1, 'buckets': 1, 'or': 1, 'slots': 1, 'from': 1, 'the': 1, 'desired': 1, 'value': 1, 'be': 1, 'found': 1}
Exercise #3
Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.

Hint: Linear Searching will require searching a list for a given number.
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage
my_list = [1, 3, 5, 7, 9, 11, 13]
target_number = 7

result = linear_search(my_list, target_number)

if result != -1:
    print(f'Target {target_number} found at index {result}.')
else:
    print(f'Target {target_number} not found in the list.')
Target 7 found at index 3.