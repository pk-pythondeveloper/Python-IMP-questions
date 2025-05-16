# print(-22+10+11+1)
# str="prince"
# print(str[2:2])



# nums="-10+
# total=0
# temp=''
# lst1=[]
# lst2=[]
# temp1=""

# for i in range(len(nums)-1): 
#     if nums[i]=="-" or nums[i]=="+" or nums[i]=="*" or nums[i]=="/":
#         lst1.append(nums[i])
#     if nums[i]!="-" and nums[i]!="+" and nums[i]!="*" and nums[i]!="/":
#         if nums[i+1]=="-" or nums[i+1]=="+" or nums[i+1]=="*" or nums[i+1]=="/":
#             temp+=nums[i]
#             lst2.append(temp)
#             temp=""
            
#         else:
#             temp+=nums[i] 
#     elif  "+" and  "-" and "*" and "/" not in nums[i:len(nums)]:
#         print("nahi  chal raha he")
#         lst2.append(nums[i+1:len(nums)])
            
# print(lst1)
# print(lst2)
# if len(lst1)<len(lst2):
#     lst1.insert(0,"+")
# for i in range(len(lst2)):
#     temp1+=lst1[i]
#     temp1+=lst2[i]
#     new=int(temp1)
#     total+=new
#     temp1=""

# print(total)

# a=5
# print(f"{a}")

s="11112222333"
dict={}
for i in s:
    temp=s.count(i)
    if i not in dict:
        dict.update({i:temp})
    
print(dict)
    

# dict={}
# dict.update({"1":"3"})
# dict.update({"1":"3"})
# print(dict)