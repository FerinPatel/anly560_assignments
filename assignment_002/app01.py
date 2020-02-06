"""
SIMPLE APP :: Prints a tuple of all records of film starting with 'zo'
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
select a.first_name, a.last_name, f.title, f.description from film as f
INNER JOIN film_actor as fa ON f.film_id = fa.film_id
INNER JOIN actor as a ON fa.actor_id = a.actor_id
where title like lower('zo%')
""")

data = cur.fetchall()

### END :: DATA EXTRACTION COMPLETE #####################################################################################

"""Print all data fetched"""
[print(row) for row in data]
