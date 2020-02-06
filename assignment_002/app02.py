"""
APP ::::
Makes a list of film dictonary that has all films that begins with 'zo'.
The dictonary has film id, name, all actors first and last name for that film and a short description of the film...
"""
import mysql.connector

### START :: DATA EXTRACTION COMPLETE ##################################################################################

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "wolfPack#2020",
  database = "sakila"
)

cur = mydb.cursor()

cur.execute("""
select a.actor_id, a.first_name, a.last_name, f.film_id, f.title, f.description from film as f
INNER JOIN film_actor as fa ON f.film_id = fa.film_id
INNER JOIN actor as a ON fa.actor_id = a.actor_id
where title like lower('zo%')
""")

data = cur.fetchall()

### END :: DATA EXTRACTION COMPLETE #####################################################################################

def display_films(data):
  films_id = {unique_film[3] for unique_film in data}
  films_n_actors = []

  'Making dictonary of films that has id, title, actors of that film and short description'
  for id in films_id:
    fna = {}
    fna["film_id"] = id                                                                     # Id of film
    fna["film_name"] = {film[4] for film in data if film[3] == id}                          # film name
    fna["film_actors"] = [f'{actor[1]} {actor[2]}' for actor in data if actor[3] == id]     # all actors of the film
    fna["film_desc"] = {desc[5] for desc in data if desc[3] == id}                          # short description of the film
    films_n_actors.append(fna)

  [print(result) for result in films_n_actors]

display_films(data)