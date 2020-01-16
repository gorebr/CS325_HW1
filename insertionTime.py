import random as r
import time as t

#swap two elements in an array by index
def swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp


#two loop insertion sort
def i_sort(arr):
    #start at every index except first
    for i in range(1,len(arr)):
        j = i
        #move item down until it is bigger than the item before it or at the end
        while(j - 1 >= 0 and arr[j] < arr[j - 1]):
            swap(arr, j, j -1)
            j -= 1

#make array of length n with wandom ints
def randArr(arr, num):
    arr.clear()
    while(len(arr) < num):
        arr.append(r.randint(0,10000))

#seed rand
r.seed(t.time())
#preset runtimes
runNum = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000] #edit me to change array sizes (run times)
runTimes = []
arr = []
start = 0
end = 0

print("Array Lenght, Time(ms)")
#loop through all run times
for num in runNum:
    #fill array to correct size
    randArr(arr,num)
    #record start time
    start = t.time()
    #sort array
    i_sort(arr)
    #record end time
    end = t.time()
    #record data
    print(num, 1000 * (end -start))

