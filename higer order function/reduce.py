from functools  import reduce
def apply_reduce(a,b):
    print(a)
    print(b)
    return a+b
lst=[10,24,56,5]
new_list=reduce(apply_reduce,lst)

print(new_list)
#using lambda
# lst=[1,2,4,56,5]

# new_lst=reduce(lambda a,b:a+b,lst)
# print(new_lst)