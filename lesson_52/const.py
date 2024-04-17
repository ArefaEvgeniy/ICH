dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'sakila'}

QUERY_CATEGOTIES = 'SELECT category_id, name FROM category'

QUERY_FILMS = """
SELECT title, release_year, description
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.category_id = {} LIMIT 10;
"""
