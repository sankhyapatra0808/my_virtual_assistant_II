import mysql.connector

def register_users():
    user_name = input("BOSS PLEASE CONFIRM YOUR IDENTITY\n(ENTER YOUR USER NAME) : ")
    con = mysql.connector.connect(host="localhost", user="root", password="spaytm17", database="virtual_assistant")
    cur = con.cursor()
    q = "select * from jarvis inner join jarvis_user_name on jarvis_user_name.email = jarvis.email WHERE user_name = '" + user_name + "'"
    cur.execute(q)
    d = cur.fetchone()
    if d[3] == 'Male' or d[3] == 'M':
        print("Login information verified for Mr. " + d[0] + ", Welcome!!")
        name = d[0]
        email = d[1]
        password = d[2]
        gender = d[3]
        user_name = d[5]
        return name, email, password, gender, user_name

    else:
        print("Login information verified for Mrs. " + d[0] + ", Welcome!!")
        name = d[0]
        email = d[1]
        password = d[2]
        gender = d[3]
        user_name = d[5]
        return name, email, password, gender, user_name

register_users()