def login_page():
    import mysql.connector

    print("IF YOU WANT TO DELETE YOUR ACCOUNT FROM JARVIS PRESS (d)")
    ch = input("ARE YOU NEW TO JARVIS? \n(y/n/d): ")
    if ch == 'y' or ch == 'yes':
        print("PLEASE CREATE A NEW ACCOUNT")
        con = mysql.connector.connect(host="localhost", user="root", password="spaytm17", database="virtual_assistant")
        cur = con.cursor()

        name = input("ENTER YOUR NAME : \n").capitalize()
        password = input("ENTER THE PASSWORD YOU WANT : \n")
        gender = input("ENTER YOUR GENDER : \n").capitalize()

        def joint():
            try:
                email = input("ENTER YOUR EMAIL ID : \n")
                q = "INSERT INTO JARVIS VALUES('{}','{}','{}','{}')".format(name, email, password, gender)

                cur.execute(q)
                con.commit()
                return email
            except:
                print("YOU HAVE ENTERED SOMEONE ELSE'S EMAIL PLEASE A DIFFERENT EMAIL")
                joint()

        a = joint()

        def join(email):
            try:
                user_name = input("ENTER THE USER NAME YOU WANT : \n")
                q1 = "INSERT INTO JARVIS_USER_NAME VALUES('{}','{}')".format(email, user_name)
                cur.execute(q1)
                con.commit()
                print("JUST REMEMBER YOUR USER NAME")
            except:
                print("USER NAME NOT AVAILABLE PLEASE TRY AGAIN")
                join(email)

        join(a)


        print("ACCOUNT CREATED SUCCESSFULLY")
        print("YOU NEED TO LOGIN AGAIN TO USE J.A.R.V.I.S")

        ch1 = input("HAVE YOU CREATED AN USER NAME ALREADY OR SAVED YOUR LOGIN INFORMATION\n(y/n): ")
        if ch1 == "y":
            con = mysql.connector.connect(host="localhost", user="root", password="spaytm17",
                                          database="virtual_assistant")
            cur = con.cursor()
            un = input("ENTER YOUR PERSONAL USER NAME : \n")
            q = "select * from jarvis_user_name inner join jarvis on jarvis_user_name.email = jarvis.email WHERE user_name = '" + un + "'"
            cur.execute(q)
            d = cur.fetchone()
            user_name = d[1]
            name = d[2]
            email = d[3]
            password = d[4]
            gender = d[5]
            return user_name, name, email, password, gender, ch
            # a = [user_name, name, email, password, gender]
            # print(a)

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="spaytm17",
                                          database="virtual_assistant")
            cur = con.cursor()
            em = input("ENTER THE EMAIL ID YOU WANT TO SEARCH : \n")
            pwd = input("ENTER THE PASSWORD YOU WANT TO SEARCH : \n")
            q = "SELECT * FROM JARVIS WHERE email = '" + em + "' AND password = '" + pwd + "'"
            cur.execute(q)
            d = cur.fetchone()
            user_name = d[1]
            name = d[2]
            email = d[3]
            password = d[4]
            gender = d[5]
            return user_name, name, email, password, gender, ch
            # a = [user_name, name, email, password, gender]
            # print(a)



    elif ch == 'd':
        con = mysql.connector.connect(host="localhost", user="root", password="spaytm17", database="virtual_assistant")
        cur = con.cursor()
        eml = input("ENTER THE EMAIL YOU WANT TO DELETE : \n")
        q2 = "DELETE FROM jarvis WHERE email = '" + eml + "'"
        cur.execute(q2)
        con.commit()
        q3 = "DELETE FROM jarvis_user_name WHERE email = '" + eml + "'"
        cur.execute(q3)
        con.commit()
        print("ACCOUNT DELETED SUCCESSFULLY")
        exit()

    else:
        ch1 = input("HAVE YOU CREATED AN USER NAME ALREADY OR SAVED YOUR LOGIN INFORMATION\n(y/n): ")
        if ch1 == "y":
            con = mysql.connector.connect(host="localhost", user="root", password="spaytm17", database="virtual_assistant")
            cur = con.cursor()
            un = input("ENTER YOUR PERSONAL USER NAME : \n")
            q = "select * from jarvis_user_name inner join jarvis on jarvis_user_name.email = jarvis.email WHERE user_name = '" + un + "'"
            cur.execute(q)
            d = cur.fetchone()
            user_name = d[1]
            name = d[2]
            email = d[3]
            password = d[4]
            gender = d[5]
            return user_name, name, email, password, gender, ch
            # a = [user_name, name, email, password, gender]
            # print(a)

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="spaytm17", database="virtual_assistant")
            cur = con.cursor()
            em = input("ENTER THE EMAIL ID YOU WANT TO SEARCH : \n")
            pwd = input("ENTER THE PASSWORD YOU WANT TO SEARCH : \n")
            q = "SELECT * FROM JARVIS WHERE email = '" + em + "' AND password = '" + pwd + "'"
            cur.execute(q)
            d = cur.fetchone()
            user_name = d[1]
            name = d[2]
            email = d[3]
            password = d[4]
            gender = d[5]
            return user_name, name, email, password, gender, ch
            # a = [user_name, name, email, password, gender]
            # print(a)

