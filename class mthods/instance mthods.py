class myclass:
    a=34
    def show(self):
        # nonlocal a we can bind this variable
        
        print(self.a)
    
obj=myclass()
obj.show()