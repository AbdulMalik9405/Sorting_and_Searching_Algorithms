import time

Students = ["Malik", "Abdel", "Josh", "Aziz", "Thomas", "Karl", "James", "Eric", "Jason", "David", "Ron", "Bob", "Charlie", "Alice", "Lily", "Mason", "Alex", 
            "Noah", "Olivia", "Emma", "Ella", "Tom", "Max"]
StudentsHash = []
HashTable = [[] for _ in range(20)]
BinaryTreeData = [None] * 23
LeftPointer = [-1] * 23
RightPointer = [-1] * 23
nextFreePointer = 0


def linear_search(name):
    count = 0
    found = True
    for i in range(len(Students)):
        count = count + 1
        if Students[i] == name:
            print(name, " found at position", i+1)
            found = True
            print(count, "Number of trials to find", name)
            break
        else:
            found = False
    if found == False:
        print(name, "not found")
        print(count, "Number of trials")

def hash_function(name):
    NameInt = 0
    for i in range(len(name)):
        NameInt = NameInt + ord(name[i])
    NameInt = NameInt % 19
    return NameInt

def hash_search(name):
    count = 0
    Flag = False
    for i in range(len(HashTable[hash_function(name)])):
        count = count + 1
        if name == HashTable[hash_function(name)][i]:
            print("Name Found at position", hash_function(name)+1)
            print(count, "Number of trials to find", name)
            Flag = True
            break
    if Flag == False:
        print("Name not found")
        print(count, "Number of trials")          

def bubble_sort():
    flag = True
    while flag:
        flag = False
        for i in range(len(Students)-1):
            if Students[i] > Students[i+1]:
                Students[i], Students[i+1] = Students[i+1], Students[i]
                flag = True

def insertion_sort():
    for i in range(1,len(Students)):
        value = Students[i]
        for j in range(1,len(Students)):
            if i-j < 0:
                Students[i-j+1] = value
                break
            elif value < Students[i-j]:
                Students[i-j+1] = Students[i-j]
            else:
                Students[i-j+1] = value
                break

def insertion_sort2():
    for i in range(1,len(Students)):
        value = Students[i]
        compare = 1
        while i-compare >= 0 and value < Students[i-compare]:
            Students[i-compare+1] = Students[i-compare]
            compare += 1
        Students[i-compare+1] = value

def binary_search(name):
    count = 0
    lower_bound = 0
    upper_bound = len(Students)-1
    middle = (upper_bound-lower_bound)//2
    found = True
    while found:
        count = count + 1
        if lower_bound > upper_bound:
            print(name, "not found")
            print(count, "Number of trials")
            found = False
        elif Students[middle] == name:
            print(name, "found at position", middle + 1)
            print(count, "Number of trials to find", name)
            found = False
        elif Students[middle] < name:
            lower_bound = middle+1
            middle = lower_bound + (upper_bound-lower_bound)//2
        else:
            upper_bound = middle-1
            middle = upper_bound - (upper_bound-lower_bound)//2

def insert(pointer, i):
    """Inserts into the left and right pointer"""
    oldPointer = 0
    student = Students[i]
    while pointer != -1:
        current = BinaryTreeData[pointer]
        oldPointer = pointer
        if current is None:
            pointer = -1
            left = None
        elif student < current:
            pointer = LeftPointer[pointer]
            left = True
        else:
            pointer = RightPointer[pointer]
            left = False
    return student, oldPointer, left


def binary_tree(FreePointer):
    """Function to create a binary tree"""
    pointer = 0
    for i in range(len(Students)):
        student, oldPointer, left = insert(pointer, i)
        if left is None:
            LeftPointer[oldPointer] = -1
            RightPointer[oldPointer] = -1
        elif left:
            LeftPointer[oldPointer] = FreePointer
        else:
            RightPointer[oldPointer] = FreePointer

        BinaryTreeData[FreePointer] = student
        FreePointer += 1

def binary_tree_search(name):
    """Search through the binary tree"""
    pointer = 0
    found = False
    count = 1
    while not found:
        if pointer == -1:
            print(f"{name} not found")
            break
        current = BinaryTreeData[pointer]
        if current == name:
            print(f"{name} found")
            print(f"{count} number of trials")
            found = True
        elif name < current:
            pointer = LeftPointer[pointer]
        else:
            pointer = RightPointer[pointer]
        count += 1

binary_tree(nextFreePointer)
print(BinaryTreeData)
print(LeftPointer)
print(RightPointer)

for names in Students:
    index = hash_function(names)
    HashTable[index].append(names)

name = input("input a name: ")

print("Binary tree")
start = time.perf_counter()
binary_tree_search(name)
end = time.perf_counter()
time_difference = end - start
print(time_difference)

# start = time.perf_counter()
# linear_search(name)
# end = time.perf_counter()
# time_difference = end - start
# print(time_difference)

# start = time.perf_counter()
# hash_search(name)
# end = time.perf_counter()
# time_difference = end - start
# print(time_difference)

# bubble_sort()
# start = time.perf_counter()
# binary_search(name)
# end = time.perf_counter()
# time_difference = end - start
# print(time_difference)
