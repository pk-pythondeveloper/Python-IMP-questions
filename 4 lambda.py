# result=lambda a,b: a+b
# print(result(20,30))


#using labda print table 


# table=lambda a,b:[print(a * i) for i in range(1,b+1)]
# table(2,10)

# lst=[1,2,3]
# lst2=['a','b','c']
# lst3=zip(lst,lst2)
# for i in lst3:
#     print(i)





def get_man(lst):
    n=len(lst)
    sets=[""]*n
    sets[0]=lst[0]
    l,r=1,n-1
    for i in range(1,n):
        if i%2==1:
            sets[r]=lst[i]
            r-=1
        else:
            sets[l]=lst[i]
            l+=1
    return sets
lst = ["A", "B", "C", "d", "E","f","g","h","i","j"]
print(get_man(lst))

    