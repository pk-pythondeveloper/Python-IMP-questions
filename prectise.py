

# 

# lst=["apple","cup","ram","rrr","uuu","ram"]

# count=0
# for i in range(len(lst)):
#     if lst[i]=="ram":
#         count+=1
#     if count==2:
        
#         print(lst.index(lst[i],i))




# nums="-22+10+11+22"
# total=0
# temp=''
# lst1=[]
# lst2=[]
# temp1=""
# for i in range(len(nums)): 
#     if nums[i]=="-" or nums[i]=="+":
#         lst1.append(nums[i])
#     # elif(i==(len(nums)-1)):
#     #     print('new execution')
#     #     lst2.append(nums[i])
#     elif i<len(nums):
#         if  ("+" not in nums[i:len(nums)]) and ("-" not in nums[i:len(nums)]) :
#             lst2.append(nums[i:len(nums)])
            
#     elif(i==(len(nums)-1)):
#         lst2.append(nums[i])
#     if nums[i]!="-" and nums[i]!="+":
#         if nums[i+1]=="-" or nums[i+1]=="+":
#             temp+=nums[i]
#             lst2.append(temp)
#             temp=""
#         else:
#             temp+=nums[i] 
    
# print(lst1)
# print(lst2)
# if len(lst1)<len(lst2):
#     lst1.insert(0,"+")
# for i in range(len(lst2)):
#     temp1+=lst1[i]
#     temp1+=lst2[i]
#     new=int(temp1)
#     print(new)
#     total+=new
    
#     temp1=""

# print(total)


# lst=[2,3,4,5]
# lst2=[7,9,10]
# lst.extend(lst2)
# print(lst)

# print(dir(str))

# def outer_function():
#     outer_var = "Hello"
#     def inner_function():
#         nonlocal outer_var # Declare outer_var as nonlocal
#         outer_var = "World" # Modify the outer variable
#         print(outer_var) # Print the modified valuep
#     def inerr2():
#         print("this is inner 2",outer_var)

#     inner_function()
#     inerr2()
#     print(outer_var) # Print to show the change

# outer_function()
# Output: World, World
            
        
        
            
            
        

   
    

      

# print(lst1)
# print(lst2)

# def scope_test():
#     def do_local():
#         spam = "local spam"
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#     def do_global():
#         global spam
#         spam = "global spam"
#     spam = "test spam"
#     do_local()
#     print("after local assignment:", spam) 
#     do_nonlocal()
#     print("after nonlocal assignment:", spam)
#     do_global()
#     print("after global assignment:", spam)
# scope_test()
# #do local :-test spam
# #do_nonlocal non localspam
# #global spam
# print("scope_test run",spam)
    

# l2=['a','b','c','a'],cdict={}
# for i in range(len(l2)):

#     dict[l2[i]]=l1[i]
    
    
# print(dict)


# dict={}
# for i in range(len(l2)):

#     dict[l2[i]]=l1[i] 
# print(dict)

# h="hello i am prince"
# temp=h.split()

# for i in range(len(temp)):
#     for j in range(i+1,len(temp)):
#         if len(temp[i])>len(temp[j]):
#             new=temp[j]
#             temp[j]=temp[i]
#             temp[i]=new
# print(temp)

# lst=[1,2,3,4,34,4,6,2,4]
# dict={}
# for i in lst:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1

# # print(dict)
# lst=[]
# for j,k in dict.items():
#     current=[]
#     current.append(i)
#     current.append(j)
#     lst.append(current)
# print(lst)

# new_lst=[ new=lst[i] lst[i]=lst[j] lst[j]=lst[i] if lst[i]<lst[j] for j in range(i+1,len(lst)) for i in range(len(lst))  ] 
# print(new_lst)
# new=0
# lst_compersion={dict[i] for i in range(len(dict)) for j in range(i+i,len(dict)) if dict[i].keys()<dict[j].keys() dict[i],dict[j]=dict[j],dict[i]}
# # print(lst_compersion)
# a=10
# b=20
# a,b=b+a,a

# my_dict ={'a':[5, 8, 7],
#   'b':[4, 7, 2],
#   'c':[2, 2, 4]}

# d = {key: [x if x <= 5 else x + 2 for key,value in  ] for key, value in dict.items()}
# print(d)

# for i in range(dict.values()):
#     print(i)



# print(def dispatch(self, request, *args, **kwargs):
    # return super(ClassName, self).dispatch(request, *args, **kwargs))





    

    




    



