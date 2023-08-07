# REST-API-Flask

> This REST-API is simply me putting my technical skills on Flask and databases (SQLAlchemy here) into practice.
> This is also an implementation of a REST API using Flask to possibly help developers with dummy data for projects they are working on.

# Installing

```
To get started it would be preferable if you create a virtual environment to install extensions.
One way to that would be to use the command below on ubuntu/linux:

python -m venv venv

Then you activate the virtual environment using the command:

source venv/bin/activate

Then you can install the following extensions the project depends on.

pip install flask
pip install flask-sqlalchemy

```

# USAGE


```
General structure

/app_name/api/version/folder

```


### Getting the full list of tasks.

```bash
curl -i http://localhost:5000/todo/api/v1.0/tasks

PS: Ensure the flask app runs on port 5000
```

### Getting a specific task with a particular ID

```bash
curl -i http://localhost:5000/todo/api/v1.0/tasks/id
```

### Adding a new task of the same json structure to the database

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read the Markdown"}' http://localhost:5000/todo/api/v1.0/tasks
```

### Updating a task of particular id in the database

```bash
curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/32

This updates the task with id == 32.
```

### Deleting a task with particular id in the database.

```bash
curl -X DELETE  http://localhost:5000/todo/api/v1.0/tasks/2
```

# Challenges Experienced

> One challenge that stood out was getting the database to update immediately a command is run. This was not the case however. I had to stop the app from running and then kickstart it again to be able to fetch the updated data in the database.

# Contrubutors
* Jacob Precious Chiemezie[click](https://github.com/Cheerio-ban/)


