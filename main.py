from dabase import creat_user,user_check,user_delete,check_password,check_admin,add_admin,show_admins
from movie import show_likes,show_movies,my_movies
import os
from datetime import datetime
import time
from tabulate import tabulate

    
class Movies:
    def __init__(self):
        pass

    def show_movies(self, type):
        movies = show_movies(type)
        print(tabulate(movies, headers='keys', tablefmt='grid'))
        print('1. Go back main menu ! | 2. Exit')
        ans = int(input('Enter:'))
        if ans == 1:
            menu()
        elif ans == 2:
            quit()




class Users:
    def __init__(self):
        pass

    def show_like(self, username):
        print('1.Movie 🎥 | 2.Series 📽')
        tp = int(input('Enter type:'))
        tg = ''
        if tp == 1:
            movies = show_movies('movie')
            print(tabulate(movies, headers='keys', tablefmt='fancy_grid'))
            film_type = 'movie'
        else:
            movies = show_movies('series')
            print(tabulate(movies, headers='keys', tablefmt='fancy_grid'))
            film_type = 'series'

        film_id = int(input('Enter film id:'))
        like = show_likes(username, film_id, film_type)
        if like == None:
            print('This movie is not exist ❌')
        elif like:
            print(f'You liked that {tg} ❤')
        else:
            print(f'You have already liked that {tg} ❤')
        time.sleep(3)
        self.login_menu(username)

    def login_menu(self,username):
        os.system('cls')
        print(f"\t\tHi {username} welcome to your page ✋\n")
        print("1.My movies 🎥 | 2.Likes 💖 | 3.Log out 🔃\n")
        ans = int(input("Choose:"))
        if ans == 1:
           data = my_movies(username)
           if data == None:
               print('You have not film 🎥')
               time.sleep(3)
               self.login_menu(username)
           else:
               print(tabulate(data, headers='keys', tablefmt='psql'))
               print('1.Back << | 2.Log out')
               ans2 = int(input("Enter:"))
               if ans2 == 1:
                   self.login_menu(username)
               else:
                   menu()
        elif ans == 2:
            self.show_like(username)
        elif ans == 3:
            a = True
            while a:
                agreement = input('Do you really want to log out[y/n]:')
                if agreement == 'y':
                    a = False
                    menu()
                elif agreement == 'n':
                    a = False
                    self.login_menu(username)
                else:
                    print("Please enter just 'y' or 'n':")



    def check_user(self,username):
        data = user_check(username)
        return data
    
    def login(self):
        p = True
        while p:
            username = input("Enter username:")
            ans = self.check_user(username=username)
            if ans:
                password_count = 3
                while password_count:
                    password = input("Enter password:")
                    ask = check_password(password,username)
                    if ask:
                        self.login_menu(username)

                    else:
                        password_count-=1
                        print(f"Incorrect password ❌ \n {password_count} chance!")
                        if password_count == 0:
                            os.system('cls')
            else:
                print("There is not user in the list ❌ ")


    def register(self):
        name = input("Enter your name:")
        p = True
        while p:
            username = input("🤵 Enter username:")
            ans = self.check_user(username=username)
            if not ans:
                password = input("🔐 Enter password:")
                creat_user(name,username,password)
                p = False
            else:
                print("This username already exists ❌")
        print('Successfully ✔')
        time.sleep(2)
        menu()


class Admin(Users):
    def __init__(self):
        super().__init__()

    def show_admins(self, username):
        data = show_admins()
        print(tabulate(data,headers='keys',tablefmt='fancy_grid'))
        print("1.Back <<< | 2.Log out")
        ans = int(input("Choose: "))
        if ans == 1:
            self.login_menu(username=username)
        elif ans == 2:
            menu()


    def login_menu(self,username):
        os.system('cls')
        print(f"\t\tHi {username} welcome to your page ✋\n")
        print("1.My movies 🎥 | 2.Likes 💖 | 3.Delete user 🧺 | 4.Add admin ➕ | 5.Show Admins 🧝‍ | 6.Log out 🔃\n")
        ans = int(input("Choose:"))
        if ans == 1:
            data = my_movies(username)
            if data == None:
                print('You have not film 🎥')
                time.sleep(3)
                self.login_menu(username)
            else:
                print(tabulate(data, headers='keys', tablefmt='psql'))
                print('1.Back << | 2.Log out')
                ans2 = int(input("Enter:"))
                if ans2 == 1:
                    self.login_menu(username)
                else:
                    menu()
        elif ans == 2:
           self.show_like(username)
        elif ans == 3:
            a = True
            while a:
                du = input("🧟‍♂️ Unnecessary User's username:")
                data = user_delete(du)
                if type(data) == type('str'):
                    print(data)
                    a = False
                    time.sleep(2)
                    self.login_menu(username=username)
                else:
                    print('This user does not exists ❌')
        elif ans == 4:
            p = True
            while p:
                user = input("😎 Enter user you want to be an admin:")
                data2 = user_check(user)
                if data2:
                    admin_data = check_admin(user)
                    if admin_data:
                        print(f'{user} already admin 💥')
                        time.sleep(3)
                        p = False
                        self.login_menu(username=username)
                    else:
                        add_admin(user)
                        print("Admin add 🟢")
                        time.sleep(2)
                        p = False
                        self.login_menu(username=username)
                else:
                    print("We have not anything abut this user 🤔 ")
        elif ans == 5:
            self.show_admins(username)
        elif ans == 6:
            a = True
            while a:
                agreement = input('Do you really want to log out[y/n]:')
                if agreement == 'y':
                    a = False
                    menu()
                elif agreement == 'n':
                    a = False
                    self.login_menu(username)
                else:
                    print("Please enter just 'y' or 'n':")
    def login(self):
        p = True
        while p:
            username = input("🤵 Enter username:")
            ans = check_admin(username=username)
            if ans:
                password_count = 3
                while password_count:
                    password = input("🔐 Enter password:")
                    ask = check_password(password,username)
                    if ask:
                        self.login_menu(username)
                    else:
                        password_count-=1
                        print(f"Incorrect password ❌ \n {password_count} chance!")
                        if password_count == 0:
                            os.system('cls')
            else:
                print("There is not admin in the list ❌ ")
    



def menu():
    os.system('cls')
    print("""
    \t\t\t\t\t\t _🎥_🎥_🎥_🎥_🎥_🎥_
    \t\t\t\t\t\t| WELCOME TO UZMOVIE|
    \t\t\t\t\t\t|_🎥_🎥_🎥_🎥_🎥_🎥_|
    """)
    print('___________________________________________________________________________________________________________')
    print("""
    \t\t\t\t1. MOVIES | 2.SERIES | 3.REGISTER | 4. LOG IN 
    """)
    ask = int(input("Choose:"))
    if ask == 1:
        movie = Movies()
        movie.show_movies('movie')
    elif ask == 2:
        movie = Movies()
        movie.show_movies('series')
    elif ask == 3:
        new_user = Users()
        print(new_user.register())
    elif ask == 4:
        ans = True
        while ans:
            t = input("Who are you? [admin/user]:").lower()
            if t == 'user':
                ans = False
                new_user = Users()
                new_user.login()
            elif t == 'admin':
                ans = False
                admin = Admin()
                admin.login()
            else:
                print("Please enter just showed!")
menu()
