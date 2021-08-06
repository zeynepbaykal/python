def loginscreen():
    print("Welcome to shopping site")
    print("1. Register ")
    print("2. Login for shopping")
    print("0. Exit")
    option = input("Select an option.")
    if(option == "1"):
        f = open("accountfile.txt","a+")

        name = input("~ Please enter your name!\n")
        surname = input("~ Please enter your surname!\n")
        tcno = input("~ Please enter your TC No!\n")
        username2 = input("~ Please enter your Username!\n")
        password2 = input("~ Please enter your password!\n")
        authority = input("~ Please enter your authority!\n")

        f.write(f"{name}|{surname}|{tcno}|{username2}|{password2}|{str(authority)}\n")
        f.close()
        print("username and password has been made")
        loginscreen()

    elif(option == "2"):
        control = 0
        print("Please enter your details to log in")
        username1 = input("Please enter your username: ")
        password1 = input("Please enter your password: ")

        file = open("accountfile.txt","r")

        for row in file:
            field = row.split("|")
            username = field[3]
            password = field[4]
            auth = field[5]

            if username1 == username and password1 == password:
                control=1
                print("Hello : ", username)
                print("Auth : ", auth)
                
                if(str(auth[:-1])=="1"):
                    auth="1"
                    mainMenu(auth)

                elif(str(auth[:-1])=="2"):
                    print("Hello User")
                    auth="2"
                    mainMenu(auth)

        if(control==0):
            print("Incorrect pass or id")
        file.close()
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
    x = input("Please select sub-category")

    file = open("products.txt","r")

    for row in file:
        gelen = row.split("|")
        firstId = gelen[0]
        productId = gelen[1] #
        productName = gelen[2]
       
        if(firstId == x):            
            print(productId+". "+productName)

    loginscreen()


def addMainCategory():
    f = open("maincategories.txt","a+")
    inpValue = input("How many categories do you want to add \n")
    a=0
    for i in range(int(inpValue)):
        a+=1
        ctgName = input("Please enter category name : ")
        f.write(f"{str(a)}|{ctgName}\n")
    f.close()
    mainMenu(auth="1")
def addSubCategory():
    print("Please select category to add sub-category")

    bg = open("maincategories.txt", "r")
    ctgs = bg.readlines()

    for i in ctgs:
        print(i, end='')
    bg.close()

    selectCtg = input("Please select number of main category.")

    file = open("maincategories.txt","r")

    for row in file:
        gelen = row.split("|")
        ctg = gelen[0]
        ctgName = gelen[1] #

        print(ctgName, end='')
        if(selectCtg == ctg):
            print("Selected ctg : " + ctg)
            subCtgName = input("Please enter a sub category name : ")
            cnc = open("subcategories.txt", "a+")
            cnc.write(f"{ctg}|{ctgName[:-2]}|{subCtgName}\n")
            cnc.close()
            mainMenu(auth="1")
        else:
            print("Please control the selection")    


def listCategory():
    print("Categories")
    bg = open("maincategories.txt", "r")
    ctgs = bg.readlines()

    for i in ctgs:
        print(i, end='')
    bg.close()
    selectCtg = input("Please select number of main category.")
    file = open("subcategories.txt","r")
    for row in file:
        gelen = row.split("|")
        if(str(gelen[0]) == str(selectCtg)):
            print(gelen[0]+". "+gelen[2])


def addProduct():
    listCategory()
    inpPrd = input("Please select sub-category for add new product : ")

    f = open("products.txt","a+")
    inpValue = input("How many products do you want to add \n")
    a=0
    for i in range(int(inpValue)):
        a+=1
        prdName = input("Please enter product name : ")
        f.write(f"{inpPrd}|{str(a)}|{prdName}\n")
    f.close()
    mainMenu(auth=="1")


loginscreen()
