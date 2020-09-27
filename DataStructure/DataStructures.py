list_creation = list()
list_from_tuple = list() #tuple inside paranthesis
my_list = ["Abacus", "Buffalo", "Cat", "Dog"] # list

# iterating list.

for item in my_list:
    print(item)

for index, item in enumerate(my_list):
    print(index, item)

#finding out the length of the list.

print("length",len(my_list))

#finding out minimum and maximum item in list based on their ascii values
#here we cannot insert items as alphanumeric, it must be either number or integer
print("Minimum",min(my_list))
print("Maximum",max(my_list))

#sorting the list, sorting() function return new sorted list.
#for string also it is same.
sorted_list = sorted(my_list)
print("Sorted List", sorted_list)


#counting the number of occurence of item in list using count() method.
#it is same for string.     
print("Counting Dog", my_list.count("Dog"))


#finding out the index of first occurence of specific item in list using index() method.
#it is same for string

print("Index of cat", my_list.index("Cat"))

#unpacking the list using exact number of variable in list.

a,b,c,d = my_list
print("Unpacking")
print(a)
print(b)
print(c)
print(d)


#list comprehensions

x = [m for m in range(10)]
#[0,1,2,3,4,5,6,7]
x = [z**2 for z in range(10) if z > 4]
#[25,36,49,64,81]

# del myList[index], append(item), extend(list), insert(index, item), pop(), remove(item), reverse(), sort() 


#tuples are immutables(cannot change value once assigened) but member inside tuple are mutable.
t = () #empty tuples
t = (1,2,3) #parenthesis are optional
t = 1,2,3
t = 1,
t = tuple() #tuple from list


t = (1,2,3)
#del (t[1]) error cannot change size
#t[1] = 2 error cannot change the value unless it is list.

z = ([0,1], 3) # list and int
del (z[0][1]) # no error, since list is member of tuple so can be changed. # z = ([0],3)

#Set, it doesn't order the object in sequence and no duplicateion.
s = {1,2,1,2}  # result: {1,2}
s = set() #empty set
s = set() #set from list

#Set Comprehension

s = {3*x for x in range(10) if x > 4}
#result :{18,21,24,27} but in random order.

#add(item), remove(item), len(set),  item in set, item not in set, pop() random item from set, clear() all items from set.

#Dictionaries, key value pairs
d = {"a":1, "b": 2}
d = dict([("a":1, "b": 2)])
d = dict ("a":1, "b": 2) 

# basic operation in dict
d["c"] = 3 #adding or chaning item
del d["a"] # remove item from dict
lem(d) #length of dict
d.clear() #remove all items from list

d = {}
d.keys() #returning list of keys
d.values() # returning list of values
d.items() # returning list of key-value pairs from dict.


#iterating dict
#Entries in dict is in ranoom order.

for key in d:
    print(key, d[key])
    
for k,v in d.items():
    print(k,v)


