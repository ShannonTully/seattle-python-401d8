# PostgreSQL Shell

## Starting the server
*You must do this every time you restart your machine*
```
$ brew services start postgres
```

## Creating a user-default database
```
$ createdb
<!-- This will create a new database with the same name as your user login -->
<!-- You only have to do this once -->

$ createdb twitter
<!-- This will create a new database called twitter, which can contain many individual tables -->
```

## Starting the postgres shell
```
$ psql

sjschmidt=# # this is your sql shell prompt
<!-- With no arguments, `psql` will start the shell at your user-default database -->

$ psql twitter

twitter=#
<!-- This will start the shell at our twitter database -->
```

## Quit the postgres shell
```
sjschmidt=# \q

$
```

## Basic shell navigation
#### List all of your databases
```
sjschmidt=# \l

List of databases
Name    |   Owner   | Encoding |   Collate   |    Ctype    |    Access privileges
-----------+-----------+----------+-------------+-------------+----------
movies    | sjschmidt | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
sjschmidt | sjschmidt | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
(2 rows)

```

#### Connect to a database
```
sjschmidt=# \c movies
You are now connected to database "movies" as user "sjschmidt".
movies=# \c sjschmidt
You are now connected to database "sjschmidt" as user "sjschmidt".
```

#### List all relations (tables) in the database
```
sjschmidt=# \dt

List of relations
Schema |   Name   | Type  |   Owner
--------+----------+-------+-----------
public | articles | table | sjschmidt
public | authors  | table | sjschmidt
(4 rows)
```

#### Display the schema configuration (column properties)
```
sjschmidt=# \d articles

Table "public.authors"
Column   |          Type          |       Modifiers
-----------+------------------------+-----------------------
author_id | integer                | not null default
author    | character varying(255) | not null
authorUrl | character varying(255) |
Indexes:
  "authors_pkey" PRIMARY KEY, btree (author_id)
```

-----

# Structured Query Language Cheat Sheet

## Working with Tables
#### Creating a new table
```sql
CREATE TABLE IF NOT EXISTS
users(
  id SERIAL PRIMARY KEY NOT NULL,
  first_name VARCHAR(256) NOT NULL,
  last_name VARCHAR(256) NOT NULL,
  ssn INTEGER NOT NULL,
  ninja_status BOOLEAN NOT NULL,
  biography TEXT NOT NULL
);
```

#### Deleting a table
```sql
DROP TABLE users;
```

## Working with Records
#### Reading all record from the DB
```sql
SELECT * FROM users;
```

#### Reading a specific record from the DB
```sql
SELECT * FROM users WHERE id=3;
```

#### Inserting a new record
```sql
INSERT INTO users(first_name, last_name, ssn, ninja_status, biography)
VALUES('Flibbity', 'Jibbit', 333-44-5555, TRUE, "By the time of the Meiji Restoration (1868), the tradition of the shinobi had become a topic of popular imagination and mystery in Japan. Ninja figured prominently in legend and folklore, where they were associated with legendary abilities such as invisibility, walking on water and control over the natural elements. As a consequence, their perception in popular culture is often based on such legend and folklore than on the spies of the Sengoku period.");
```

#### Updating an existing record
```sql
UPDATE users
SET
  first_name="Flibbity",
  last_name="Jibbit",
  ssn=333-44-5555,
  ninja_status=FALSE, -- We changed this value!!
  biography="By the time of the Meiji Restoration (1868), the tradition of the shinobi had become a topic of popular imagination and mystery in Japan. Ninja figured prominently in legend and folklore, where they were associated with legendary abilities such as invisibility, walking on water and control over the natural elements. As a consequence, their perception in popular culture is often based on such legend and folklore than on the spies of the Sengoku period."
WHERE id=3;
```

#### Deleting a record from the DB
```sql
DELETE FROM users WHERE id=3;
```
