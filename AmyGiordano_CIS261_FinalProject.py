# Amy Giordano
# CIS261 FINAL Project
# 03/06/2023
from datetime import datetime
################################################################################
# Define a function to get the username from the user
def GetUserName():
    return input("Enter the username (type END to stop): ")

# Define a function to get the user's password
def GetUserPassword():
    return input("Enter the user's password: ")

# Define a function to get the user's role
def GetUserRole():
    return input("Enter the user's role: ")

# Define the CreateUsers function
def CreateUsers():
    print('##### Create users, passwords, and roles #####')
    
    # Open the file user_info.txt in append mode and assign to UserFile
    with open("user_info.txt", "a") as UserFile:
        while True:
            # Call function GetUserName and assign the return value to username
            username = GetUserName()
            
            if (username.upper() == "END"):
                break
                
            # Call function GetUserPassword and assign the return value to userpwd
            userpwd = GetUserPassword()
            
            # Call function GetUserRole and assign the return value to userrole
            userrole = GetUserRole()
            
            UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
            UserFile.write(UserDetail)
        
        # Close the file UserFile
        UserFile.close()

# Call the CreateUsers function to create the users
CreateUsers()


       
    

def GetUserName():
    while True:
        username = input("Enter the username (type END to stop): ")
        if username.upper() == "END":
            return username
        elif username.strip() == "":
            print("Please enter a username.")
        else:
            return username

def GetUserPassword():
    while True:
        userpwd = input("Enter the user's password: ")
        if userpwd.strip() == "":
            print("Please enter a password.")
        else:
            return userpwd

def GetUserRole():
    while True:
        userrole = input("Enter role (Admin or User): ")
        if userrole.lower() == "admin" or userrole.lower() == "user":
            return userrole
        else:
            print("Please enter either 'Admin' or 'User'.")

def printuserinfo():
    UserFile = open("user_info.txt","r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "") #remove carriage return from end of line
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpassword = UserList[1]
        userrole = UserList[2]
        print("User Name: ", username, " Password: ", userpassword, " Role: ", userrole)



############################################################################################

def Login():
    # read login information and store in a list
    
    # open the file user_info.txt in read mode
    UserFile = open("user_info.txt", "r")
    
    UserName = input("Enter User Name: ")
    UserRole = "None"
    
    while True:
        # read a line from UserFile and assign it to UserDetail
        UserDetail = UserFile.readline().rstrip("\n")
        
        if not UserDetail:
            # reached end of file, user not found
            UserFile.close()
            return UserRole, UserName
        
        # replace the carriage return in UserDetail
        UserDetail = UserDetail.replace("\r", "")
        
        # split UserDetail on the pipe delimiter (|) and assign it to UserList
        UserList = UserDetail.split("|")
        
        if UserName == UserList[0]:
            UserRole = UserList[2]  # user is valid, return role
            UserFile.close()
            return UserRole, UserName
    
    UserFile.close()
    return UserRole, UserName


#########################################################################################
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
def GetDatesWorked():
    fromdate = input("Enter Start Date (mm/dd/yyyy: ")
    todate = input("Enter End Date (mm/dd/yyyy: ")
    return fromdate, todate
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(DetailsPrinted):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    EmpFile = open("employee_records.txt","r")
    while True:
        rundate = input ("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue  
    while True:
        EmpDetail = EmpFile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetail.rstrip("\n") 
        EmpList = EmpDetail.split("|")
        fromdate = EmpList[0]
        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
            if (checkdate < rundate):
                continue        
        todate = EmpList[1]
        empname = EmpList[2]
        hours = float(EmpList[3])
        hourlyrate  = float(EmpList[4])
        taxrate = float(EmpList[5])
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHrs"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay
        DetailsPrinted = True   
    if (DetailsPrinted):  
        PrintTotals (EmpTotals)
    else:
        print("No detail information to print")
def PrintTotals(EmpTotals):    
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax:  {EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f}')


   

if __name__ == "__main__":
    CreateUsers()    
    print()
    print("##### Data Entry #####")
    UserRole, UserName = Login()


    DetailsPrinted = False  ###
    EmpTotals = {} ###
if UserRole == "NONE":
    print(UserName," is invalid.")

  
    print(UserName," is invalid.")
    
    if UserRole != "ADMIN":
        print("Only Admin users can enter data.")
else:
    EmpFile = open("Employees.txt", "a+")
    # rest of the code

  
    EmpFile = open("Employees.txt", "a+")                
    while True:
                empname = GetEmpName()
                if (empname.upper() == "END"):
                    break
                fromdate, todate = GetDatesWorked()
                hours = GetHoursWorked()
                hourlyrate = GetHourlyRate()
                taxrate = GetTaxRate()
                EmpDetail = fromdate + "|" + todate  + "|" + empname  + "|" + str(hours)  + "|" + str(hourlyrate)  + "|" + str(taxrate) + "\n"  
                EmpFile.write(EmpDetail)
        # close file to save data
EmpFile.close()    
printinfo(DetailsPrinted)




