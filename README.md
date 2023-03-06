# Foodapp
## On-Boarding-Project (OBP) for Yelster Digital by @cvargas

### About Foodapp
Foodapp is dummy application written in python using django to explore the backend stack of the company during the OBP. It offers functionalties such a CRUD for **Restaurants, Customers and Reservations**.

### The relations between the entities are the follow:

- **Restaurants** can have multiple **Restaurant Tables (Tables)**
- **Restaurants** can have multiple **Reservations**
- **Customers** can have **Reservations** of **Tables** in **Restaurants** for a specific **date**

### The interactions between entities are the follow:

- More than one **Reservation** on the same **Table** and **date** is not possible
- Each **Table** belongs only to one **Restaurant**

### Using the endpoints

- **[Restaurants](http://localhost:9000/api/restaurants/)**
- **[Restaurant-Tables](http://localhost:9000/api/restaurant-tables/)**
- **[Customers](http://localhost:9000/api/customers/)**
- **[Reservations](http://localhost:9000/api/reservations/)**

- **Customers** can send **requests** using the **endpoint** of **Reservations** to book a **Table** by sending a valid JSON **Reservation** object. If this is correct, the application *"sends an email"* to the **Customer**.

## Quickstart

### Build docker containers
```bash
docker-compose up -d
```

### Check if docker containers run healthy
In total, 5 docker containers should run in parallel:

```bash
docker-compose ps
```

- Django web app (django)
- Postgres database (db)
- Asynchronous tasks-broker (celery)
- Message-broker receiver (rabbitmq)
- Message-broker responder (redis)

### Acess to foodapp

login at:
- [Django Admin](http://localhost:9000/admin/)

```bash
Username: django
Password: admin
```

See the OpenAPI Documentation at:
- [OpenAPI Documentation](http://localhost:9000/docs/)