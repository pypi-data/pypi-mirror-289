'''
Module Name : PythonDSA
Created By  : Ankit Chandok
Website     : https://codexstudios.pythonanywhere.com
Contact Us  : codexstudios@gmail.com,codexcodespace@gmail.com
'''
#########################################################################################################################################
from typing import Iterable
import pprint,ctypes

class MyError(Exception):
	# Constructor or Initializer
	def __init__(self, value):
		self.value = value
	# __str__ is to print() the value
	def __str__(self):
		return(repr(self.value))
def ERROR(func,x):
    raise func(x)
'''
class Main:
    def __init__(self):
        self.service()
    def service(self):
        global hiiw,byew
        class hiiw:
            def run():
                print('hello')
        class byew:
            def run():
                print('bye')
'''
class Algorithms:
    '''
    You can these Algorithms Directly in Your Code no need to write it .
                                                                          By : ANKIT CHANDOK'''
    def __init__(self,classmember:str=None):
        self.classinherited = {}
        self.ImportAlgo(classmember)
    def ImportAlgo(self,classmember:str=None):
        if classmember:
            if classmember.lower() in ['sort','sorting','1']:
                self.SortingAlgo()
                self.classinherited['sort'] = 'SortingAlgo'
            elif classmember.lower() in ['search','searching','2']:
                self.SearchingAlgo()
                self.classinherited['search'] = 'SearchingAlgo'
            elif classmember.lower() in ['*','all']:
                for classmember in ['sort','search']:
                    self.ImportAlgo(classmember)
    def DelAlgo(self,classmember:str='*'):
        global sort,search
        if classmember.lower() in ['sort','sorting','1']:
            del sort,self.classinherited['sort']
        elif classmember.lower() in ['search','searching','2']:
            del search,self.classinherited['search']
        elif classmember == '*':
            del sort,search,self.classinherited['sort'],self.classinherited['search']

    def FixImport(self,ShowFIXREPORT=False):
        if ShowFIXREPORT: print('[DEBUG] ON')
        for classmember in self.classinherited:
            try:
                self.ImportAlgo(classmember)
            except:
                if ShowFIXREPORT:
                    print(f'[DEBUG] Fix Import {classmember} Failed')
                    print('[DEBUG] OFF')
                break
            if ShowFIXREPORT:
                print(f'[DEBUG] Fix Import {classmember} Done')
        else:
            if ShowFIXREPORT:
                print('[DEBUG] Import Fixed Successfully !!')
                print('[DEBUG] OFF')

    def SortingAlgo(self,classmember:str='*'):
        global sort
        class sort:
            def SelectionSort(arr):
                for idx in range(len(arr)):
                    m = idx
                    swap = False
                    for it in range(idx,len(arr)):
                        if arr[m] > arr[it]:
                            m = it
                            swap = True
                    if swap:
                        arr[idx],arr[m]=arr[m],arr[idx]
                return arr
            def bubbleSort(arr):
                n = len(arr)
                # Traverse through all array elements
                for i in range(n):
                    swapped = False
                    # Last i elements are already in place
                    for j in range(0, n-i-1):
                        # Traverse the array from 0 to n-i-1
                        # Swap if the element found is greater
                        # than the next element
                        if arr[j] > arr[j+1]:
                            arr[j], arr[j+1] = arr[j+1], arr[j]
                            swapped = True
                    if (swapped == False):
                        break
            def insertionSort(arr):
                for i in range(1, len(arr)):
                    key = arr[i]
                    j = i - 1

                    # Move elements of arr[0..i-1], that are
                    # greater than key, to one position ahead
                    # of their current position
                    while j >= 0 and key < arr[j]:
                        arr[j + 1] = arr[j]
                        j -= 1
                    arr[j + 1] = key
            def merge(arr, left, mid, right):
                n1 = mid - left + 1
                n2 = right - mid

                # Create temp arrays
                L = [0] * n1
                R = [0] * n2

                # Copy data to temp arrays L[] and R[]
                for i in range(n1):
                    L[i] = arr[left + i]
                for j in range(n2):
                    R[j] = arr[mid + 1 + j]

                i = 0  # Initial index of first subarray
                j = 0  # Initial index of second subarray
                k = left  # Initial index of merged subarray

                # Merge the temp arrays back
                # into arr[left..right]
                while i < n1 and j < n2:
                    if L[i] <= R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1

                # Copy the remaining elements of L[],
                # if there are any
                while i < n1:
                    arr[k] = L[i]
                    i += 1
                    k += 1

                # Copy the remaining elements of R[], 
                # if there are any
                while j < n2:
                    arr[k] = R[j]
                    j += 1
                    k += 1

            def merge_sort(arr, left, right):
                if left < right:
                    mid = (left + right) // 2

                    sort.merge_sort(arr, left, mid) # type: ignore
                    sort.merge_sort(arr, mid + 1, right) # type: ignore
                    sort.merge(arr, left, mid, right) # type: ignore

            def partition(arr, low, high):
                # Choose the pivot
                pivot = arr[high]
                
                i = low - 1
                
                # Traverse arr[low..high] and move all smaller
                # elements on the left side. Elements from low to 
                # i are smaller after every iteration
                for j in range(low, high):
                    if arr[j] < pivot:
                        i += 1
                        arr[i], arr[j] = arr[j], arr[i]
                
                # Move pivot after smaller elements and
                # return its position
                arr[i + 1], arr[high] = arr[high], arr[i + 1]
                return i + 1

            # The QuickSort function implementation
            def quick_sort(arr, low, high):
                if low < high:
                    # pi is the partition return index of pivot
                    pi = sort.partition(arr, low, high)

                    # Recursion calls for smaller elements
                    # and greater or equals elements
                    sort.quick_sort(arr, low, pi - 1)
                    sort.quick_sort(arr, pi + 1, high)
            
            def heapify(arr, N, i):
                largest = i  # Initialize largest as root
                l = 2 * i + 1     # left = 2*i + 1
                r = 2 * i + 2     # right = 2*i + 2

                # See if left child of root exists and is
                # greater than root
                if l < N and arr[largest] < arr[l]:
                    largest = l

                # See if right child of root exists and is
                # greater than root
                if r < N and arr[largest] < arr[r]:
                    largest = r

                # Change root, if needed
                if largest != i:
                    arr[i], arr[largest] = arr[largest], arr[i]  # swap

                    # Heapify the root.
                    sort.heapify(arr, N, largest)

            # The main function to sort an array of given size


            def heapSort(arr):
                N = len(arr)

                # Build a maxheap.
                for i in range(N//2 - 1, -1, -1):
                    sort.heapify(arr, N, i)

                # One by one extract elements
                for i in range(N-1, 0, -1):
                    arr[i], arr[0] = arr[0], arr[i]  # swap
                    sort.heapify(arr, i, 0)
            
            def count_sort(input_array):
                # Finding the maximum element of input_array.
                M = max(input_array)

                # Initializing count_array with 0
                count_array = [0] * (M + 1)

                # Mapping each element of input_array as an index of count_array
                for num in input_array:
                    count_array[num] += 1

                # Calculating prefix sum at every index of count_array
                for i in range(1, M + 1):
                    count_array[i] += count_array[i - 1]

                # Creating output_array from count_array
                output_array = [0] * len(input_array)

                for i in range(len(input_array) - 1, -1, -1):
                    output_array[count_array[input_array[i]] - 1] = input_array[i]
                    count_array[input_array[i]] -= 1

                return output_array

    def SearchingAlgo(self,classmember:str='*'):
        global search
        class search:
            def linear_search(arr, N, x):
                for i in range(0, N):
                    if (arr[i] == x):
                        return i
                return -1
            def binary_search(arr, low, high, x):
                # Check base case
                if high >= low:
                    mid = (high + low) // 2
                    # If element is present at the middle itself
                    if arr[mid] == x:
                        return mid
                    # If element is smaller than mid, then it can only
                    # be present in left subarray
                    elif arr[mid] > x:
                        return search.binary_search(arr, low, mid - 1, x) # type: ignore
                    # Else the element can only be present in right subarray
                    else:
                        return search.binary_search(arr, mid + 1, high, x) # type: ignore
                else:
                    # Element is not present in the array
                    return -1
            # Function to perform Ternary Search
            def ternary_Search(l, r, key, ar):
                if (r >= l):
                    # Find the mid1 and mid2
                    mid1 = l + (r - l) //3
                    mid2 = r - (r - l) //3
                    # Check if key is present at any mid
                    if (ar[mid1] == key): 
                        return mid1
                    if (ar[mid2] == key): 
                        return mid2
                    # Since key is not present at mid,
                    # check in which region it is present
                    # then repeat the Search operation
                    # in that region
                    if (key < ar[mid1]): 
                        # The key lies in between l and mid1
                        return search.ternary_Search(l, mid1 - 1, key, ar)
                    elif (key > ar[mid2]): 
                        # The key lies in between mid2 and r
                        return search.ternary_Search(mid2 + 1, r, key, ar)
                    else: 
                        # The key lies in between mid1 and mid2
                        return search.ternary_Search(mid1 + 1,mid2 - 1, key, ar)
                # Key not found
                return -1
            def jump_Search( arr , x , n ):
                import math
                # Finding block size to be jumped
                step = math.sqrt(n)
                # Finding the block where element is
                # present (if it is present)
                prev = 0
                while arr[int(min(step, n)-1)] < x:
                    prev = step
                    step += math.sqrt(n)
                    if prev >= n:
                        return -1
                # Doing a linear search for x in 
                # block beginning with prev.
                while arr[int(prev)] < x:
                    prev += 1 
                    # If we reached next block or end 
                    # of array, element is not present.
                    if prev == min(step, n):
                        return -1
                # If element is found
                if arr[int(prev)] == x:
                    return prev
                return -1
            def interpolation_Search(arr, lo, hi, x):
                    # Since array is sorted, an element present
                    # in array must be in range defined by corner
                if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
            
                    # Probing the position with keeping
                    # uniform distribution in mind.
                    pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                                (x - arr[lo]))
            
                    # Condition of target found
                    if arr[pos] == x:
                        return pos
            
                    # If x is larger, x is in right subarray
                    if arr[pos] < x:
                        return search.interpolation_Search(arr, pos + 1,
                                                hi, x)
            
                    # If x is smaller, x is in left subarray
                    if arr[pos] > x:
                        return search.interpolation_Search(arr, lo,
                                                pos - 1, x)
                return -1
            def fibMonaccian_Search(arr, x, n): 
  
                # Initialize fibonacci numbers 
                fibMMm2 = 0  # (m-2)'th Fibonacci No. 
                fibMMm1 = 1  # (m-1)'th Fibonacci No. 
                fibM = fibMMm2 + fibMMm1  # m'th Fibonacci 
            
                # fibM is going to store the smallest 
                # Fibonacci Number greater than or equal to n 
                while (fibM < n): 
                    fibMMm2 = fibMMm1 
                    fibMMm1 = fibM 
                    fibM = fibMMm2 + fibMMm1 
            
                # Marks the eliminated range from front 
                offset = -1
            
                # while there are elements to be inspected. 
                # Note that we compare arr[fibMm2] with x. 
                # When fibM becomes 1, fibMm2 becomes 0 
                while (fibM > 1): 
            
                    # Check if fibMm2 is a valid location 
                    i = min(offset+fibMMm2, n-1) 
            
                    # If x is greater than the value at 
                    # index fibMm2, cut the subarray array 
                    # from offset to i 
                    if (arr[i] < x): 
                        fibM = fibMMm1 
                        fibMMm1 = fibMMm2 
                        fibMMm2 = fibM - fibMMm1 
                        offset = i 
            
                    # If x is less than the value at 
                    # index fibMm2, cut the subarray 
                    # after i+1 
                    elif (arr[i] > x): 
                        fibM = fibMMm2 
                        fibMMm1 = fibMMm1 - fibMMm2 
                        fibMMm2 = fibM - fibMMm1 
            
                    # element found. return index 
                    else: 
                        return i 
            
                # comparing the last element with x */ 
                if(fibMMm1 and arr[n-1] == x): 
                    return n-1
            
                # element not found. return -1 
                return -1
            def exponential_search(arr, x):
                n = len(arr)
                if n == 0:
                    return -1
            
                # Find range for binary search by repeatedly doubling i
                i = 1
                while i < n and arr[i] < x:
                    i *= 2
            
                # Perform binary search on the range [i/2, min(i, n-1)]
                left = i // 2
                right = min(i, n-1)
            
                while left <= right:
                    mid = (left + right) // 2
                    if arr[mid] == x:
                        return mid
                    elif arr[mid] < x:
                        left = mid + 1
                    else:
                        right = mid - 1
            
                return -1
    def DatabaseAlgo(self,classmember:str='*'):
        pass

    def __str__(self)->str:
        return f'PythonDSA = (Algorithms)[Include] =>{str(self.classinherited)} '
    
