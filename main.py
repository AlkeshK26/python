import json
import random
import string
from  pathlib import Path

class Bank:
    database  = 'data.json'
    data = []
     
    try:
      if Path(database).exists():
         with open(database) as fs:
            data = json.loads(fs.read())
      else:
         print("no such file exists")

    except Exception as err:
       print(f" an exception occured as {err}")     
              

    @classmethod 
    def __update(cls) :
       with open(cls.database,'w') as fs:
          fs.write(json.dumps(Bank.data))
        
    @classmethod
    def __accountgenerate(cls):
       alpha =  random.choices(string.ascii_letters, k = 3)
       num = random.choices(string.digits, k=3)
       spchar= random.choices("!@#$%^&*", k = 1)
       id = alpha + num + spchar 
       random.shuffle(id)
       return "".join(id)
    


    def Createaccount(self):
       info = {
          "name": input("Enter Your Name = "),
          "age": int(input("Enter Your age = ")),
          "email": input("Enter Your email = "),
          "pin": int(input("Enter Your  4 digit Pin = ")),
           "accountNo": Bank.__accountgenerate(),
           "balance" : 0

       }

       if info['age'] < 18 or len(str(info['pin'])) != 4:
          print("Sorry yoy cant create your account")
       else:
          print("account has been created successfully")
          for i in info:
             print(f"{i} : {info[i]}")   
          print("please note down your account no. ")   

          Bank.data.append(info)

          Bank.__update()

    

    def depositemoney(self):
       accnumber = input("pLease Enter uyour account number")
       pin = int (input( "please Enter your pin as well"))

       userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

       if userdata == False:
          print ("sorry no data found")
                 
       else:
             amount = int (input("how much amount yoy want to deposit "))
             if amount > 10000 or amount < 0:
                print ("Sorry the amount is too much you can deposti below 10000 and above 0 ")

             else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully")



    def withdearmoney(self):
        accnumber = input("pLease Enter uyour account number")
        pin = int (input( "please Enter your pin as well"))
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
      
        if userdata == False:
          print ("sorry no data found")

        else:
           amount = int(input("how much amount you want to withdraw")) 
           if userdata [0]['balance'] < amount :
              print("sorry you dont have this much amount")

           else:

                userdata[0]['balance'] -= amount
                Bank.__update()
                print ( " Amount with draw Successfully")

    def showdetails(self):

        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        print("Ypur information are\n\n")

        for i in userdata[0]:
           print(f" {i} : {userdata[0][i]}")
    

    def updatedetails(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("no such user found ")

        else:
           print("you cannot change the age, account number, balance")
           print("Fill the details for change or leave it empty if no change")


           newdata = {
               "name": input("please tell new name or press enter : "),
                "email":input("please tell your new Email or press enter to skip :"),
                "pin": input("enter new Pin or press enter to skip: ")

           }

           if newdata[" name"] == "":
              newdata["name"] = userdata[0]["name"]
           if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
           if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
                newdata['age'] = userdata[0]['age']

                newdata['accountNo'] = userdata[0]['accountNo.']
                newdata['balance'] = userdata[0]['balance']
            
                if type(newdata['pin']) == str:
                  newdata['pin'] = int(newdata['pin'])
            
        for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

                 Bank.__update()
                 print("details updated successfully")



    def Delete(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("sorry no such data exist ")
            
        else:
            check = input("press y if you actually want to delete the account or press n")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully ")
                Bank.__update()




user = Bank()

user = Bank()
print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response :- "))



if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.Delete()