CREATE TABLE IF NOT EXISTS stg.row_clients(
    id serial PRIMARY KEY,
    registration_date DATE,
    name VARCHAR(50), 
    city VARCHAR(50), 
    job VARCHAR(50), 
    phone_numb VARCHAR(50),
    inn BIGINT,
    bank VARCHAR(50),
    provider VARCHAR(50),
    birthdate DATE,
    credit INT
)

