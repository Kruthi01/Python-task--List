'''
1. For the given python list, creating list which has all even numbers and another list which has all odd numbers
'''
#Declaring list
list1=[10,501,22,37,100,999,87,351]
#declaring empty list to add them odd or even numbers respectively
even=[]
odd=[]
#Iterating the list
for data in list1:
#Separating odd and even number and storing them in respective list names
    if data%2==0:
        even.append(data)
    else:
        odd.append(data)
#Printing them
print("Even numbers are:",even)
print("Odd numbers are:",odd)

'''_________________________________________________________________________________________________________________________'''
'''
2.Given a python list, finding prime number among them and putting them in new list
'''
#Defining user defined function
def count_primes_in_list(numbers):
#Initializing empty list to store the prime numbers
    prime = []
    for num in numbers:
        if num == 2:
            prime.append(num)
        else:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print (num)
                prime.append(num)
    return len(prime)
list2 = [10,501,22,37,100,999,87,351]
print ("Prime numbers are:",count_primes_in_list(list2))
'''_______________________________________________________________________________________________________________________'''
'''
4. Finding sum of first and last digit of an integer
'''
#Getting integer input from user
inp=input("Enter an Integer:")
#typecasting number into string
string=str(inp)
#Storing index value of first digit variable
firstnum=int(string[0])
#Storing index value of last digit in another variable
lastnum=int(string[-1])
#Adding both variable to get the result
result=firstnum+lastnum
print(result)
'''_______________________________________________________________________________________________________________________'''
'''
6. Finding duplicate from 3 list 
'''
#initializing 3 different list
mylist = [5, 3, 5, 2, 1, 6, 6, 4] 
mylist1=[3,4,5,6,7,6]
mylist2=[2,2,3,3]
newlist = [] 
duplist1 = [] 
#iterate through list1
for i in mylist:
    if i not in newlist:
        newlist.append(i)
    else:
        duplist1.append(i) 
newlist1=[]
duplist2=[]
#iterate through list2
for i in mylist1:
    if i not in newlist1:
        newlist1.append(i)
    else:
        duplist2.append(i)
newlist2=[]
duplist3=[]
#iterate through list3
for i in mylist2:
    if i not in newlist2:
        newlist2.append(i)
    else:
        duplist3.append(i)
#Printing all duplicates from 3 lists
print("List1 duplicates are:", duplist1)
print("List2 duplicates are:", duplist2)
print("List3 duplicates are:", duplist3)
'''______________________________________________________________________________________________________________________'''
'''
7. Finding first non repeating elements in a given list of integers
'''
def first_non_repeated_el(lst):
    ctr = {}
    for i in lst:
        if i in ctr:
            ctr[i] += 1
        else:
            ctr[i] = 1
    for i in lst:
        if ctr[i] == 1:
            return i
    return None
x=[0,1,2,3,4]
print("First Non repeated element is:",first_non_repeated_el(x))
'''________________________________________________________________________________________________________________________'''
'''
8. Finding Minimum element in a rated or sorted list
'''
list1=[7,3,5,6,8,9]
L1=sorted(list1)
#using min method to find the minimum value from the list
res=min(L1)
print("The Original list:",L1)
print("The Minimum element is:",res)
'''________________________________________________________________________________________________________________________'''
'''
9. From the given list find triplet whose sum is equakl
'''
def find3Numbers(A, arr_size, sum): 
    for i in range( 0, arr_size-2): 
        for j in range(i + 1, arr_size-1):  
            for k in range(j + 1, arr_size): 
                if A[i] + A[j] + A[k] == sum: 
                    print("Triplet is", A[i], 
                          ", ", A[j], ", ", A[k]) 
                    return True
    return False 
A = [10,20,30,9] 
sum = 59
arr_size = len(A) 
find3Numbers(A, arr_size, sum) 
'''_______________________________________________________________________________________________________________________'''
'''
10. From the given list find if there is a sub-list with sum equal to zero
'''
def sublist(arr):
    s = set()
    s.add(0)
    total = 0
    for i in arr:
        total += i
        if total in s:
            return True
        s.add(total)
    return False
list1 = [4,2,-3,1,6]
print(sublist(list1))
'''________________________________________________________________________________________________________________________'''