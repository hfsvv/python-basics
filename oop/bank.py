
from datetime import datetime
class bank:
    banknname="sbi"#static variable or class variable
    def __init__(self,name,accno,balance):
        self.pname=name
        self.accno=accno

        self.blc=balance
    def deposit(self,amt):
        self.blc+=amt
        print(bank.banknname,"Your acc ",self.accno,"has been credited with",amt,"on",datetime.today(),"avl balance",self.blc)
    def withdrawal(self,amt):
        if self.blc>amt:
            self.blc-=amt
            print(bank.banknname,"Your acc ",self.accno,"has been debited with",amt,"on",datetime.today(),"avl balance",self.blc)
        else:
            print("Transaction cancelled with error code")
    def bal_enq(self):
        print(self.blc)
obj=bank("febin",1000,1000)
obj.withdrawal(100)




#diff type of variables
