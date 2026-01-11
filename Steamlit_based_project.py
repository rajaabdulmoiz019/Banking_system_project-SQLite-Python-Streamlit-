import sqlite3 as st
# import time
import streamlit as sv

conn=st.connect("Database_Banking_system.db")
cursors=conn.cursor()
if 'page' not in sv.session_state:
   sv.session_state.page="Home"
if sv.session_state.page=="Home":
   sv.title("Banking System")
    # print("-------------------------------------BANK MANAGEMENT SYSTEM------------------------------------")

    # print("PRSSS 1 For Account creation")
    # print("PRESS 2 For Balance inquiry")
    # print("PRESS 3 For Transaction")
    # print("PRESS  For Exiting")
    # print()
    # print("="*50)
    
    
   sv.subheader("Select operation")
   choose=sv.selectbox("",["Account creation","Balance inquirry","Transaction"])
   if sv.button("Select"):
      sv.session_state.page=choose
      sv.rerun()

           

   #  match choose:
   #      case "Account creation":
elif sv.session_state.page=="Account creation":
             sv.title("Account creation")
             id=sv.number_input("Enter the ID")
             name=sv.text_input("Enetr your name")
             date=sv.date_input("Enetr Date")
             if sv.button("Create Account"):
                 try:
                     cursors.execute("""insert into Customer_data(Card_ID,"Name","Date")VALUES
                            (?,?,?)""",(id,name,str(date,),))
                     starting=(100000)
                     cursors.execute("""insert into Balance(Card_ID,balance)VALUES
                             (?,?)""",(id,starting,))
                     conn.commit()
                     sv.write("Account created successfully🎇✨🎈🎊")
                 except:
                     sv.error("INvalid")
              
            # id=int(input("Enter your id :"))
            # if id==0:
            #    break
            # else:
            #  name=input("Enter your name :")
            #  date=input("Enter Today's DATE :")
            #  print("Creating Account  ....")
            #  print("Please wait  ....")
            #  time.sleep(1.5)
            #  print("--------------Acount created Succesfully----------")
            #  print("✨✨🎇✨🎉🎊🎉✨🎆🎈")
            #  time.sleep(1.5)
             #while True:
            #   print("="*50)
            #   print("SElect operation ")
            #   print("Withdraw =1 ")
            #   print("Deposit =2")
            #   print("Program end =0")
            #   print("="*50)
             
             option=sv.selectbox("Select process to perform",["Withdraw","Deposit"])
             amounts=sv.number_input("Enetr amount")
                           # break
              
            #  amounts=int(input("Enter the amount:"))
             
             match option:
                  case "Withdraw":
                    def Withdraw_amont(amount):
                       cursors.execute("update Balance set balance=balance-? where Card_ID=?",(amount,id,))
                       conn.commit()
                    withdraw=Withdraw_amont(amounts)
                    if sv.button("Done"):
                     sv.text(f"{amounts} succesfully Withdrawal")
                     
                                  

                  #   print(f"{amounts} Succesfully Withdrawal")
                    
                  case "Deposit":
                    def deposit_amount(amount):
                       cursors.execute("update Balance set balance=balance+? where Card_ID=?",(amount,id,))
                       conn.commit()
                    deposit=deposit_amount(amounts)
                    if sv.button("Done"):
                     sv.text(f"{amounts} Succesfully Deposited")
                     
             if sv.button("Back to Home"):
              sv.session_state.page="Home"
              sv.rerun()
                    
             
                   # break
elif sv.session_state.page=="Balance inquirry":
    sv.title("Balance Inquirry")

        
             
              

      #   case "Balance inquirry":
      #     print("---------------BALANCE INQUIRRY-----------------")
    id=sv.number_input("Enter ID ")
    cursors.execute("""select c.Card_ID,c.Name,b.balance from Customer_data as c INNER JOIN Balance as b on c.Card_ID=b.Card_ID Where c.Card_ID=?""",(id,))
    data=cursors.fetchone()
    if data==None:
      sv.error("INVALID INPUT !")
    else:
      sv.write(data)
    if sv.button("Back to Home"):
              sv.session_state.page="Home"
              sv.rerun()


elif sv.session_state.page=="Transaction":
        
         #  print("---------------------Authentication-------------------")
          id=sv.number_input("Enter ID")
    
    # This keeps the section open after 'Enter' is clicked
          cursors.execute("""select * from Customer_data where Card_ID=?""",(id,))
          data=cursors.fetchone()
        
          if data==None:
            sv.Error("Please register yourself !")
            #  time.sleep(1.5)
            #  print("---You are not Registred Please Register yourself ---")
          else:
                None
            # time.sleep(2)
            # print("Access Granted!")
            # time.sleep(1.5)
         #   while True:
         #      print("SElect operation ")
         #      time.sleep(1)
         #      print("Withdraw =1 ")
         #      time.sleep(1)
         #      print("Deposit =2")
         #      print("Program End =0")
         #      print("="*50)
          option=sv.selectbox("Select process to perform",["Withdraw","Deposit"])
          amounts=sv.number_input("Enetr amount")
                           # break
              
            #  amounts=int(input("Enter the amount:"))
             
          match option:
               case "Withdraw":
                    def Withdraw_amont(amount):
                       cursors.execute("update Balance set balance=balance-? where Card_ID=?",(amount,id,))
                       conn.commit()
                    withdraw=Withdraw_amont(amounts)
                    if sv.button("Done"):
                     sv.text(f"{amounts} succesfully Withdrawal")

                  #   print(f"{amounts} Succesfully Withdrawal")
                    
               case "Deposit":
                    def deposit_amount(amount):
                       cursors.execute("update Balance set balance=balance+? where Card_ID=?",(amount,id,))
                       conn.commit()
                    deposit=deposit_amount(amounts)
                    if sv.button("Done"):
                     sv.text(f"{amounts} Succesfully Deposited")
               case _:
                    sv.write("INVALID INPUT!")
          if sv.button("Back to Home"):
              sv.session_state.page="Home"
              sv.rerun()
             
                   # break
      #         option=int(input("Eneter operation :"))
      #         if option==0:
      #            break
      #         else:
      #          amounts=int(input("Enter the amount:"))
      #          match option:
      #             case 1:
      #                def Withdraw_amont(amount):
      #                   cursors.execute("update Balance set balance=balance-? where Card_ID=?",(amount,id,))
      #                   conn.commit()
      #                withdraw=Withdraw_amont(amounts)
      #                print(f"{amounts} Succesfully Withdrawal")
                    
      #             case 2:
      #                def deposit_amount(amount):
      #                   cursors.execute("update Balance set balance=balance+? where Card_ID=?",(amount,id,))
      #                   conn.commit()
      #                deposit=deposit_amount(amounts)
      #                print(f"{amounts} Succesfully Deposited")
      #             case _:
      #                raise ValueError("INVALID INPUT!")
          
          
      #   case "Exiting":
      #     print("exit")         
                    
                      
                      
                      
                      
                      
                      


        




        