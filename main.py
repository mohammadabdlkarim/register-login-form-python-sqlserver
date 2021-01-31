import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-9EPAOGD;'
                      'Database=loginSystem;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()


def login(user_name, pass_word):
    cursor.execute("SELECT * FROM account WHERE username = '" + user_name + "'")
    for row in cursor:
        if pass_word == row[3]:
            return user_name, row[1], row[2]
    return False


def register(user_name, user_email, user_country, pass_word):
    cursor.execute("SELECT * FROM account WHERE username = '" + user_name + "' OR email = '" + user_email + "'")
    for row in cursor:
        if user_name == row[0]:
            print("username not available")
            return False
        if user_email == row[1]:
            print("email already exists")
            return False
    cursor.execute("INSERT INTO account(username, email, country, pass)"
               "VALUES('" + user_name + "','" + user_email + "', '" + user_country + "', '" + pass_word + "')")
    conn.commit()
    return True


loginType = input("Enter L for Login or R for Register: ")
if loginType.upper() == 'L':
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        details = login(username, password)
        if len(details) > 0:
            print("username:" + username + '''
email: ''' + details[1] + '''
country: ''' + details[2])
            break
        else:
            print("Wrong username or password")
elif loginType.upper() == 'R':
    while True:
        username = input("Enter a username: ")
        email = input("Enter your email: ")
        country = input("Enter your country: ")
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")
        if password == confirm_password:
            if register(username, email, country, password):
                print("Welcome")
                break
        else:
            print("Passwords doesn't match")

