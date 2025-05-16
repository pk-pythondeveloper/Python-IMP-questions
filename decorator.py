

# def outer(somthing):
#     def inner():
#         print("welcome prince ")
#     # return inner
#     print(f"{inner}")
    
#     def welcom():
#         # breakpoint()
#         print("welcome !!")
#     # return welcom

#     return welcom

#     welcom()

# @outer
# def welcome():
#     # breakpoint()
#     print("welcome !!")

# welcome()

# def admin_only(f):
   
#     # print('call ho raha')
#     def inner(user):
#         print('andar aa raha')
#         if user != "admin":
#             return print("access denied")

#         return inner
#     return inner
# @admin_only
# def access_data(user):
#     print(f"Welcome {user}, access granted")
# print('-----------idhar aa raha--------')
# access_data("guest")
# access_data("admin")


# s = "admin"
# print(admin_only(s))
# React

# Reply

# 5:28
# def decor(printer,a):

#     def inner(a):
#         a=45
#         # printer()
#         # add new functionalities
#         print("welcome!!",a)
#     return inner
# def printer(a):
#     print("welcome!")

# inner = decor(printer)
# inner()



# def ab():
#     return "ab"

# def bc():
#     return ab

# print(bc())

# def outer():
#     def inner():
#         print("Hello from inner!")

#     return inner  # Returning function reference

# f = outer()  # Now, f is inner()
# f()  # Calls inner()










# def decor(printer):
#     def inner(a,b):
        
        
#         print("welcome!!",a+b)
#         printer(a,b)
#     return inner

# def printer(a,b):
#     print(a*b)

# inner=decor(printer)
# idef nner(45,45)

# f
def fun(a):
    def inner():
    
        print("hello")
        a()
        print("world")
        
    return inner
@fun
def a():
    print('manisha')
a()