from dabase import conn, cursor1

def show_likes(username,film_id,film_type):
    cursor1.execute(f"select * from users where username = '{username}'")
    person = cursor1.fetchone()
    query = f"select * from movies where id = ? and type = ? "
    values = (film_id,film_type)
    cursor1.execute(query,values)
    film = cursor1.fetchone()
    if film == None:
        return None
    else:
        values4 = (film[1],username)
        cursor1.execute("select * from likes where movie = ? and username = ? ", values4)
        explain = cursor1.fetchone()
        if explain == None:
            query2 = """insert into `likes`(
                `movie`,
                `username`
                ) values (? , ?)
            """ 
            values2 = (film[1], username)
            cursor1.execute(query2, values2)
            conn.commit()
            like_num = int(film[-1]) + 1
            query3 = f"update movies set likes = ? where id = ?"
            values3 = (like_num,film_id)
            cursor1.execute(query3,values3)
            return True
        else:
            return False
            
# show_likes('muradxan005',34,'movie')


def my_movies(username):
    data = (username)
    cursor1.execute(f"select * from likes where username = '{username}' ")
    user_movies = cursor1.fetchall()
    if user_movies == None:
        return False
    movies_data = []
    for i in user_movies:
        movies_data.append({"Film name": i[0], "Comment": 'You like this film ❤'})
    return movies_data

my_movies('muradxan005')

def show_movies(type1):
    cursor1.execute(f"select * from movies where type ='{type1}'")
    movies = cursor1.fetchall()
    movies_data = []
    for i in movies:
        movies_data.append({'Id': i[0], 'Title': i[1], 'Year': i[2], 'Rating': i[3], 'Type': i[4], "Likes": i[5]})
    return movies_data

show_movies('movie')

