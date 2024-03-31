import psycopg2 as psql

class DATABASE:
    @staticmethod
    def connect(query, type):
        database = psql.connect(
            database = 'instagram_register',
            user = 'postgres',
            host = 'localhost',
            password = '1605'
        )

        cursor = database.cursor()
        cursor.execute(query)

        if type in ['create', 'delete', 'update', 'insert']:
            database.commit()

        elif type == 'select':
            return cursor.fetchall()
