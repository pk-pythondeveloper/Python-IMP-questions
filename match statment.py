#if the case is not matched it reteurn None

# def error_checker(status,status2):
#     match status,status2:
#         case if(status)>(status2):
#             print("this case 404")
#             return "not allowed"
#         case 400:
#             return "url mismatch"
#             # break
#         case 400:
#             return "bad request"
#         case ram:
#             raise ValueError("Not a point")
        

# print(error_checker(400,404))

#we can also applied condition    
# def check(point)    
# match point:
#     case Point(x, y) if x == y:
#         print(f"Y=X at {x}")
#     case Point(x, y):
#         print(f"Not on the diagonal")



def manage_seating(persons):
    n = len(persons)
    chairs = [''] * n
    chairs[0] = persons[0]
    left, right = 1, n - 1
    for i in range(1, n):
        if i % 2 == 1:
            chairs[right] = persons[i]
            right -= 1
        else:
            chairs[left] = persons[i]
            left += 1
    return chairs
persons = ["Person 1", "Person 2", "Person 3", "Person 4", "Person 5"]
seating = manage_seating(persons)
print(seating)