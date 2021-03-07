DROP TABLE IF EXISTS users.users;
DROP SCHEMA IF EXISTS users;

CREATE SCHEMA users;

CREATE TABLE users.users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL,
    is_activated BOOLEAN NULL,
    activation_token TEXT UNIQUE NOT NULL
);

