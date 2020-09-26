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







