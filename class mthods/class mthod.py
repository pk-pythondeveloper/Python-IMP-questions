# class myclass:
#     a=34
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#     # @classmethod
#     def show():
#         print(cls.a)
    
# obj=myclass("prince","indore")
# myclass.show()
# # obj.show()

class MethodTypes:
    name = "Ragnar"
    def instanceMethod(self,lastname):
        self.lastname = lastname
        self.name="ttttttttttttt"
        print(self.name,'i am printing in class variable  in stancemethod')
        # print(self.lastname,"")
    @classmethod
    def classMethod(cls,m):
        print('---------------------class method -------------')
        print(cls.name)
        print(m.lastname)
        print(cls.name,"class variable is accesing ")
        # cls.name="dddddddddddd"
        print(cls.name)


    # @staticmethod
    # def staticMethod():
    
    #     print("This is a static method")
# Creates an instance of the class
m = MethodTypes()

# Calls instance method
# MethodTypes.name="by using the class name we can update the class variable easyly"
# MethodTypes.classMethod("we passing argument in class mthods")
m.instanceMethod("ramaaaaaaaaa")
# MethodTypes.staticMethod()
MethodTypes.classMethod(m)


# MethodTypes.classMethod()
# MethodTypes.staticMethod()