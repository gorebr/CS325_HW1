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

#open files
data = open('data.txt', 'r')
insert = open('insert.txt', 'w')

#read firstline
line = data.readline()

#loop trough all lines
while line != "":
    #creat array of strings with numbers
    ins = line.split(" ")
    ins.pop(0)
    #convert strings to ints
    for i in range(len(ins)):
        ins[i] = int(ins[i])

    #sort array
    i_sort(ins)

    #convert ints bact to strings
    for i in range(len(ins)):
        ins[i] = str(ins[i])

    #make aray into 1 string and write it to file
    insert.write(" ".join(ins) + '\n')

    #read next line
    line = data.readline()

#close files
data.close()
insert.close()
