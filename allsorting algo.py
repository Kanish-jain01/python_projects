import time
#binary search
def binarySearch(l,search):
    print("Binary search\n")
    lower=0
    upper=len(l)-1
    starts=time.perf_counter()
    while(lower<upper):
        mid=(lower+upper)//2
        if(l[mid]==search):
            break
        else:
            if(l[mid]<search):
                lower=mid+1
            else:
                upper=mid-1
    end=time.perf_counter()
    print("Binary search time: ",end-starts)


#linear search
def linearSearch(l,search):
    print("Through Linerar search\n")
    found=False
    starts=time.perf_counter()
    for i in l:
        if(search==i):
            found=True
            break
    end=time.perf_counter()
    if(found):
        print("Yes Found")
    else:
        print("Not in the list\n")
    print("Time for linear search: ",end-starts)

#bubble sort
def bubbleSortandLinear(l,search):
    print("This result is for bubble sort and linear search\n")
    n=len(l)
    start=time.perf_counter()
    for i in range(n-1,0,-1):
        for j in range(i):
            if(l[j]>l[j+1]):
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    end=time.perf_counter()
    print("Sorting done moving to search\n")
    print("Bubble sort time: ",end-start)
    print("\n")
    linearSearch(l,search)

def bubbleSortandBinary(l,search):
    print("This result is for bubble sort and binary search\n")
    n=len(l)
    start=time.perf_counter()
    for i in range(n-1,0,-1):
        for j in range(i):
            if(l[j]>l[j+1]):
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    end=time.perf_counter()
    print("Sorting done moving to search\n")
    print("Bubble sort time: ",end-start)
    print("\n")
    binarySearch(l,search)
    


#selection sort
def selectionSortAndBinary(l,search):
    n=len(l)
    print("These are for selection sort + binary search\n")
    start=time.perf_counter()
    for i in range(n):
        minpos=i
        for j in range(i,n):
            if(l[j]<l[minpos]):
                minpos=j 
        temp=l[i]
        l[i]=l[minpos]
        l[minpos]=temp
        end=time.perf_counter()
    print("Sorting done moving to search\n")
    print("Selection sort time: ",end-start)
    print("\n")
    binarySearch(l,search)

def selectionSortAndlinear(l,search):
    n=len(l)
    print("These are for selection sort + linear search\n")
    start=time.perf_counter()
    for i in range(n):
        minpos=i
        for j in range(i,n):
            if(l[j]<l[minpos]):
                minpos=j 
        temp=l[i]
        l[i]=l[minpos]
        l[minpos]=temp
        end=time.perf_counter()
    print("Sorting done moving to search\n")
    print("Selection sort time: ",end-start)
    print("\n")
    linearSearch(l,search)

#main code
print("Welcome\n")
print("Here are various searching algorithms\n")
l=[78,99,47,83,98,99,45,7,79,4,35,96,32,0,37,35,63,35,45,56,433,233,4567,39300]
print("Please enter the element to be searched\n")
search=int(input())
selectionSortAndBinary(l,search)
bubbleSortandLinear(l,search)
selectionSortAndlinear(l,search)
bubbleSortandBinary(l,search)
