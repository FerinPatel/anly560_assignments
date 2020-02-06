"""
SIMPLE APP -- 
Prints a list of film dictonary that has all films that begins with 'zo'.
The dictonary has film id, name, all actors first and last name for that film and a short description of the film...
"""
import mysql.connector
import fna_dict

### START :: DATA EXTRACTION ##################################################################################

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

### END :: DATA EXTRACTION #####################################################################################

"""Print all data fetched"""
result = fna_dict.display_films(data)
[print(films_info) for films_info in result]
