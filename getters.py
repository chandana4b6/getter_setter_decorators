# class bank:
#     def __init__(self):
#         self.bal=5000


#     def get_bal(self): # getter
#         return self.bal
    

#     def set_bal(self,reAmount):
#         if reAmount<0:
#             print("pls enter +ve values")
#         else:
#             self.bal+=reAmount
#             print(self.bal)
# obj=bank()
# print(obj.bal)



class bank:
    def __init__(self):
        self.balance=5000

    @property
    def bal(self): # getter
        return self.balance
    
    @bal.setter
    def bal(self,reAmount):
        if reAmount<0:
            print("pls enter +ve values")
        else:
            self.balance+=reAmount
            print(self.balance)
obj=bank()
print(obj.bal)# getter 
obj.bal=10000 # setter
