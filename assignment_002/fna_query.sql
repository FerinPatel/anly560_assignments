-- create a query that displays the film title, description, as well the actor first and last name for all films that begin with the letters 'zo'.

SELECT a.first_name, a.last_name, f.title, f.description FROM film AS f
INNER JOIN film_actor AS fa ON f.film_id = fa.film_id
INNER JOIN actor AS a ON fa.actor_id = a.actor_id
WHERE title LIKE lower('zo%')