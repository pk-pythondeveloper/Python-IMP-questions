lst=[[1.45,2.46],# 1
     [2.46,4.45],#2
      [4.45,6.14],#3
       [6.11,9.44],
    #     [1.45,4.44], # 1
]

def num_of_used_station(lst):
    count=1
    trains=[lst[0]]
    for i in range(1,len(lst)):
    
        temp=0
        for j in range(len(trains)):
            if trains[j][1]>=lst[i][0]:
                print(trains[j][1],lst[i][0]) 
                print(trains)
                temp+=1
            else:
                trains.remove(trains[j])
                trains.append(lst[i])
                break
        if temp>0:

            trains.append(lst[i])
            print(trains)
            count+=1
    return count
    
            
    
print(num_of_used_station(lst))