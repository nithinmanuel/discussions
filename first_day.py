
# simple multipllication
width = 20
height = 10 
area = width * height 
print(area)

# divison 

tax = 22.5/100
product_price = 60 
taxed_amout = 60 * tax
total_price = product_price + taxed_amout
print(total_price) 

# string example 

name = "covala"
moto = "dosen't walk , only sleep "
print(moto)

# string concatination
first_name = "coavala"
last_name = "australian"
full_name = first_name + last_name
print(full_name)

# inedex finding the value by address
word = "python"
print(word[0])
print(word[5])
# count from right 
word[-1]
word[-4]
#print(word[6]) # error there is no value (character) in this address location 
# slicing 

first_slice = word[0:3]
print(first_slice)
last_slice = word[3:]
print(last_slice)
full_slice = word[:2] + word[2:]
print(full_slice)

# lists are the arrays in python

fruits = ["mango", "banana", "apple", "orange", "raspebeery","pera"]
print(fruits)
student = ["student_name", 5, "x@gmail.com"]
print(student)
# slice the lisst 
sliced_fruits = fruits[0:3]
print(sliced_fruits)
copy_fruits = fruits[:] # this is called shallow copy 
print(copy_fruits)
# list is mutable data_type it means you can edit the list 
fruits.append("watermelon")
fruits[2] = "passion_fruit"
print(len(fruits))
print(fruits)


# some programing , fibinocci series
a, b = 0, 1
while a <30:
    a, b = b, a+b
    print(a)
# how the loop works assignment priority 

# test a lanmda

test = lambda x: x + y (3, 4)

def testagain(y):
    result = test
    return lambda x: x + y 

brain = testagain(12)
print(brain(0))






