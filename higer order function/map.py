#map using normal function

# def incriment(a):
#     return a+10
lst=[13,20,40,59,67]


# new_lst=list(map(incriment,lst))
# print(new_lst)

new_lst=list(map(lambda a:a+30,lst))

print(new_lst)