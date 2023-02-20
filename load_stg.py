import psycopg2
from faker import Faker
from config import host, user, password, db_name

fake = Faker(locale="ru_RU")

try: 
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(open('SQL\CREATE_SCHEMA.sql').read())
        cursor.execute(open('SQL\CREATE_ROW_CLIENTS.sql').read())
        cursor.execute("TRUNCATE stg.row_clients RESTART IDENTITY")
        for i in range(1000000):
            registration_date = fake.date_between(start_date = "-3y")
            name = fake.name()
            city = fake.city_name()
            job = fake.job()
            phone_number = fake.phone_number()
            inn = fake.individuals_inn()
            bank = fake.bank()
            provider = fake.credit_card_provider()
            birthdate = fake.date_between(start_date = "-65y", end_date= "-21y") 
            credit = fake.random_int(-1, 1)
            sql = f"""INSERT INTO 
            stg.row_clients (
                registration_date, name, city, job, phone_numb, inn, bank, provider, birthdate, credit) 
            VALUES (
                '{registration_date}', '{name}', '{city}', '{job}', '{phone_number}', {inn}, '{bank}', '{provider}', '{birthdate}',{credit})"""
   
            cursor.execute(sql)
            
        cursor.execute("SELECT version()")
        print(cursor.fetchone())
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")