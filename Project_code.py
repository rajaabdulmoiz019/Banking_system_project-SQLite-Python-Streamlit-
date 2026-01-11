import sqlite3 as st
import time


conn=st.connect("Database_Banking_system.db")
cursors=conn.cursor()
while True:
    print("-------------------------------------BANK MANAGEMENT SYSTEM------------------------------------")

    print("PRSSS 1 For Account creation")
    print("PRESS 2 For Balance inquiry")
    print("PRESS 3 For Transaction")
    print("PRESS  For Exiting")
    print()
    print("="*50)
    choose=int(input("Select Operation :"))
    match choose:
        case 1:
            id=int(input("Enter your id :"))
            if id==0:
               break
            else:
             name=input("Enter your name :")
             date=input("Enter Today's DATE :")
             print("Creating Account  ....")
             print("Please wait  ....")
             time.sleep(1.5)
             print("--------------Account created Succesfully----------")
             print("✨✨🎇✨🎉🎊🎉✨🎆🎈")

             cursors.execute("""insert into Customer_data(Card_ID,"Name","Date")VALUES
                            (?,?,?)""",(id,name,date,))
             starting=(100000)
             cursors.execute("""insert into Balance(Card_ID,balance)VALUES
                             (?,?)""",(id,starting,))
             conn.commit()
             time.sleep(1.5)
            while True:
             print("="*50)
             print("SElect operation ")
             print("Withdraw =1 ")
             print("Deposit =2")
             print("Program end =0")
             print("="*50)
             option=int(input("Eneter operation :"))
             if option==0:
                break
             else:
              amounts=int(input("Enter the amount:"))
              match option:
                 case 1:
                    def Withdraw_amont(amount):
                       cursors.execute("update Balance set balance=balance-? where Card_ID=?",(amount,id,))
                       conn.commit()
                    withdraw=Withdraw_amont(amounts)
                    print(f"{amounts} Succesfully Withdrawal")
                    
                 case 2:
                    def deposit_amount(amount):
                       cursors.execute("update Balance set balance=balance+? where Card_ID=?",(amount,id,))
                       conn.commit()
                    deposit=deposit_amount(amounts)
                    print(f"{amounts} Succesfully Deposited")
                 case _:
                    raise ValueError("INVALID INPUT!")
        case 2:
          print("---------------BALANCE INQUIRRY-----------------")
          id=int(input("Enetr the Card_ID :"))
          cursors.execute("""select c.Card_ID,c.Name,b.balance from Customer_data as c INNER JOIN Balance as b on c.Card_ID=b.Card_ID Where c.Card_ID=?""",(id,))
          data=cursors.fetchone()
          if data==None:
             print("INVALID INPUT !")
          else:
           print(data)
        case 3:
          print("---------------------Authentication-------------------")
          id=int(input("Enter Card_Id :"))
          cursors.execute("""select * from Customer_data where Card_ID=?""",(id,))
          data=cursors.fetchone()
          if data==None:
             print("Searching......")
             time.sleep(1.5)
             print("---You are not Registred Please Register yourself ---")
          else:
           print("Processing.......")
           time.sleep(2)
           print("Access Granted!")
           time.sleep(1.5)
           while True:
              print("SElect operation ")
              time.sleep(1)
              print("Withdraw =1 ")
              time.sleep(1)
              print("Deposit =2")
              print("Program End =0")
              print("="*50)
              option=int(input("Eneter operation :"))
              if option==0:
                 break
              else:
               amounts=int(input("Enter the amount:"))
               match option:
                  case 1:
                     def Withdraw_amont(amount):
                        cursors.execute("update Balance set balance=balance-? where Card_ID=?",(amount,id,))
                        conn.commit()
                     withdraw=Withdraw_amont(amounts)
                     print(f"{amounts} Succesfully Withdrawal")
                    
                  case 2:
                     def deposit_amount(amount):
                        cursors.execute("update Balance set balance=balance+? where Card_ID=?",(amount,id,))
                        conn.commit()
                     deposit=deposit_amount(amounts)
                     print(f"{amounts} Succesfully Deposited")
                  case _:
                     raise ValueError("INVALID INPUT!")
          
          
        case _:
          print("exit")         
                    
                      
                      
                      
                      
                      
                      


        




        