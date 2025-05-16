class a:
    def __init__(self):
        pass
    def add(self,t,f):
        print("class a mehtod")
        return t+f
class b(a):
    def show(self):
        print("thsi show mehtod")



obj=b()
print(obj.add(13,45))



