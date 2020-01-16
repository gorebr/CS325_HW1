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

#open files
data = open('data.txt', 'r')
merge = open('merge.txt', 'w')

#loop through all lines (until EOF)
line = data.readline()
while line != "":
    #make array of numbers
    mer = line.split(" ")
    mer.pop(0)
    #convert array to ints
    for i in range(len(mer)):
        mer[i] = int(mer[i])

    #sort array
    m_sort(mer)

    #convert array to strings
    for i in range(len(mer)):
        mer[i] = str(mer[i])

    #convert array to 1 string and add string to file
    merge.write(" ".join(mer) + '\n')

    #read next line
    line = data.readline()

#close files
data.close()
merge.close()
