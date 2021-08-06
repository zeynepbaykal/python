import pyodbc

conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=DESKTOP-ACB6R2Q;Database=PythonFinal;Trusted_Connection=yes;")

def loginscreen():
    print("Welcome to shopping site")
    print("1. Register ")
    print("2. Login for shopping")
    print("0. Exit")
    option = input("Select an option.")
    if(option == "1"):

        name = input("~ Please enter your name!\n")
        surname = input("~ Please enter your surname!\n")
        tcno = input("~ Please enter your TC No!\n")
        username2 = input("~ Please enter your Username!\n")
        password2 = input("~ Please enter your password!\n")
        authority = input("~ Please enter your authority!\n")

        cursor = conn.cursor()
        cursor.execute("INSERT INTO TblUsers(Name, Surname, TcNo, Username, Password, Auth) VALUES(?,?,?,?,?,?)", name, surname, tcno, username2, password2, str(authority))
        conn.commit()

        print("username and password has been made")
        loginscreen()

    elif(option == "2"):
        control = 0
        print("Please enter your details to log in")
        username1 = input("Please enter your username: ")
        password1 = input("Please enter your password: ")

        cursor = conn.cursor()
        cursor.execute("select Username,Password,Auth from TblUsers")

        for row in cursor:
            username = row[0]
            password = row[1]
            auth = row[2]

            if username1 == username and password1 == password:
                control=1
                print("Hello : ", username)
                print("Auth : ", auth)
                
                if(auth==1):
                    auth="1"
                    mainMenu(auth="1")

                elif(auth==2):
                    print("Hello User")
                    auth="2"
                    mainMenu(auth="2")

        if(control==0):
            print("Incorrect pass or id")
    elif(option=="0"):
        print("Program closed.")
        exit()

def mainMenu(auth):
    if(auth == "1"):
        print("Hello Admin : ")
        print("1. Add Main Category")
        print("2. Add Sub Category")
        print("3. Add Product")
        print("4. List Product")
        choice = input("Please select a number : ")
        if(choice=="1"):
            addMainCategory()
        elif(choice=="2"):
            addSubCategory()
        elif(choice =="3"):
            addProduct() 
        elif(choice=="4"):
            listProduct() 
    if(auth == "2"):
        print("1. List The Products")
        chuser = input("Enter choice : ")
        if(chuser == "1"):
            listProduct()

def listProduct():
    listCategory()
    subId = input("Please select sub-category")

    cursor = conn.cursor()
    cursor.execute("select ProductName from TblProduct where SubId='%s'" % int(subId))

    for row in cursor:
        print(row, end='\n')

    loginscreen()


def addMainCategory():
    inpValue = input("How many categories do you want to add \n")
    a=0
    for i in range(int(inpValue)):
        mainCtgName = input("Please Enter a Main Category Name: ")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TblMaiNCategories(MainCtgName) VALUES(?)", mainCtgName)
        conn.commit()
    mainMenu(auth="1")
def addSubCategory():
    print("Please select category to add sub-category")

    cursor = conn.cursor()
    cursor.execute("select MainCtgId,MainCtgName from TblMainCategories")

    for i in cursor:
        print(i, end='\n')

    cursor.close()
    selectCtg = input("\nPlease select number of main category : ")
    
    cr = conn.cursor()
    cr.execute("select MainCtgId,MainCtgName from TblMainCategories")

    for row in cr:
        ctgId = row[0]
        ctgName = row[1] #

        #print(ctgName, end='')
        if(int(selectCtg) == ctgId):
            print("Selected ctg : " + str(ctgId))
            subCtgName = input("Please enter a sub category name : ")
            cr.close()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO TblSubCategories(MainCtgId, SubCtgName) VALUES(?, ?)", ctgId, subCtgName)
            conn.commit()
            conn.close()
            mainMenu(auth="1")
        else:
            print("Please control the selection")    


def listCategory():
    print("Categories")

    cursor = conn.cursor()
    cursor.execute("select * from TblMainCategories")
    for i in cursor:
        print(i, end='\n')
    cursor.close()

    selectCtg = input("Please select number of main category.")
    cursor = conn.cursor()
    cursor.execute("select * from TblSubCategories where MainCtgId='%s'" % int(selectCtg))

    for row in cursor:
        print(str(row[0])+". "+str(row[2]))
    cursor.close()

def addProduct():
    listCategory()
    inpPrd = input("Please select sub-category for add new product : ")

    cursor = conn.cursor()
    cursor.execute("select * from TblSubCategories where SubCtgId='%s'" % int(inpPrd))

    for i in cursor:
        subCtgId = i[0]
        mainCtgId = i[1]

    cursor.close()

    inpValue = input("How many products do you want to add \n")
    for i in range(int(inpValue)):
        prdName = input("Please enter product name : ")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TblProduct(MainId, SubId, ProductName) VALUES(?,?,?)", mainCtgId, subCtgId, prdName)
        conn.commit()
    cursor.close()
    mainMenu(auth="1")

loginscreen()
