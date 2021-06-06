# if condition ! 

x = int(input("please enter an integer: "))
# the condition to detect a value below zero 
if x<0:   
    x = 0
    print("the negative integer changed to zero")

elif x == 5:
    print("it's five !!") 

elif x<10:
    print("number entered is below 10")

else:
    print("number enterd is above 10 ")

 #Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence
# for loop 

words = ['cat', 'window', 'defenestrate']
for word in words:
    print(word , len(word))

for word in words:
    if word == 'window':
        print(word)


# update a list or string, dictionary or collection loop while running through it , Code that modifies a collection while iterating over that same collection 

new_words = []
for word in words:
    keyword = word + 's'
    new_words.append(keyword)
print(new_words)      

# range in python 

#for i in range(10):
    #print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
#for i in range(len(a)):
    #print(i , a[i])

# check that the number is prime or not , if it is prime it can be factor into smaller numbers eg. 5 , but 4 can be factored 2*2
# use of break statement 

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, "it's a prime number")        

for n in range(2, 10):
    if n % 2  == 0:
        print(n , "found a even number")
        continue 
    print(n, "found an odd number")                   
    
        
            
            
  
            
       

    
   


    
    

    