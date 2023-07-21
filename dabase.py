import sqlite3
conn = sqlite3.connect('db.db')
cursor1 = conn.cursor()

#           MOVIES
cursor1.execute("""
    CREATE TABLE if not exists movies(
         id integer not null primary key autoincrement,
         title varchar(40),
         year varchar(5),
         rating varchar(2),
         type varchar(6),
         likes text[]
    )
""")
conn.commit()




# with open('movie.json') as f:
#     data = json.load(f)
#     for i in data:
#         cursor1.execute(f"""
#             insert into movies("title",'year','rating','type','likes')
#             values
#             ('{i["title"]}','{i["year"]}','{i["rating"]}','{i["type"]}','{i["likes"]}')
#         """)
#         conn.commit()


cursor1.execute("""
    create table if not exists  users(
        `id` integer not null primary key autoincrement,
        `name` varchar(30),
        `username` varchar(30),
        `password` varchar(8)

    )
""")
conn.commit()

cursor1.execute("""
    create table if not exists  likes(
        `movie` varchar(30),
        `username` varchar(30)
    )
""")
conn.commit()


def creat_user(name,username,password):
    cursor1.execute(f"""
        insert into users(`name`,`username`,`password`)
        values
        ('{name}','{username}','{password}')
    """)
    conn.commit()

 #  Mavjud adminlar haqida ma'lumotlar 
def show_admins():
    cursor1.execute('select * from admins')
    data = cursor1.fetchall()
    admins_data = []
    for i in data:
        admins_data.append({'ID':i[1],'Username':i[0]})
    return admins_data


# Bu user o'chiriladi va id saqlab qolinadi     
def user_delete(username):
     cursor1.execute(f"select * from `users` where username = '{username}'")
     del_user = cursor1.fetchone()
     if del_user != None:
        if del_user[2] == 'muradxan005':
            return 'You cannot delete superuser 🚫'
        else:
            cursor1.execute(f"delete from users where username = '{username}'")
            cursor1.execute(f"delete from admins where admin_username = '{username}'")
            conn.commit()
            return 'User delete successfully 🟢'
     else:
        return False


# Bu user db da bor yoki yoqligini tekshiradi  
def user_check(user):
    sql = f"SELECT * FROM users WHERE username = '{user}'"
    cursor1.execute(sql)
    res = cursor1.fetchall()
    if res == []:
        return False
    else:
        return True


def check_admin(username):
    sql = f"select * from admins where admin_username = '{username}'"
    cursor1.execute(sql)
    data = cursor1.fetchone()
    if data == None:
        return False
    else:
        return True

# Bu userning paroli va username ni solishtirib ikkalasi bitta user bo'lsa parolni tekshiradi!
def check_password(ps,us):
    sql = f"SELECT * FROM users WHERE username ='{us}'"
    cursor1.execute(sql)
    res = cursor1.fetchone()
    if res[2] == us and res[3] == ps :
        return True
    else:
        return False



def add_admin(username):
    ans = user_check(user=username)
    data = f"select * from users where username = '{username}'"
    cursor1.execute(data)
    user_id = cursor1.fetchone()
    if ans:
         cursor1.execute(f"""
            insert into admins(admin_username,admin_id)
            values
            ('{username}','{user_id[0]}')
        """)
         conn.commit()