class Stack(Exception):
    def __init__(self,stack,size=10):
            self.stack = stack
            self.__size = size
            self.__errors = {
                'NI' : 'Not Implemented',
                'OverFlow' : 'Sorry , Stack OverFlow 😊 .',
                'UnderFlow' : 'Sorry , Stack is Empty 😊 .',
                'ChangeSize' : 'Sorry , The Stack will be OverFlow by Doing This So Not Implemented  😊 .'
            }
    def push(self,value,ThrowERROR=False):
        if (self.__size == len(self.stack)):
            if (ThrowERROR):
                ERROR(Stack,self.__errors['OverFlow'])
            else:
                return print(self.__errors['OverFlow'])
        else:
            try:
                self.stack.append(value)
            except:
                if (ThrowERROR):
                    ERROR(Stack,self.__errors['NI'])
                else:
                    print(self.__errors['NI'])
    def pop(self,tell=None,ThrowERROR=False):
        try:
            if tell:
                if (tell.lower()=='return'):
                    return self.stack.pop()
                elif (tell.lower()=='tell'):
                    print(f'The Item Removed From Stack is {self.stack.pop()}')
            else:
                self.stack.pop()
        except:
            if (ThrowERROR):
                ERROR(Stack,self.__errors['UnderFlow'])
            else:
                print(self.__errors['UnderFlow'])
    def peek(self,Return=None,ThrowERROR=False):
        try:
            if (Return==None):
                print(f'The Peek Item in The Stack is {self.stack[-1]}')
                return self.stack[-1]
            elif (Return):
                return self.stack[-1]
            else:
                print(f'The Peek Item in The Stack is {self.stack[-1]}')
        except:
            if (ThrowERROR):
                ERROR(Stack,self.__errors['UnderFlow'])
            else:
                print(self.__errors['UnderFlow'])
    def IsEmpty(self):
        if (self.stack==[]):
            return True
        else:
            return False
    def IsFull(self):
        if (len(self.stack == self.__size)):
            return True
        else:
            False
    def OfSize(self):
        return len(self.stack)
    def MaxSize(self,Return=None):
        if (Return):
            return self.__size
        else:
            print(f'Max Size Allocated to this Stack is {self.__size} 😊 .')
    def SpaceLeft(self,Return=None):
        if (Return):
            return (self.__size - len(self.stack))
        else:
            print(f'The Space Left to Add Items in this Stack is {(self.__size - len(self.stack))} 😊 .')
    def ChangeSize(self,size):
        if (size > len(self.stack)):
            self.__size = size
        else:
            print(self.__errors['ChangeSize'])
    def ClearStack(self):
        self.stack = []

