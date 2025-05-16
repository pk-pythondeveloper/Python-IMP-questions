#what is exception handling 
#ans:-At the time of code exception prevent from code crase you hav eneed to handle exception
'''
try :- it test the code
except:- it handle execption
else:- it execute when error not  occured
finally :- it execute at any way

'''


'''
what is raise keyword ?
and:- it is used to raise execption if conndition occures
'''


# def add(a,b):
#     if a/b !=5:
#         raise Exception("answer should be only 5")

# add(10,23)
# def age_checker(age):
#     try:
#         if age<21:
#             raise Exception("you are under age")
#         else:
#             print("yuou are good for the age")
#     except TypeError:
#         print('plese given only int value')
#     else:
#         print("this is else block")
 
    
#     finally:
#         print("this is finally block ")
# age_checker(23)


# def division(a,b):
#     try:
#         a/b

# try:
#   print("Hello")
# else:
#   print("Nothing went wrong")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#     raise TypeError('bad type')
# except Exception as e:
#     e.add_note('Add some information')
#     e.add_note('you add some information')
#     raise
# def fun():
#     try:
#         # breakpoint()
#         a=10
#         # a=10
#         b=0
#         c=a/b
#     # except  ZeroDivisionError as e:
#     #     print('you can divide with zero',e)
#     except:
#         b=2

    
#     else:
#         print("this is else")
#     finally:
#         print("this is finally")

# print(fun())