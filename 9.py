def insertionSort(nlist):
    for index in range(1,len(nlist)):
        curr=nlist[index]
        pos=index
        while pos>0 and nlist[pos-1]>curr:
            nlist[pos]=nlist[pos-1]
            pos=pos-1
        nlist[pos]=curr
def mergeSort(nlist):
    print("splitting",nlist)
    if len(nlist)>1:
        mid=len(nlist)//2
        lefthalf=nlist[:mid]
        righthalf=nlist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1
           
        while i<len(lefthalf):
                nlist[k]=lefthalf[i]
                i=i+1
                k=k+1
        while j<len(righthalf):
                nlist[k]=righthalf[j]
                j=j+1
                k=k+1
        print("merging",nlist)
nlist=[1,5,2,3,4,0]
print("Insertion sort before sorting")
print(nlist)
print("Insertionsort after sorting")
insertionSort(nlist)
print(nlist)
print("END OF INSERTION SORT")
nlist=[1,5,2,3,4,0]
print("Merge sort before sorting")
print(nlist)
print("Merge sort after sorting")
mergeSort(nlist)
print(nlist)
print("END OF MERGE SORT")
