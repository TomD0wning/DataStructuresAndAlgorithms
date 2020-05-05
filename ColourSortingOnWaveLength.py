import time

#Implementation of various sorting algorithms that sort colours based on the RGB to wavelength conversion


# inseratoin sort, takes a wavelength and sorts the corresponding pixles
def iterationSort(aList):
    start = time.time()
    for index in range(1,len(aList)):
        currentValue = aList[index]
        position = index

        while position>0 and aList[position-1]>currentValue:
            aList[position]=aList[position-1]
            position = position-1
        aList[position]=currentValue
    end = time.time()
    return aList, end-start

print("IterationSort ",iterationSort(aList))