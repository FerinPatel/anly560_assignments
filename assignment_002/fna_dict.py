"""
func. that creates a dict...
"""

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

  return films_n_actors