class Queue:
    pass

class PriorQueue:
    pass

class Deque:
    pass
        

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.start = None
    def viewList(self):
        if self.start == None:
            print('List is Empty .')
        else:
            temp = self.start
            while temp != None:
                print(temp.data,end=' ')
                temp = temp.next
    def deleteFirst(self):
        if self.start == None:
            print('Linked List is Empty .')
        else:
            self.start = self.start.next
    def insertFirst(self,value):
        FirstNode = value
        temp = self.start
        self.start = Node(FirstNode)
        self.start.next = temp
    def insertLast(self,value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode


class MeraList:

  def __init__(self):
    self.size = 1
    self.n = 0
    # create a C type ka array with size -> self.size
    self.A = self.__make_array(self.size)

  def __len__(self):
    return self.n

  def append(self,item):
    # check if vacant
    if self.n == self.size:
      # array is full -> resize
      self.__resize(self.size*2)

    self.A[self.n] = item
    self.n = self.n + 1

  def pop(self):
    if self.n == 0:
      return 'Empty List'
    print(self.A[self.n-1])
    self.n = self.n - 1

  def clear(self):
    self.n = 0
    self.size = 1

  def find(self,item):

    for i in range(self.n):
      if self.A[i] == item:
        return i
    return 'ValueError - not in list'

  def insert(self,pos,item):

    if self.n == self.size:
      self.__resize(self.size*2)

    for i in range(self.n,pos,-1):
      self.A[i] = self.A[i-1]

    self.A[pos] = item
    self.n = self.n + 1

  def remove(self,item):
    # search and get pos
    pos = self.find(item)
    if type(pos) == int:
      # delete
      self.__delitem__(pos)
    else:
      return pos

  def __resize(self,new_capacity):
    # create a new array with new capacity
    B = self.__make_array(new_capacity)
    self.size = new_capacity
    # copy the content of old array to new one
    for i in range(self.n):
      B[i] = self.A[i]
    # reassign A
    self.A = B

  def __str__(self):
    result = ''
    for i in range(self.n):
      result = result + str(self.A[i]) + ','

    return '[' + result[:-1] + ']'

  def __getitem__(self,index):

    if 0<= index < self.n:
      return self.A[index]
    else:
      return 'IndexError'

  def __delitem__(self,pos):
    # delete pos wala item
    if 0<= pos < self.n:
      for i in range(pos,self.n-1):
        self.A[i] = self.A[i+1]

      self.n = self.n - 1

  def __make_array(self,capacity):
    # referential array(C type)
    return (capacity*ctypes.py_object)()
      
class Array(list):
    '''This is Created by : Ankit Chandok'''
    def __init__(self,array,size_FIXED=False):
        if size_FIXED:
            self.size = size_FIXED
            self.changeSize = self.__changeSize
            self.add = self.__add
            self.join = self.__join
        else:
            self.size = False
            self.add = self.append
            self.join = self.extend
        self.changeLimitProperty = self.__changeLimitProperty
        if array:
            self.extend(array)
        self.__errors = {
            "NI" : "Not Implemented",
            "ChangeSize" : 'Sorry , The Array will be OverFlow by Doing This So Not Implemented  😊 .'
        }
    def __changeSize(self,size):
        self.size = size
    def __changeLimitProperty(self,new,ThrowERROR=False):
        if self.size:
            if len(self) <= new:
                self.size = new
                self.changeSize = self.__changeSize
                self.add = self.__add
                self.join = self.__join
            else:
                if ThrowERROR:
                    raise Exception(self.__errors['ChangeSize'])
                else:
                    return print(self.__errors['ChangeSize'])
        else:
            self.size = False
            self.add = self.append
            self.join = self.extend

            return print('Some Unexpected Error Occured .')
    def __add(self,value,ThrowERROR=False):
        if len(self) < self.size:
            self.append(value)
        else:
            if ThrowERROR:
                raise Exception(self.__errors['NI'])
            else:
                return print(self.__errors['NI'])
    def __join(self,value,ThrowERROR=False):
        if len(self) < self.size:
            self.extend(value)
        else:
            if ThrowERROR:
                raise Exception(self.__errors['NI'])
            else:
                return print(self.__errors['NI'])
    def __str__(self):
        return f'Array([ {" ".join(self)} ])'
    def __add__(self,*args):
        if self.size:
            if ( len(self) + sum([len(i) for i in args]) ) <= self.size:
                for val in args:
                    self.join(val)
            else:
                return print(self.__errors['NI'])
        else:
            for val in args:
                self.join(val)
        return self
    def __mul__(self,*args):
        if self.size:
            final = 1
            for i in args:
                final *= i
            if ( len(self) * final ) <= self.size:
                for val in args:
                    self.join(list(self)*(val-1))
            else:
                return print(self.__errors['NI'])
        else:
            for val in args:
                self.join(list(self)*(val-1))
        return self
    def Credits(self):
        print('''
Created By : Ankit Chandok
Email ID   : codexcodespaceltd@gmail.com
Website    : https://codexstudiosltd.pythonanywhere.com
              ''')
        
class DimensionalArray(Array):
    def __init__(self,dimension=False,array=False,size=False,**kwargs):
        self.dimension = dimension
        self.size = size
        if array:
            if (self.dimension.upper() == '2D'):
                sample = len(array[0])
                for val in array:
                    if sample != len(val):
                        self.extend([[None]*sample for i in range(len(array))])
                        break
                else:
                    self.extend(array)
        else:
            if dimension[0] == '3':
                array = [[ [None for col in range(kwargs['col1'])] for col in range(kwargs['col2'])] for row in range(kwargs['row'])]
            elif dimension[0] == '2':
                array = [[None for i in range(kwargs['column'])] for j in range(kwargs['row'])]
                pass
            elif dimension[0] == '1':
                array = [None for el in range(kwargs['column'])]
            else:
                array = [[None,None],[None,None]]
            self.extend(array)
        self.lastcorrect = list(self)
        self.__errors = {
            "NI" : "Not Implemented",
            "ChangeSize" : 'Sorry , The Array will be OverFlow by Doing This So Not Implemented  😊 .'
        }
    def Check(self):
        if self.dimension[0] == '1':
            pass
        elif self.dimension[0] == '2':
            if self:
                self.__sample = len(self[0])
                try:
                    for val in self:
                        if self.__sample != len(val):
                            self.clear()
                            self.extend(list(self.lastcorrect))
                            break
                    else:
                        pass
                except:
                    self.clear()
                    self.extend(list(self.lastcorrect))
            else:
                self
        elif self.dimension[0] == '3':
            pass
    def add(self,Array):
        self.Check()
        if self:
            if len(Array) == self.__sample:
                self.append(Array)
                self.lastcorrect = list(self)
            else:
                const = self.__sample - len(Array)
                Array.extend([None]*const)
                self.append(Array)
                self.lastcorrect = self
        else:
            self.append(Array)
            self.lastcorrect = list(self)
    def __str__(self):
        return f'DimensionalArray({self.dimension.upper()})([ {" ".join([str(i) for i in self])} ])'

class NumArray(Array):
    pass

class Matrix(list):
    def __init__(self,matrix):
        pass
def ShowArray(x):
    pprint.pprint(x)

##################################################################################
