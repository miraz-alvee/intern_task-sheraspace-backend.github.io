# intern_task-sheraspace-backend.github.io

## Project setup
Create a .env file in the root directory:

## Clone the Reposity
```bash
$ git clone [this repository]
$ cd [project name]
```
```bash
$ pip install
```

## Compile and run the project

```bash
# development
$ flask run 

# watch mode
$ python app.py


## Create a .env file in the root directory:

DB_HOST=your-database-host
DB_PORT=5432
DB_USERNAME=your-username
DB_PASSWORD=your-password
DB_DATABASE=your-database


```
## Api end point

| Method | Endpoint       | Description               |
|--------|----------------|---------------------------|
| GET    | `/tasks/:id`   | Get user tasks           |
| POST   | `/tasks`       | create tasks       |
| PUT    | `/tasks`       | edit task     |
| DELETE | `/tasks/:id`   | Delete a specific tasks    |
