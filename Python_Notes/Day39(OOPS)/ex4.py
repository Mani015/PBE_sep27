
# A class is a user-defined blueprint or prototype from which objects are created.
# Classes provide a means of bundling data and functionality together.
# Creating a new class creates a new type of object,


class LapTop:
    def __init__(self,Lmodel,Lprice,Lcolor,Lram,Lssd):
        self.model = Lmodel
        self.price = Lprice
        self.color = Lcolor
        self.ram = Lram
        self.ssd = Lssd

    def Show(self): #Insatnce method
        print(
            self.model,self.price,self.color,self.ram,self.ssd
        )
    def Incrementprice(self,newprice):  #Instance method
        self.price+= newprice

    def Decrementprice(self,newprice):
        self.price = self.price - newprice


ob1 = LapTop('Dell',40000,'black',str(16)+'GB' ,512)
ob1.Show()
# Dell 40000 black 16GB 512
ob1.Incrementprice(5000)
ob1.Show()
# Dell 45000 black 16GB 512


ob1.Decrementprice(10000)
ob1.Show()
# Dell 35000 black 16GB 512


