
from auth import register, login
from finance import add_transaction, list_transactions, delete_transaction, update_transaction
from budget import set_budget, check_budget
from report import monthly_report, yearly_report
from backup import backup_db, restore_db

def menu():
    while True:
        print("\n1) Add Transaction")
        print("2) View Transactions")
        print("3) Update Transaction")
        print("4) Delete Transaction")
        print("5) Set Budget")
        print("6) Check Budget")
        print("7) Monthly Report")
        print("8) Yearly Report")
        print("9) Backup")
        print("10) Restore")
        print("0) Logout")
        ch=input("Choose: ")

        if ch=="0": break
        elif ch=="1":
            t=input("Type (income/expense): ")
            c=input("Category: ")
            a=float(input("Amount: "))
            add_transaction(uid,t,c,a)
        elif ch=="2":
            print(list_transactions(uid))
        elif ch=="3":
            tid=int(input("ID: "))
            amt=float(input("New amount: "))
            update_transaction(tid,amt)
        elif ch=="4":
            tid=int(input("ID: "))
            delete_transaction(tid)
        elif ch=="5":
            c=input("Category: ")
            l=float(input("Monthly limit: "))
            set_budget(uid,c,l)
        elif ch=="6":
            c=input("Category: ")
            print(check_budget(uid,c))
        elif ch=="7":
            m=input("Month (MM): ")
            print(monthly_report(uid,m))
        elif ch=="8":
            y=input("Year (YYYY): ")
            print(yearly_report(uid,y))
        elif ch=="9":
            backup_db(); print("Backup done.")
        elif ch=="10":
            restore_db(); print("Restore done.")

print("1) Register")
print("2) Login")
ch=input("Choose: ")

if ch=="1":
    u=input("Username: ")
    p=input("Password: ")
    print("Registered!" if register(u,p) else "Failed!")
elif ch=="2":
    u=input("Username: ")
    p=input("Password: ")
    uid=login(u,p)
    if uid:
        print("Login Success")
        menu()
    else:
        print("Invalid login")
