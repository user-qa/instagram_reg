from sql_connect import DATABASE

user = """
        create table if not exists user_table(
        first_name varchar(20) not null,
        last_name varchar(20) not null,
        email varchar(30) primary key,
        phone_number varchar(12) not null unique,
        username varchar(30) not null unique,
        password varchar(30) not null
        )"""


DATABASE.connect(user, 'create')