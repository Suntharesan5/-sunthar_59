dic = {}
x=open(r"C:\Users\ELCOT\Desktop\filehandling4.txt","r")
y=x.readlines()
print(y)

class RBI:
    def __init__(self):
        self.current_balanance1 = 90000
        self.current_account1 = 15


class SBI(RBI):
    def __init__(self):
        self.current_balanance2= 75000
        self.current_account2 = 9
        super().__init__()

class TN(SBI):
    def __init__(self):
        self.current_balanance3=30000
        self.current_account3=5
        super().__init__()

class AD(TN):
    def __init__(self,totalfun4,noaccount4):
        self.current_balanance4 = totalfun4
        self.current_account4 = noaccount4
        print("BANK MANAGEMENT")
        print("-----*----*----")
        print("     1.CREDIT AMOUNT AND ADD ACCOUNT..")
        print("     2.DEBIT AMOUNT AND DELETE ACCOUNT..")

        while choose:=int(input("Enter 1 0r 2:")):

            if choose == 1:

                print("ADYAR CURRENT BANK AMOUNT :",str(self.current_balanance4))
                print("ADYAR CURRENT NO OF ACCONUTS :",str(self.current_account4))
                totfund4 = int(input("Enter the Total fund Amount:"))
                noofacc4 = int(input("Enter the Accounts to add:"))
                total5=totfund4+self.current_balanance4
                account5=noofacc4+self.current_account4
                print("ADYAR Current  ADD AND DEPOSIT Status")
                print("=====================================")
                print(total5)
                print(account5)
                dic.setdefault("ad", [total5, account5])

                super().__init__()
                print("TN BANK RESULT")
                total6 = totfund4 + self.current_balanance3
                account6 = noofacc4 + self.current_account3
                print(total6)
                print(account6)
                dic.setdefault("tn", [total6, account6])

                print("SBI BANK RESULT")
                total7 = totfund4 + self.current_balanance2
                account7 = noofacc4 + self.current_account2
                print(total7)
                print(account7)
                dic.setdefault("sbi", [total7, account7])

                print("RBI BANK RESULT")
                total8 = totfund4 + self.current_balanance1
                account8= noofacc4 + self.current_account1
                print(total8)
                print(account8)
                dic.setdefault("rbi", [total8, account8])

            elif choose==2:
                print("ADYAR CURRENT BANK AMOUNT :", str(self.current_balanance4))
                print("ADYAR CURRENT NO OF ACCONUTS :", str(self.current_account4))
                totfund4 = int(input("Enter the  Withdraw Amount:"))
                noofacc4 = int(input("Enter the  deleted accounts:"))
                total5 =  self.current_balanance4-totfund4
                account5 =   self.current_account4-noofacc4
                print("ADYAR Current Remove and Withdraw  Status")
                print("=========================================")
                print(total5)
                print(account5)
                dic.setdefault("ad", [total5, account5])
                super().__init__()

                print("TN BANK RESULT")
                total6 =  self.current_balanance3-totfund4
                account6 = self.current_account3-noofacc4
                print(total6)
                print(account6)
                dic.setdefault("tn", [total6, account6])

                print("SBI BANK RESULT")
                total7 =self.current_balanance2-totfund4
                account7 =self.current_account2-noofacc4
                print(total7)
                print(account7)
                dic.setdefault("sbi", [total7, account7])

                print("RBI BANK RESULT")
                total8 =self.current_balanance1-totfund4
                account8 = self.current_account1-noofacc4
                print(total8)
                print(account8)
                dic.setdefault("rbi", [total8, account8])




            else:
                print("Not valid no...")
                break


A=AD(10000,10)
fil = open(r"C:\Users\ELCOT\Desktop\filehandling4.txt","a")
fil.write(str(dic)+'\n')
fil.close()

# print(A.__dict__)



# print(A.noofacc)
# print(A.totfund)

