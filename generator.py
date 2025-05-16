#In Python, a generator is a special type of function that produces a sequence of values, 
# yielding one at a time, rather than storing them all in memory at once, using the yield keyword. 

#noraml function
# def get_square(n):
#     for i in range(1,n):
#         print(i*i)
        
# print(get_square(6))\

#get squre using generator
# def get_square(n):
#     for i in range(n):
#         yield i*i
# n=get_square(6)
# for value in n: 
#         print(value)



def simple_generator():
    for i in range(1, 6):
        # yield i  # Yield returns a value and pauses the function
        # print(type(i))
#Using the generator
        yield i
gen = simple_generator()



# # for num in gen:
# #     print(num)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
# print(gen.__next__())

