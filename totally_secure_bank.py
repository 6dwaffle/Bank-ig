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

a = True

while a == True:
    options()
    act = int(input("input a number between 1 and 7: "))
    file1 = open("bank_main","a") 
    if act >0 and act<8:
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
            a = file_2.readlines()
            for x in a:
                x = x.strip()
                if x == y:
                    y = unique_no()
                    continue
            with file1 as csvfile:
                file_writer = csv.writer("bank_main", delimiter=',')
                file_writer.writerow(['{}'.format(y), '{}'.format(name), '{}'.format(mobile),'{}'.format(balance)])
        if act==7:
            a = False
        if act == 2:
            fileout = open("new.txt","w")
            data = file2.readlines()
            for a in data:
                x = a.split(",")
                if int(x[0])==no:
                    pass
                else:
                    fileout.write(a)
                filein.close()
                fileout.close()
                os.remove(r"numbers.txt")
                os.rename(r"new.txt",r"numbers.txt")