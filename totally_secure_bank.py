import csv
import random
import os
def options():
    print("""Options:
1. Insert details of a new account (with a starting balance amount)
2. Delete an account for a given account number
3. Print the account details of a given account using the account number
4.  Withdraw some amount from a given account number (ensure the required
balance is present before withdrawal, otherwise decline the withdrawal)
5.  Deposit an amount into a given account
6. Update phone number of a given account
7. quit
""")
def new_file():
    a = open("new.csv","w")
    a.close()
a = True

while a == True:
    options()
    act = int(input("input a number between 1 and 7: "))
    if act >0 and act<8:
#insert
        if act==1:
            name = input("enter name: ")
            mobile = input("enter mobile number: ")
            balance = input("enter amount: ")
            def unique_no():
                z = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
                return z
            y = unique_no()
            file2 = open("unique.txt","a")
            file_2 = open("unique.txt","r")
            z = file_2.readlines()
            for x in z:
                x = x.strip()
                if x == y:
                    y = unique_no()
                    continue
            with open('bank_main.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([y,mobile,balance,name])


#close
        if act==7:
            a = False
            
            
                        
#delete            
        if act == 2:
             delete_no = input("enter bank account number to be deleted: ")
             new_file()
             with open('bank_main.csv', 'r') as file:
                 reader = csv.reader(file)
                 for row in reader:
                     if row == []:
                         pass
                     else:
                         if row[0] == delete_no:
                             pass
                         else:
                             with open('new.csv', 'a') as file:
                                 writer = csv.writer(file)
                                 writer.writerow([row[0],row[1],row[2],row[3]])
             os.remove(r"bank_main.csv")
             os.rename(r"new.csv",r"bank_main.csv")



#details print
        if act == 3:
            acc_no = input("account number: ")
            with open('bank_main.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row == []:
                        pass
                    else:
                        if row[0] == acc_no:
                            print(row)
                            break
        
        
        if act == 4:
            
            uid = input("Enter your A/c Number: ")
            cash = float(input("Enter amount: "))
            with open("bank_main.csv", "r") as reader, open("new.csv", 'w+') as writer:
                reader = csv.reader(reader)
                writer = csv.writer(writer)
                for i in reader:
                    if i!= []:
                        if uid == i[0]:
                            cash -= float(i[2])
                            writer.writerow([uid, i[1], cash,i[3] ])
                        else:
                            writer.writerow(i)
                        
            os.remove(r"bank_main.csv")
            os.rename(r"new.csv", r"bank_main.csv")
#add amount
        


        if act == 5:
            uid = input("Enter your A/c Number: ")
            cash = float(input("Enter amount: "))
            with open("bank_main.csv", "r") as reader, open("new.csv", 'w+') as writer:
                reader = csv.reader(reader)
                writer = csv.writer(writer)
                for i in reader:
                    if i!= []:
                        if uid == i[0]:
                            cash += float(i[2])
                            writer.writerow([uid, i[1], cash, i[3]])
                        else:
                            writer.writerow(i)
                        
            os.remove(r"bank_main.csv")
            os.rename(r"new.csv", r"bank_main.csv")

        if act == 6:
            uid = input("Enter your A/c no>: ")
            mob = input("Enter your number: ")
            with open("bank_main.csv", "r") as reader, open("new.csv", 'w+') as writer:
                reader = csv.reader(reader)
                writer = csv.writer(writer)
                for i in reader:
                    if i!= []:
                        if uid == i[0]:
                            writer.writerow([uid, mob, i[2], i[3]])
                        else:
                            writer.writerow[i]

            os.remove(r"bank_main.csv")
            os.rename(r"new.csv", r"bank_main.csv")