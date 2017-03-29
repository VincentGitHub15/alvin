import psycopg2
from psycopg2.extras import RealDictCursor


hostname = 'localhost'
username = 'Lisa' #postgres is the owner in psql 
password = 'secret'
database = 'test'

#creates db
connection = psycopg2.connect(dbname=database)

#create cursor factory
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor(cursor_factory=RealDictCursor)



search =  "CT Head W W/O Contrast"

cursor.execute('''
	SELECT name, address, description, tot_price, image, rating, reviews
	FROM procedures 

	JOIN procedure_types
	ON procedure_types.id = procedures.id_procedure_types

	JOIN facilities 
	ON procedures.id_facilities = facilities.id

	WHERE procedure_types.description like 'CT%';
''')
query = cursor.fetchall()
print(query)
# return query


connection.close()