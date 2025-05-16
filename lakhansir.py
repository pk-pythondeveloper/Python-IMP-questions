# lst=[1,[2,[3,4],5],6]
# print(lst)
# new_lst=[]
# for i in lst:
#     if type(i)==list:
#         for j in i:
#             if type(j)==list:
#                 for k in j:
#                     if type(k)==list:
#                         for l in k:
#                             lst.append(l)
#                     else:
#                         new_lst.append(k)
#             else:
#                 new_lst.append(j)
#     else:
#         new_lst.append(i)

# print(new_lst)
# lst2=[-2,1,-3,4,-1,2,1,-5,4]
# max=0
# for i in range(len(lst2)):
#     for j in range(len(lst2)):
#         if lst2.index(lst2[i])!=lst2.index(lst2[j]):
#             temp=lst2[i]+lst2[j]
#             if temp>max:
#                 max=temp

    
# print(max)

# st="hello jyouuuuuuuuuuu are annamika how are you"
# new=st.split(' ')
# print(new)
# longest=new[0]
# for i in new:
#     if len(i)>len(longest):
#         longest=i
# print(longest)

st="leet*cod*e"

output=[]
new=''

for i in range(len(st)):
    if i==0:
        if st[i]=="*":
            pass
        else:
            output.append(st[i])
    elif(st[i]=="*"):
        output.pop()
    else:
        output.append(st[i])

for j in output:
    new+=j

print(new)