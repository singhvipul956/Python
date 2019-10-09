a=5
b="10"
c=a+int(b) #type Casting

d="Hello World"

print(d)
print(d.lower())
print(d.upper())
print(d[4])
print(d[2:7])
print(d[3:])
print(d[:3])

print(type(a)) #To know type of variable
print(type(b))

#hex(), bin(), and oct() To convert integer value
#datetime.now()
#import datetime
#import strftime
#datetime.datetime(2016, 3, 10, 2, 16, 19, 962429)
#strftime(“%Y-%m-%d %H:%M:%S”)

print("Befor : "+str(c)) 

b=int(b)

#Conditions  
if a<int(b) : 
    c=b-a
elif a>int(b) : 
    c=a-b
else :
    c=a+b

print("After : "+str(c))

'''Python Collection  (Multiline Comment)
1.List
2.Tuple
3.Set
4.Dictionary
'''

#List
lst = [20,25,30,35,40,45,50]
print("Before : ")
print(lst)

lst0 = lst[0]
lst[2]=105
lst1 =lst[2:4]
lst.append(55)      #To append to last
lst.insert(2,55)    #To insert at specific
lst.pop()           #To remove last item
lst.remove(55)      #To delete item from list
del lst[3]          #To delete specific item

print("After : ")
print(lst0)
print(lst)


#lst.clear()         #To clear the list
#del lst             #To delete whole list

#Dictionaty

dic = {"Name" : "VIP", "Class" : "12", "Marks" : 34}
dic["Marks"] = 56
print(dic["Marks"])
print(dic)
dic.pop("Marks") #Del #Update #Clear


#Tuple  Dif is you can't change tuple values.

tup = ("Harry","Rohan","Raunak")

print(tup)

#var = list(tup)
#var = tupple(lst)

#Set

st = {23,2,2,2,2,25,23,45,56,48,13}
print(st)
st.add(4556) #To Add Single item
print(st)
st.update([12,12,3425,78456,23]) #To Add multiple item
st.remove(12) #pass item that is in set or it will give error
st.discard(12) #to avoid error use discard
st.pop()
st.clear()

#Loops

print("\nfor Loop : ")

for item in lst:
    print(item)
print("\n")
for j in range(1,10):
    print(j)

print("\nWhile Loop : ")
lstforLoop  = ["ABC","BBC","XYZ"]

i=0
while(i<len(lstforLoop)):
    print(lstforLoop[i])
    i=i+1

#Function        
print("\nFunctions : ")

def callfunction():
    print(a+b+c)
    print("Function Called")

callfunction()

print("\nFunctions with arguement : ")

name = input("May I know your name? ")
print("It’s a pleasure to meet you " + name + "!")

def sum(x,y):
    Z=int(x)+int(y)
    return Z

fnum = input("First Number")
snum = input("Second Number")

result = sum(fnum,snum)
print("Sum of two numbers : "+str(result))
#print(result)
        

lstrange = list (range(10, 51, 5))
print(lstrange)


#OOPS

class Employee:
    def __init__(self,gname,gsal):
        self.name=gname
        self.salary=gsal


ClassObj = Employee("Vipul",145698)

print(ClassObj.name)
print(ClassObj.salary)
