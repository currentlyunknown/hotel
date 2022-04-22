# Hotel API

This app is an API for a hotel that allows to create bookings with rooms and customers and retrieve the data.<br>
It allows to CRUD the info for customers, rooms and bookings in your local PostgreSQL database (it will create the DB for you if not present).<br>
Stack used: FastAPI, PostgreSQL, pytest<br>

# Installing

- git clone "repository" .
- add an .env file with the following data:

POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
DATABASE_URL


# Using the API
If "hotel" database is not created, the API will create it for you.

# Start the server using bash
uvicorn main:app --reload

# Getting the data
Use one of the following parameters: customer, room, booking, followed by an id<br>
Example: /customer/2

The plural syntax for the parameter will give you a list of all the data available for a parameter<br>
Example: /customers

Example response:
{"id":3,"first_name":"Jack","last_name":"Black","email_address":"jack@black.com"}