# class RBI:
#     def __init__(self):
#          self.totalfunds=20000
#          self.accounts=20
#
# class SBI(RBI):
#      def __init__(self):
#         self.totalfunds2=10000
#         self.accounts2=10
#         super().__init__()
# class TN(SBI):
#     def __init__(self):
#         self.totalfunds3 =3000
#         self.accounts3 =5
#         super().__init__()
# class AD(TN):
#     def __init__(self):
#         self.totalfunds4 =2500
#         self.accounts4 =3
#         print("current totalfunds in AD bank")
#         print("cureent accounts in AD bank")
#         i = int(input("enter the value"))
#         totalfund=int(input("enter the totalfund"))
#         account=int(input("enter the accounts"))
#         if i==0:
#                obj1=self.totalfunds4+totalfund
#                obj2=self.accounts4+account
#                print(obj1)
#                print(obj2)
#                super().__init__()
#                obj3 = self.totalfunds3 + totalfund
#                obj4 = self.accounts3 + account
#                print(obj3)
#                print(obj4)
#                obj5 = self.totalfunds2 + totalfund
#                obj6 = self.accounts2 + account
#                print(obj5)
#                print(obj6)
#                obj7 = self.totalfunds + totalfund
#                obj8 = self.accounts + account
#                print(obj7)
#                print(obj8)
#
#         else :
#                obj1 = self.totalfunds4 - totalfund
#                obj2 = self.accounts4 - account
#                print(obj1)
#                print(obj2)
#                super().__init__()
#                obj3 = self.totalfunds3 - totalfund
#                obj4 = self.accounts3 - account
#                print(obj3)
#                print(obj4)
#                obj5 = self.totalfunds2 - totalfund
#                obj6 = self.accounts2 - account
#                print(obj5)
#                print(obj6)
#                obj7 = self.totalfunds - totalfund
#                obj8 = self.accounts - account
#                print(obj7)
#                print(obj8)
#
# sam=AD()







# class RBI:
#     def __init__(self):
#          self.totalfunds=20000
#          self.accounts=20
#
# class SBI(RBI):
#     def __init__(self):
#         self.totalfunds2=10000
#         self.accounts2=10
#         super().__init__()
# class TN(SBI):
#     def __init__(self):
#         self.totalfunds3 =3000
#         self.accounts3 =5
#         super().__init__()
# class AD(TN):
#     def __init__(self):
#         self.totalfunds4 =2500
#         self.accounts4 =3
#         print("current totalfunds in AD bank")
#         print("cureent accounts in AD bank")
#         print(self.totalfunds4)
#         print(self.accounts4)
#         totalfund=int(input("enter the totalfund"))
#         account=int(input("enter the accounts"))
#         if self.totalfunds4>=0:
#            obj1=self.totalfunds4+totalfund
#            obj2=self.accounts4+account
#            print(obj1)
#            print(obj2)
#            super().__init__()
#            obj3 = self.totalfunds3 + totalfund
#            obj4 = self.accounts3 + account
#            print(obj3)
#            print(obj4)
#            obj5 = self.totalfunds2 + totalfund
#            obj6 = self.accounts2 + account
#            print(obj5)
#            print(obj6)
#            obj7 = self.totalfunds + totalfund
#            obj8 = self.accounts + account
#            print(obj7)
#            print(obj8)

#         else:
#            while True:
#                if 1==0:
#                    obj1 = self.totalfunds4 - totalfund
#                    obj2 = self.accounts4 - account
#                    print(obj1)
#                    print(obj2)
#                    super().__init__()
#                    obj3 = self.totalfunds3 - totalfund
#                    obj4 = self.accounts - account
#                    print(obj3)
#                    print(obj4)
#                    obj5 = self.totalfunds3 - totalfund
#                    obj6 = self.accounts3 - account
#                    print(obj5)
#                    print(obj6)
#                    obj7 = self.totalfunds2 - totalfund
#                    obj8 = self.accounts2 - account
#                    print(obj7)
#                    print(obj8)
# obj=AD()

