import psycopg2
from psycopg2.extras import RealDictCursor


hostname = 'localhost'
username = 'Lisa' #postgres is the owner in psql 
password = 'secret'
database = 'test'


def get_procedure_info(procedure):
#creates db
	connection = psycopg2.connect(dbname=database)

#create cursor factory
	connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

	cursor = connection.cursor(cursor_factory=RealDictCursor)

# search =  "CT Head W W/O Contrast"
	# print(procedure)
	name = str(procedure)
	print(name)
	cursor.execute('''
		SELECT procedures.id, latitude, longitude, name, address, description, cpt_code, tot_price, image, rating, reviews
		FROM procedures 

		JOIN procedure_types
		ON procedure_types.id = procedures.id_procedure_types

		JOIN facilities 
		ON procedures.id_facilities = facilities.id

		JOIN geolocations
		ON procedures.id_facilities = geolocations.id_facilities

		WHERE procedure_types.description = (%s);

	''', (name,))
	# print(name)
	query = cursor.fetchall()
	# print(query)
	return query
	# returns a list of DICTS...
	connection.close()

# get_procedure_info('CT')





def get_cpt_info(procedure):
#creates db
	connection = psycopg2.connect(dbname=database)

#create cursor factory
	connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

	cursor = connection.cursor(cursor_factory=RealDictCursor)

# search =  "CT Head W W/O Contrast"
	# print(procedure)
	num = int(procedure)
	print(num)
	cursor.execute('''
		SELECT procedures.id, latitude, longitude, name, address, description, cpt_code, tot_price, image, rating, reviews
		FROM procedures 

		JOIN procedure_types
		ON procedure_types.id = procedures.id_procedure_types

		JOIN facilities 
		ON procedures.id_facilities = facilities.id

		JOIN geolocations
		ON procedures.id_facilities = geolocations.id_facilities

		WHERE procedure_types.cpt_code = (%s);

	''', (num,))
	# print(data)
	query = cursor.fetchall()

	return query
	# returns a list of DICTS...
	connection.close()

		


