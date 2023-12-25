class bankatm:
    bal=5000
def login(self,pin):
    if pin==1234:
        return True
    else:
        return False
def credit(self,amt):
    self.bal+=amt
def debit(self,amt):
    self.bal-=amt
def show(self):
    print("the current balance is "+str(self.bal)) obj=bankatm()
    if obj.login(int(input("enter the pin"))):
    while True:
        o=input("C for credit \n d for debit \n b for balance \n e for exit")
    if o=='c' or o=='C':
        obj.credit(int(input("enter the amount"))) print("after credit balance is")
        obj.show()
    elif o=='d' or o=="D":
        amt=int(input("enter the amount"))
    if amt<=obj.bal: obj.debit(amt)
        print("debit amount is balance is") obj.show()
    else:
        printf("invalid amount") obj.show()
    elif o=='b' or o=="B":
        print("the balance is",obj.show())
    elif o=="e" or o=='E':
        break
    else:
        print("Invalid pin")
