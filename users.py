import sqlite3
db = sqlite3.connect('guestbook.db')
is_logged_in = False
user_id = 0 # 0 means not set / not logged in.

def register():
    username = str(input('Please enter a username: '))
    if username_available(username) == True :
        import hashlib, time
        password = input('Please enter a password: ').encode('utf_8')
        encrypted = hashlib.sha256()
        encrypted.update(password)
        newpass = encrypted.hexdigest()
        
        currenttime = int(time.time())
        db.execute('insert into users (username, password, date_joined) values (?,?,?)',(username,newpass, currenttime))
        db.commit()
        print('You have been added to the user database')
        return True
    else:
        print('Unfortunately, that username is already taken. Please try again')
        register()
def login():
    username = input('Please enter your username: ')
    if username_available(username) == False: #if its taken, then it must exist.
        import hashlib
        password = input('Please enter your password: ').encode('utf_8')
        encrypted = hashlib.sha256()
        encrypted.update(password)
        newpass = encrypted.hexdigest()
        
        db.row_factory = sqlite3.Row
        row = db.execute('select id from users where username = ? and password = ?', (username, newpass))
        if row is None:
            print('Sorry, that password doesn\' match the username')
        else:
            user_id = row.fetchone()['id']
            is_logged_in = True
    else:
        print('That user doesn\'t exist. Register it?')
def logout():
    pass
def username_available(username):
    db.row_factory = sqlite3.Row
    row = db.execute('select id from users WHERE username = ?',(username,))
    
    if row.fetchone() is None:
        return True
    else:
        return False
