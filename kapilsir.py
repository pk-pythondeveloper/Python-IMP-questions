# # st="i am prince kumar from indore india"
# # output=["i am prince kumar",'from','indore','india']
# # fst=st.split(' ',4)
# # st = "i am prince kumar from indore india"
# # words = st.split()
# # print(words)

# # # Reverse characters in the first two words
# # first_part = ' '.join(word[::-1] for word in words[:])

# # # Extract the remaining words as separate elements
# # output = [first_part] + words[2:]

# # print(output)


# # print(st)
# # print(fst)
# # sec=st.reverse(split(' ',3))
# # print(sec)

# # sec=st.split(' ',)
# # print(lst)


# # print(lst)
# # ind=lst.index('from')
# # new_lst=[]
# # temp=""
# # for i in range(len(lst)):
# #     if i<ind:
# #         new_lst.append(lst[i])
# #     else:
# #         temp+=lst[i]
# #         temp+=" "

# # new_lst.append(temp)

# # print(new_lst)


# # st="i am prince kumar from indore india"
# # lst=st.split(' ')

# # print(lst)
# # ind=lst.index('from')
# # new_lst=[]
# # temp=""
# # for i in range(len(lst)):
# #     if i<ind:
# #         temp+=lst[i]
# #         temp+=" "
# #     else:
# #         new_lst.append(lst[i])

# # new_lst.insert(0,temp)

# # print(new_lst)

# # st="i am prince kumar from indore india"
# # new=st.split()
# # new.reverse()

# # print(new)

# # st = "i am prince kumar from indore india"
# # words = st.split()

# # # Reverse characters in the first two words
# # first_part = ' '.join(word[::-1] for word in words[:2])

# # # Extract the remaining words as separate elements
# # output = [first_part] + words[2:]

# # print(output)

# # st = "i am prince kumar from indore india"
# # new=st.split()

# # parts = st.split("from")
# # print(parts)

# # output = [parts[0]] +[new[4]] +parts[1].split()

# # print(output)



# lst=[1,2,4,6,5,10,9]
# target=12
# big_lst=[]
# for i in range(len(lst)):
#     temp1=[lst[i]]
#     temp2=[lst[i]]
#     temp3=[lst[i]]
#     sum1=lst[i]
#     sum2=lst[i]
#     sum3=lst[i]
#     for j in range(len(lst)):
#         if i!=j:
#             if sum1%2==0:
#                 if lst[j]%2==0:
#                     temp1.append(lst[j])
#                     sum1=sum1+lst[j]
#                     if sum1==target:
#                         big_lst.append(temp1)
#                         temp1=[lst[i]]
#                         sum1=lst[i]
#             if sum2%2!=0:
#                  if lst[j]%2!=0:
#                     temp2.append(lst[j])
#                     sum2=sum2+lst[j]
#                     if sum2==target:
#                         big_lst.append(temp1)
#                         temp2=[lst[i]]
#                         sum2=lst[i]
#             temp3.append(lst[j])
#             sum3=sum3+(lst[j])
#             if sum3==target:
#                 big_lst.append(temp3)
#                 temp3=[lst[i]]
#                 sum3=lst[i]
# print(big_lst)

# st="-1-100+1-1+1+200"
# temp=""
# for i in range(len(st)):
#     if st[i]== "-" or st[i]=="+":
#         temp+=f" {st[i]}"
#     else:
#         temp+=st[i]
# # print(temp)
# new_st=temp.split()
# print(new_st)
# total=0
# for i in new_st:
#     t=int(i)
#     print(t)
#     total+=t
# print(total)

# str="bb..........."
# str=str.lower()

# def bukket_boll(str):
#     str=str.lower()
#     bucket=""
#     boll=""
#     new_str=""
#     num_of_changege=0
#     for i in str:
#         if i==".":
#             boll+=i
#         elif(i=='b'):
#             bucket+=i
#     if len(boll)==0:
#         return -1
#     if len(bucket)>len(boll)+1:
#         return -1

#     else:
#         for i in range(len(str)):
#             if len(bucket)>i:
#                 new_str+=bucket[i]
#             if len(boll)>i:
#                 new_str+=boll[i]
#         for j in range(len(new_str)):
#             if str[j]!=new_str[j]:
#                 num_of_changege+=1
#         return new_str,num_of_changege
# print(bukket_boll(str))


# ten=[10]
# new_list=[ten*10]
# print(new_list)