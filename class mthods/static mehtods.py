class show:
    name="ramama"
    def __init__(self,lastname):
        self.lastname=lastname
    @staticmethod
    def staticMethod(obj,address):
        print(show.name)#using the class name we can access the class variable
        print(obj.lastname)#by passing the object we can access instance variable also
        print(address)
obj=show("radha ")
show.staticMethod(obj,"Indore")

