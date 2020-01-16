import random as r
import time as t

#recursive merge sort; devloped from C code made for cs261
def m_sort(arr):
    #exit condition
    if(len(arr) > 1):
        #find mid and split array
        m = len(arr) // 2
        left = arr[:m]
        right = arr[m:]

        #sort left and right arrays
        m_sort(left)
        m_sort(right)

        #set indexes to 0
        lc = 0
        rc = 0
        i = 0

        #itterate until end of left or right is reached
        while lc < len(left) and rc < len(right):
            #add smaller value from left or right array
            if left[lc] <= right[rc]:
                arr[i] = left[lc]
                lc += 1
            else:
                arr[i] = right[rc]
                rc += 1
            i += 1

        #empty left array if not empty
        while lc < len(left):
            arr[i] = left[lc]
            lc += 1
            i += 1

        #empty right array if not empty
        while rc < len(right):
            arr[i] = right[rc]
            rc += 1
            i += 1

#make array of length n with wandom ints
def randArr(arr, num):
    arr.clear()
    while(len(arr) < num):
        arr.append(r.randint(0,10000))

#seed rand
r.seed(t.time())
#preset runtimes
runNum = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000] #edit me to change array sizes (run times)
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
    m_sort(arr)
    #record end time
    end = t.time()
    #record data
    print(num, 1000 * (end -start))
